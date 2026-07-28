from __future__ import annotations

from uuid import uuid4

from universal_pudo_saas.engine_search.models import (
    Address,
    GeoLocation,
    PickupPoint,
    PickupType,
)

from universal_pudo_saas.search_platform.models import (
    SearchRequest,
)

from universal_pudo_saas.search_platform.service import (
    SearchPlatformService,
)


class FakeMultiCarrierSearchService:
    def __init__(
        self,
        pickup_points: list[PickupPoint],
    ) -> None:
        self.pickup_points = pickup_points
        self.called = False

    def search_pickup_points(
        self,
        *,
        organisation_id,
        country_code=None,
        postal_code=None,
        city=None,
        pickup_type=None,
    ):
        self.called = True

        return self.pickup_points


def build_pickup_point() -> PickupPoint:
    return PickupPoint(
        pickup_id="pickup-001",
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


def test_search_returns_search_result() -> None:
    pickup_point = build_pickup_point()

    multi_carrier_service = FakeMultiCarrierSearchService(
        pickup_points=[pickup_point],
    )

    service = SearchPlatformService(
        multi_carrier_search_service=multi_carrier_service,
    )

    request = SearchRequest(
        organisation_id=uuid4(),
        country_code="FR",
        postal_code="75001",
        carrier_codes=[
            "COLISSIMO",
        ],
    )

    result = service.search(request)

    assert len(result.pickup_points) == 1
    assert result.total_results == 1

    assert result.executed_carriers == [
        "COLISSIMO",
    ]

    assert result.failed_carriers == []

    assert result.metadata.source == "search_platform"
    assert result.metadata.duration_ms >= 0
    assert result.metadata.applied_filters == [
        "country_code",
        "postal_code",
        "carrier_codes",
    ]

    assert multi_carrier_service.called is True


def test_search_returns_empty_result() -> None:
    multi_carrier_service = FakeMultiCarrierSearchService(
        pickup_points=[],
    )

    service = SearchPlatformService(
        multi_carrier_search_service=multi_carrier_service,
    )

    request = SearchRequest(
        organisation_id=uuid4(),
    )

    result = service.search(request)

    assert result.pickup_points == []
    assert result.total_results == 0
    assert result.executed_carriers == []
    assert result.failed_carriers == []

    assert result.metadata.source == "search_platform"
    assert result.metadata.duration_ms >= 0
    assert result.metadata.applied_filters == []

    assert multi_carrier_service.called is True


def test_search_copies_executed_carriers() -> None:
    multi_carrier_service = FakeMultiCarrierSearchService(
        pickup_points=[],
    )

    service = SearchPlatformService(
        multi_carrier_search_service=multi_carrier_service,
    )

    carrier_codes = [
        "COLISSIMO",
        "MONDIAL_RELAY",
    ]

    request = SearchRequest(
        organisation_id=uuid4(),
        carrier_codes=carrier_codes,
    )

    result = service.search(request)

    carrier_codes.append("UPS")

    assert result.executed_carriers == [
        "COLISSIMO",
        "MONDIAL_RELAY",
    ]


def test_search_enriches_result_with_metadata() -> None:
    multi_carrier_service = FakeMultiCarrierSearchService(
        pickup_points=[],
    )

    service = SearchPlatformService(
        multi_carrier_search_service=multi_carrier_service,
    )

    request = SearchRequest(
        organisation_id=uuid4(),
        query="Paris",
        country_code="FR",
        postal_code="75001",
        city="Paris",
        latitude=48.8566,
        longitude=2.3522,
        radius_km=10,
        carrier_codes=[
            "COLISSIMO",
        ],
        limit=25,
    )

    result = service.search(request)

    assert result.metadata.source == "search_platform"
    assert result.metadata.duration_ms >= 0

    assert result.metadata.applied_filters == [
        "query",
        "country_code",
        "postal_code",
        "city",
        "latitude",
        "longitude",
        "radius_km",
        "carrier_codes",
        "limit",
    ]


def test_search_metadata_filters_are_independent() -> None:
    multi_carrier_service = FakeMultiCarrierSearchService(
        pickup_points=[],
    )

    service = SearchPlatformService(
        multi_carrier_search_service=multi_carrier_service,
    )

    first_request = SearchRequest(
        organisation_id=uuid4(),
        city="Paris",
    )

    second_request = SearchRequest(
        organisation_id=uuid4(),
    )

    first_result = service.search(first_request)
    second_result = service.search(second_request)

    first_result.metadata.applied_filters.append("manual")

    assert first_result.metadata.applied_filters == [
        "city",
        "manual",
    ]

    assert second_result.metadata.applied_filters == []