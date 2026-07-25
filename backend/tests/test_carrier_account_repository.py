from universal_pudo_saas.carrier_accounts.models import (
    CarrierAccount,
)
from universal_pudo_saas.carrier_accounts.repository import (
    get_carrier_account,
    list_carrier_accounts_by_organisation,
)
from universal_pudo_saas.database.session import (
    SessionLocal,
)
from universal_pudo_saas.organisations.models import (
    Organisation,
)


def test_get_carrier_account() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Repository Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        carrier_account = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="mondialrelay",
            name="Mondial Relay",
        )

        session.add(carrier_account)
        session.commit()
        session.refresh(carrier_account)

        retrieved = get_carrier_account(
            carrier_account.id,
        )

        assert retrieved is not None
        assert retrieved.id == carrier_account.id

    finally:
        session.delete(carrier_account)
        session.delete(organisation)
        session.commit()
        session.close()


def test_list_carrier_accounts_by_organisation() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Repository List Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        account_1 = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="mondialrelay",
            name="MR",
        )

        account_2 = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="colissimo",
            name="COL",
        )

        session.add(account_1)
        session.add(account_2)
        session.commit()

        results = list_carrier_accounts_by_organisation(
            organisation.id,
        )

        assert len(results) >= 2

    finally:
        session.delete(account_1)
        session.delete(account_2)
        session.delete(organisation)
        session.commit()
        session.close()