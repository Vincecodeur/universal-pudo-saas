from __future__ import annotations

import uuid

from fastapi.testclient import TestClient

from universal_pudo_saas.carrier_accounts.models import (
    CarrierAccount,
)
from universal_pudo_saas.database.session import (
    SessionLocal,
)
from universal_pudo_saas.main import app
from universal_pudo_saas.organisations.models import (
    Organisation,
)

client = TestClient(app)


def test_get_carrier_account_api_returns_account() -> None:
    session = SessionLocal()

    organisation = None
    carrier_account = None

    try:
        organisation = Organisation(
            name="Carrier Account API Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        carrier_account = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="mondialrelay",
            name="Mondial Relay API",
        )

        session.add(carrier_account)
        session.commit()
        session.refresh(carrier_account)

        response = client.get(
            f"/carrier-accounts/{carrier_account.id}",
        )

        assert response.status_code == 200

        payload = response.json()

        assert payload["id"] == str(carrier_account.id)
        assert payload["organisation_id"] == str(organisation.id)
        assert payload["carrier_code"] == "mondialrelay"
        assert payload["name"] == "Mondial Relay API"

    finally:
        if carrier_account is not None:
            session.delete(carrier_account)
            session.commit()

        if organisation is not None:
            session.delete(organisation)
            session.commit()

        session.close()


def test_get_carrier_account_api_returns_404_for_unknown_account() -> None:
    response = client.get(
        f"/carrier-accounts/{uuid.uuid4()}",
    )

    assert response.status_code == 404

    payload = response.json()

    assert payload["detail"] == "Carrier account not found"


def test_list_carrier_accounts_by_organisation_api_returns_accounts() -> None:
    session = SessionLocal()

    organisation = None
    account_1 = None
    account_2 = None

    try:
        organisation = Organisation(
            name="Carrier Account API List Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        account_1 = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="mondialrelay",
            name="MR API",
        )

        account_2 = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="colissimo",
            name="COL API",
        )

        session.add(account_1)
        session.add(account_2)
        session.commit()
        session.refresh(account_1)
        session.refresh(account_2)

        response = client.get(
            f"/carrier-accounts/organisation/{organisation.id}",
        )

        assert response.status_code == 200

        payload = response.json()

        ids = [
            account["id"]
            for account in payload
        ]

        assert str(account_1.id) in ids
        assert str(account_2.id) in ids

    finally:
        if account_1 is not None:
            session.delete(account_1)

        if account_2 is not None:
            session.delete(account_2)

        session.commit()

        if organisation is not None:
            session.delete(organisation)
            session.commit()

        session.close()


def test_list_carrier_accounts_by_organisation_api_returns_empty_list() -> None:
    response = client.get(
        f"/carrier-accounts/organisation/{uuid.uuid4()}",
    )

    assert response.status_code == 200
    assert response.json() == []