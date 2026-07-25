from universal_pudo_saas.carrier_accounts.models import (
    CarrierAccount,
)
from universal_pudo_saas.database.session import (
    SessionLocal,
)
from universal_pudo_saas.organisations.models import (
    Organisation,
)


def test_carrier_account_can_be_persisted() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Carrier Account Persistence Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        carrier_account = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="mondialrelay",
            name="Mondial Relay Production",
        )

        session.add(carrier_account)
        session.commit()
        session.refresh(carrier_account)

        assert carrier_account.id is not None
        assert carrier_account.organisation_id == organisation.id
        assert carrier_account.carrier_code == "mondialrelay"
        assert carrier_account.name == "Mondial Relay Production"

    finally:
        session.delete(carrier_account)
        session.delete(organisation)
        session.commit()
        session.close()


def test_carrier_account_can_be_retrieved() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Carrier Account Retrieval Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        carrier_account = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="colissimo",
            name="Colissimo Production",
        )

        session.add(carrier_account)
        session.commit()
        session.refresh(carrier_account)

        retrieved = session.get(
            CarrierAccount,
            carrier_account.id,
        )

        assert retrieved is not None
        assert retrieved.organisation_id == organisation.id
        assert retrieved.carrier_code == "colissimo"
        assert retrieved.name == "Colissimo Production"

    finally:
        session.delete(carrier_account)
        session.delete(organisation)
        session.commit()
        session.close()


def test_carrier_account_active_default_is_persisted() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Carrier Account Active Default Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        carrier_account = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="chronopost",
            name="Chronopost Production",
        )

        session.add(carrier_account)
        session.commit()
        session.refresh(carrier_account)

        retrieved = session.get(
            CarrierAccount,
            carrier_account.id,
        )

        assert retrieved is not None
        assert retrieved.is_active is True

    finally:
        session.delete(carrier_account)
        session.delete(organisation)
        session.commit()
        session.close()


def test_carrier_account_can_be_deleted() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Carrier Account Deletion Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        carrier_account = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="ups",
            name="UPS Production",
        )

        session.add(carrier_account)
        session.commit()
        session.refresh(carrier_account)

        carrier_account_id = carrier_account.id

        session.delete(carrier_account)
        session.commit()

        retrieved = session.get(
            CarrierAccount,
            carrier_account_id,
        )

        assert retrieved is None

    finally:
        session.delete(organisation)
        session.commit()
        session.close()
