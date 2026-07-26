from __future__ import annotations

import uuid

from fastapi.testclient import TestClient

from universal_pudo_saas.carrier_accounts.models import (
    CarrierAccount,
)
from universal_pudo_saas.carrier_credentials.models import (
    CarrierCredential,
)
from universal_pudo_saas.database.session import (
    SessionLocal,
)
from universal_pudo_saas.main import app
from universal_pudo_saas.organisations.models import (
    Organisation,
)

client = TestClient(app)


def test_get_carrier_credential_api_returns_credential() -> None:
    session = SessionLocal()

    organisation = None
    carrier_account = None
    credential = None

    try:
        organisation = Organisation(
            name="Carrier Credential API Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        carrier_account = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="mondialrelay",
            name="MR Credential API",
        )

        session.add(carrier_account)
        session.commit()
        session.refresh(carrier_account)

        credential = CarrierCredential(
            carrier_account_id=carrier_account.id,
            credential_key="api_key",
            credential_value="secret",
        )

        session.add(credential)
        session.commit()
        session.refresh(credential)

        response = client.get(
            f"/carrier-credentials/{credential.id}",
        )

        assert response.status_code == 200

        payload = response.json()

        assert payload["id"] == str(credential.id)
        assert payload["carrier_account_id"] == str(carrier_account.id)
        assert payload["credential_key"] == "api_key"
        assert payload["credential_value"] == "secret"

    finally:
        if credential is not None:
            session.delete(credential)
            session.commit()

        if carrier_account is not None:
            session.delete(carrier_account)
            session.commit()

        if organisation is not None:
            session.delete(organisation)
            session.commit()

        session.close()


def test_get_carrier_credential_api_returns_404_for_unknown_credential() -> None:
    response = client.get(
        f"/carrier-credentials/{uuid.uuid4()}",
    )

    assert response.status_code == 404

    payload = response.json()

    assert payload["detail"] == "Carrier credential not found"


def test_list_credentials_by_carrier_account_api_returns_credentials() -> None:
    session = SessionLocal()

    organisation = None
    carrier_account = None
    credential_1 = None
    credential_2 = None

    try:
        organisation = Organisation(
            name="Carrier Credential API List Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        carrier_account = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="colissimo",
            name="COL Credential API",
        )

        session.add(carrier_account)
        session.commit()
        session.refresh(carrier_account)

        credential_1 = CarrierCredential(
            carrier_account_id=carrier_account.id,
            credential_key="api_key",
            credential_value="secret1",
        )

        credential_2 = CarrierCredential(
            carrier_account_id=carrier_account.id,
            credential_key="account_number",
            credential_value="secret2",
        )

        session.add(credential_1)
        session.add(credential_2)
        session.commit()
        session.refresh(credential_1)
        session.refresh(credential_2)

        response = client.get(
            f"/carrier-credentials/carrier-account/{carrier_account.id}",
        )

        assert response.status_code == 200

        payload = response.json()

        ids = [
            credential["id"]
            for credential in payload
        ]

        assert str(credential_1.id) in ids
        assert str(credential_2.id) in ids

    finally:
        if credential_1 is not None:
            session.delete(credential_1)

        if credential_2 is not None:
            session.delete(credential_2)

        session.commit()

        if carrier_account is not None:
            session.delete(carrier_account)
            session.commit()

        if organisation is not None:
            session.delete(organisation)
            session.commit()

        session.close()


def test_list_credentials_by_carrier_account_api_returns_empty_list() -> None:
    response = client.get(
        f"/carrier-credentials/carrier-account/{uuid.uuid4()}",
    )

    assert response.status_code == 200
    assert response.json() == []