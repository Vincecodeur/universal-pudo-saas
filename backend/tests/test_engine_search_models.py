from universal_pudo_saas.engine_search.models import (
    Address,
    GeoLocation,
    PickupPoint,
    PickupType,
)


def test_create_pickup_point() -> None:
    pickup_point = PickupPoint(
        pickup_id="pickup-1",
        carrier_id="COLISSIMO",
        name="Pickup Point",
        pickup_type=PickupType.STORE,
        address=Address(
            street_line_1="1 Rue de Paris",
            postal_code="75001",
            city="Paris",
            country_code="FR",
        ),
        geolocation=GeoLocation(
            latitude=48.8566,
            longitude=2.3522,
        ),
    )

    assert pickup_point.pickup_id == "pickup-1"
    assert pickup_point.carrier_id == "COLISSIMO"
    assert pickup_point.pickup_type == PickupType.STORE
    assert pickup_point.address.city == "Paris"


def test_pickup_type_values() -> None:
    assert PickupType.STORE == "STORE"
    assert PickupType.LOCKER == "LOCKER"