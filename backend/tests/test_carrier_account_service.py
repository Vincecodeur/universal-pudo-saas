from __future__ import annotations

import uuid

from universal_pudo_saas.carrier_accounts.models import (
    CarrierAccount,
)
from universal_pudo_saas.carrier_accounts.service import (
    get_carrier_account_service,
    list_carrier_accounts_for_organisation,
)
from universal_pudo_saas.database.session import (
    SessionLocal,
)
from universal_pudo_saas.organisations.models import (
    Organisation,
)


def test_get_carrier_account_service() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Service Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        carrier_account = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="mondialrelay",
            name="Mondial Relay Service",
        )

        session.add(carrier_account)
        session.commit()
        session.refresh(carrier_account)

        retrieved = get_carrier_account_service(
            session=session,
            carrier_account_id=carrier_account.id,
        )

        assert retrieved is not None
        assert retrieved.id == carrier_account.id

    finally:
        session.delete(carrier_account)
        session.delete(organisation)
        session.commit()
        session.close()


def test_get_carrier_account_service_returns_none() -> None:
    session = SessionLocal()

    try:
        result = get_carrier_account_service(
            session=session,
            carrier_account_id=uuid.uuid4(),
        )

        assert result is None

    finally:
        session.close()


def test_list_carrier_accounts_for_organisation() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Service List Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        account_1 = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="mondialrelay",
            name="MR Service",
        )

        account_2 = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="colissimo",
            name="COL Service",
        )

        session.add(account_1)
        session.add(account_2)
        session.commit()

        results = list_carrier_accounts_for_organisation(
            session=session,
            organisation_id=organisation.id,
        )

        assert len(results) >= 2

    finally:
        session.delete(account_1)
        session.delete(account_2)
        session.delete(organisation)
        session.commit()
        session.close()


def test_list_carrier_accounts_for_organisation_returns_empty_list() -> None:
    session = SessionLocal()

    try:
        results = list_carrier_accounts_for_organisation(
            session=session,
            organisation_id=uuid.uuid4(),
        )

        assert results == []

    finally:
        session.close()