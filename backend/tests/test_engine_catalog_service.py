from universal_pudo_saas.engine_catalog.client import (
    InMemoryEngineCatalogClient,
)
from universal_pudo_saas.engine_catalog.models import (
    Carrier,
    CarrierLifecycle,
)
from universal_pudo_saas.engine_catalog.service import (
    EngineCatalogService,
)


def build_service() -> EngineCatalogService:
    carriers = [
        Carrier(
            carrier_id="active",
            code="COLISSIMO",
            name="Colissimo",
            lifecycle=CarrierLifecycle.ACTIVE,
        ),
        Carrier(
            carrier_id="deprecated",
            code="MR",
            name="Mondial Relay",
            lifecycle=CarrierLifecycle.DEPRECATED,
        ),
        Carrier(
            carrier_id="sunset",
            code="CHRONOPOST",
            name="Chronopost",
            lifecycle=CarrierLifecycle.SUNSET,
        ),
        Carrier(
            carrier_id="removed",
            code="REM",
            name="Removed Carrier",
            lifecycle=CarrierLifecycle.REMOVED,
        ),
    ]

    return EngineCatalogService(
        InMemoryEngineCatalogClient(
            carriers=carriers,
        ),
    )


def test_list_all_carriers() -> None:
    service = build_service()

    result = service.list_all_carriers()

    assert len(result) == 4


def test_list_visible_carriers() -> None:
    service = build_service()

    result = service.list_visible_carriers()

    ids = {carrier.carrier_id for carrier in result}

    assert ids == {
        "active",
        "deprecated",
        "sunset",
    }


def test_list_activatable_carriers() -> None:
    service = build_service()

    result = service.list_activatable_carriers()

    ids = {carrier.carrier_id for carrier in result}

    assert ids == {
        "active",
        "deprecated",
    }


def test_get_carrier() -> None:
    service = build_service()

    result = service.get_carrier("active")

    assert result is not None
    assert result.carrier_id == "active"


def test_get_visible_carrier_returns_visible_carrier() -> None:
    service = build_service()

    result = service.get_visible_carrier("active")

    assert result is not None


def test_get_visible_carrier_returns_none_for_removed_carrier() -> None:
    service = build_service()

    result = service.get_visible_carrier("removed")

    assert result is None


def test_get_activatable_carrier_returns_carrier() -> None:
    service = build_service()

    result = service.get_activatable_carrier("active")

    assert result is not None


def test_get_activatable_carrier_returns_none_for_sunset() -> None:
    service = build_service()

    result = service.get_activatable_carrier("sunset")

    assert result is None


def test_get_activatable_carrier_returns_none_for_removed() -> None:
    service = build_service()

    result = service.get_activatable_carrier("removed")

    assert result is None