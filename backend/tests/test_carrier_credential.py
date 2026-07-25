import uuid

from universal_pudo_saas.carrier_credentials.models import CarrierCredential


def test_carrier_credential_creation() -> None:
    credential = CarrierCredential(
        carrier_account_id=uuid.uuid4(),
        credential_key="API_KEY",
        credential_value="secret-value",
    )

    assert credential.credential_key == "API_KEY"


def test_carrier_credential_key_is_stored() -> None:
    credential = CarrierCredential(
        carrier_account_id=uuid.uuid4(),
        credential_key="API_SECRET",
        credential_value="secret-value",
    )

    assert credential.credential_key == "API_SECRET"


def test_carrier_credential_value_is_stored() -> None:
    credential = CarrierCredential(
        carrier_account_id=uuid.uuid4(),
        credential_key="API_KEY",
        credential_value="my-secret",
    )

    assert credential.credential_value == "my-secret"


def test_carrier_credential_inherits_base_entity_fields() -> None:
    credential = CarrierCredential(
        carrier_account_id=uuid.uuid4(),
        credential_key="API_KEY",
        credential_value="secret-value",
    )

    assert hasattr(credential, "id")
    assert hasattr(credential, "created_at")
    assert hasattr(credential, "updated_at")
    assert hasattr(credential, "deleted_at")


def test_carrier_credential_deleted_at_default_is_none() -> None:
    credential = CarrierCredential(
        carrier_account_id=uuid.uuid4(),
        credential_key="API_KEY",
        credential_value="secret-value",
    )

    assert credential.deleted_at is None