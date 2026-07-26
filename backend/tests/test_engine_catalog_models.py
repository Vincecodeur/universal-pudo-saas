from universal_pudo_saas.engine_catalog.models import (
    Carrier,
    CarrierCapability,
    CarrierLifecycle,
)


def test_active_carrier_is_visible_and_activatable() -> None:
    carrier = Carrier(
        carrier_id="carrier-1",
        code="COLISSIMO",
        name="Colissimo",
        lifecycle=CarrierLifecycle.ACTIVE,
    )

    assert carrier.is_visible() is True
    assert carrier.is_activatable() is True


def test_deprecated_carrier_is_visible_and_activatable() -> None:
    carrier = Carrier(
        carrier_id="carrier-1",
        code="COLISSIMO",
        name="Colissimo",
        lifecycle=CarrierLifecycle.DEPRECATED,
    )

    assert carrier.is_visible() is True
    assert carrier.is_activatable() is True


def test_sunset_carrier_is_visible_but_not_activatable() -> None:
    carrier = Carrier(
        carrier_id="carrier-1",
        code="COLISSIMO",
        name="Colissimo",
        lifecycle=CarrierLifecycle.SUNSET,
    )

    assert carrier.is_visible() is True
    assert carrier.is_activatable() is False


def test_unlisted_carrier_is_not_visible() -> None:
    carrier = Carrier(
        carrier_id="carrier-1",
        code="COLISSIMO",
        name="Colissimo",
        lifecycle=CarrierLifecycle.UNLISTED,
    )

    assert carrier.is_visible() is False
    assert carrier.is_activatable() is False


def test_removed_carrier_is_not_visible_and_not_activatable() -> None:
    carrier = Carrier(
        carrier_id="carrier-1",
        code="COLISSIMO",
        name="Colissimo",
        lifecycle=CarrierLifecycle.REMOVED,
    )

    assert carrier.is_visible() is False
    assert carrier.is_activatable() is False


def test_carrier_default_values() -> None:
    carrier = Carrier(
        carrier_id="carrier-1",
        code="COLISSIMO",
        name="Colissimo",
    )

    assert carrier.supported_countries == []
    assert carrier.capabilities == []


def test_carrier_capabilities_are_stored() -> None:
    carrier = Carrier(
        carrier_id="carrier-1",
        code="COLISSIMO",
        name="Colissimo",
        capabilities=[
            CarrierCapability.SEARCH_PICKUP_POINTS,
        ],
    )

    assert carrier.capabilities == [
        CarrierCapability.SEARCH_PICKUP_POINTS,
    ]