import uuid

from universal_pudo_saas.carrier_accounts.models import CarrierAccount


def test_carrier_account_creation() -> None:
    organisation_id = uuid.uuid4()

    carrier_account = CarrierAccount(
        organisation_id=organisation_id,
        carrier_code="mondialrelay",
        name="Mondial Relay Production",
    )

    assert carrier_account.organisation_id == organisation_id


def test_carrier_account_name_is_stored() -> None:
    carrier_account = CarrierAccount(
        organisation_id=uuid.uuid4(),
        carrier_code="mondialrelay",
        name="Mondial Relay Production",
    )

    assert carrier_account.name == "Mondial Relay Production"


def test_carrier_account_carrier_code_is_stored() -> None:
    carrier_account = CarrierAccount(
        organisation_id=uuid.uuid4(),
        carrier_code="mondialrelay",
        name="Mondial Relay Production",
    )

    assert carrier_account.carrier_code == "mondialrelay"


def test_carrier_account_is_active_field_is_available() -> None:
    carrier_account = CarrierAccount(
        organisation_id=uuid.uuid4(),
        carrier_code="mondialrelay",
        name="Mondial Relay Production",
    )

    assert hasattr(carrier_account, "is_active")


def test_carrier_account_inherits_base_entity_fields() -> None:
    carrier_account = CarrierAccount(
        organisation_id=uuid.uuid4(),
        carrier_code="mondialrelay",
        name="Mondial Relay Production",
    )

    assert hasattr(carrier_account, "id")
    assert hasattr(carrier_account, "created_at")
    assert hasattr(carrier_account, "updated_at")
    assert hasattr(carrier_account, "deleted_at")


def test_carrier_account_deleted_at_default_is_none() -> None:
    carrier_account = CarrierAccount(
        organisation_id=uuid.uuid4(),
        carrier_code="mondialrelay",
        name="Mondial Relay Production",
    )

    assert carrier_account.deleted_at is None