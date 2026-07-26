from __future__ import annotations

import uuid

from universal_pudo_saas.carrier_accounts.models import (
    CarrierAccount,
)
from universal_pudo_saas.carrier_credentials.models import (
    CarrierCredential,
)
from universal_pudo_saas.carrier_credentials.service import (
    get_carrier_credential_service,
    list_credentials_for_carrier_account,
)
from universal_pudo_saas.database.session import (
    SessionLocal,
)
from universal_pudo_saas.organisations.models import (
    Organisation,
)


def test_get_carrier_credential_service() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Credential Service Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        carrier_account = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="mondialrelay",
            name="MR Credential Service",
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

        retrieved = get_carrier_credential_service(
            session=session,
            carrier_credential_id=credential.id,
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


def test_get_carrier_credential_service_returns_none() -> None:
    session = SessionLocal()

    try:
        result = get_carrier_credential_service(
            session=session,
            carrier_credential_id=uuid.uuid4(),
        )

        assert result is None

    finally:
        session.close()


def test_list_credentials_for_carrier_account() -> None:
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
            carrier_code="mondialrelay",
            name="MR Credential List",
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

        results = list_credentials_for_carrier_account(
            session=session,
            carrier_account_id=carrier_account.id,
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


def test_list_credentials_for_carrier_account_returns_empty_list() -> None:
    session = SessionLocal()

    try:
        results = list_credentials_for_carrier_account(
            session=session,
            carrier_account_id=uuid.uuid4(),
        )

        assert results == []

    finally:
        session.close()