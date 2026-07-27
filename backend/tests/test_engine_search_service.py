from universal_pudo_saas.engine_search.client import (
    InMemoryEngineSearchClient,
)
from universal_pudo_saas.engine_search.models import (
    Address,
    GeoLocation,
    PickupPoint,
    PickupType,
)
from universal_pudo_saas.engine_search.service import (
    EngineSearchService,
)


def build_service() -> EngineSearchService:
    pickup_points = [
        PickupPoint(
            pickup_id="pickup-1",
            carrier_id="COLISSIMO",
            name="Paris Store",
            pickup_type=PickupType.STORE,
            address=Address(
                street_line_1="1 Rue Paris",
                postal_code="75001",
                city="Paris",
                country_code="FR",
            ),
            geolocation=GeoLocation(
                latitude=48.8566,
                longitude=2.3522,
            ),
        ),
        PickupPoint(
            pickup_id="pickup-2",
            carrier_id="MR",
            name="Lyon Locker",
            pickup_type=PickupType.LOCKER,
            address=Address(
                street_line_1="1 Rue Lyon",
                postal_code="69001",
                city="Lyon",
                country_code="FR",
            ),
            geolocation=GeoLocation(
                latitude=45.7640,
                longitude=4.8357,
            ),
        ),
    ]

    return EngineSearchService(
        InMemoryEngineSearchClient(
            pickup_points=pickup_points,
        ),
    )


def test_search_pickup_points() -> None:
    service = build_service()

    results = service.search_pickup_points(
        carrier_id="COLISSIMO",
    )

    assert len(results) == 1


def test_get_pickup_point() -> None:
    service = build_service()

    result = service.get_pickup_point(
        "pickup-1",
    )

    assert result is not None


def test_get_pickup_point_returns_none() -> None:
    service = build_service()

    result = service.get_pickup_point(
        "unknown",
    )

    assert result is None


def test_list_carrier_pickup_points() -> None:
    service = build_service()

    results = service.list_carrier_pickup_points(
        "MR",
    )

    assert len(results) == 1


def test_search_pickup_points_by_radius() -> None:
    service = build_service()

    results = service.search_pickup_points_by_radius(
        latitude=48.8566,
        longitude=2.3522,
        radius_km=10,
    )

    assert len(results) == 2