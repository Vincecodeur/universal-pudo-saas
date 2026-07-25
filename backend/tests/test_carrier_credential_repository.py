from universal_pudo_saas.carrier_accounts.models import (
    CarrierAccount,
)
from universal_pudo_saas.carrier_credentials.models import (
    CarrierCredential,
)
from universal_pudo_saas.carrier_credentials.repository import (
    get_carrier_credential,
    list_credentials_by_carrier_account,
)
from universal_pudo_saas.database.session import (
    SessionLocal,
)
from universal_pudo_saas.organisations.models import (
    Organisation,
)


def test_get_carrier_credential() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Credential Repository Organisation",
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

        credential = CarrierCredential(
            carrier_account_id=carrier_account.id,
            credential_key="API_KEY",
            credential_value="secret-value",
        )

        session.add(credential)
        session.commit()
        session.refresh(credential)

        retrieved = get_carrier_credential(
            credential.id,
        )

        assert retrieved is not None
        assert retrieved.id == credential.id

    finally:
        session.delete(credential)
        session.commit()

        session.delete(carrier_account)
        session.delete(organisation)
        session.commit()

        session.close()


def test_list_credentials_by_carrier_account() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Credential List Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        carrier_account = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="colissimo",
            name="Colissimo",
        )

        session.add(carrier_account)
        session.commit()
        session.refresh(carrier_account)

        credential_1 = CarrierCredential(
            carrier_account_id=carrier_account.id,
            credential_key="API_KEY",
            credential_value="key-value",
        )

        credential_2 = CarrierCredential(
            carrier_account_id=carrier_account.id,
            credential_key="API_SECRET",
            credential_value="secret-value",
        )

        session.add(credential_1)
        session.add(credential_2)
        session.commit()

        results = list_credentials_by_carrier_account(
            carrier_account.id,
        )

        assert len(results) >= 2

    finally:
        session.delete(credential_1)
        session.delete(credential_2)
        session.commit()

        session.delete(carrier_account)
        session.delete(organisation)
        session.commit()

        session.close()