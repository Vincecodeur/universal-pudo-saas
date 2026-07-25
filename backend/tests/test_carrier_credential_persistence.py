from universal_pudo_saas.carrier_accounts.models import (
    CarrierAccount,
)
from universal_pudo_saas.carrier_credentials.models import (
    CarrierCredential,
)
from universal_pudo_saas.database.session import (
    SessionLocal,
)
from universal_pudo_saas.organisations.models import (
    Organisation,
)


def test_carrier_credential_can_be_persisted() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Carrier Credential Persistence Organisation",
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

        credential = CarrierCredential(
            carrier_account_id=carrier_account.id,
            credential_key="API_KEY",
            credential_value="secret-value",
        )

        session.add(credential)
        session.commit()
        session.refresh(credential)

        assert credential.id is not None
        assert credential.carrier_account_id == carrier_account.id
        assert credential.credential_key == "API_KEY"
        assert credential.credential_value == "secret-value"

    finally:
        session.delete(credential)
        session.commit()

        session.delete(carrier_account)
        session.delete(organisation)
        session.commit()
        session.close()


def test_carrier_credential_can_be_retrieved() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Carrier Credential Retrieval Organisation",
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

        credential = CarrierCredential(
            carrier_account_id=carrier_account.id,
            credential_key="API_SECRET",
            credential_value="retrieval-secret",
        )

        session.add(credential)
        session.commit()
        session.refresh(credential)

        retrieved = session.get(
            CarrierCredential,
            credential.id,
        )

        assert retrieved is not None
        assert retrieved.carrier_account_id == carrier_account.id
        assert retrieved.credential_key == "API_SECRET"
        assert retrieved.credential_value == "retrieval-secret"

    finally:
        session.delete(credential)
        session.commit()

        session.delete(carrier_account)
        session.delete(organisation)
        session.commit()
        session.close()


def test_carrier_credential_foreign_key_is_persisted() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Carrier Credential Foreign Key Organisation",
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

        credential = CarrierCredential(
            carrier_account_id=carrier_account.id,
            credential_key="ACCOUNT_NUMBER",
            credential_value="account-123",
        )

        session.add(credential)
        session.commit()
        session.refresh(credential)

        retrieved = session.get(
            CarrierCredential,
            credential.id,
        )

        assert retrieved is not None
        assert retrieved.carrier_account_id == carrier_account.id

    finally:
        session.delete(credential)
        session.commit()

        session.delete(carrier_account)
        session.delete(organisation)
        session.commit()
        session.close()

def test_carrier_credential_can_be_deleted() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Carrier Credential Deletion Organisation",
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

        credential = CarrierCredential(
            carrier_account_id=carrier_account.id,
            credential_key="USERNAME",
            credential_value="delete-user",
        )

        session.add(credential)
        session.commit()
        session.refresh(credential)

        credential_id = credential.id

        session.delete(credential)
        session.commit()

        retrieved = session.get(
            CarrierCredential,
            credential_id,
        )

        assert retrieved is None

    finally:
        session.delete(carrier_account)
        session.delete(organisation)
        session.commit()
        session.close()