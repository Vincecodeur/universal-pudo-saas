from __future__ import annotations

import uuid

from universal_pudo_saas.engine_catalog.models import (
    Carrier,
)
from universal_pudo_saas.engine_search.models import (
    Address,
    GeoLocation,
    PickupPoint,
    PickupType,
)
from universal_pudo_saas.organisation_search.service import (
    OrganisationSearchService,
)


class FakeCarrierCatalogService:
    def __init__(
        self,
        carriers: list[Carrier],
    ) -> None:
        self._carriers = carriers

    def list_organisation_carriers(
        self,
        organisation_id: uuid.UUID,
    ) -> list[Carrier]:
        return self._carriers


class FakeEngineSearchService:
    def __init__(
        self,
        results_by_carrier: dict[str, list[PickupPoint]],
    ) -> None:
        self._results_by_carrier = results_by_carrier

    def search_pickup_points(
        self,
        *,
        carrier_id: str | None = None,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
        pickup_type: str | None = None,
    ) -> list[PickupPoint]:
        return self._results_by_carrier.get(
            carrier_id or "",
            [],
        )


def build_pickup_point(
    *,
    pickup_id: str,
    carrier_id: str,
) -> PickupPoint:
    return PickupPoint(
        pickup_id=pickup_id,
        carrier_id=carrier_id,
        name=f"Pickup {pickup_id}",
        pickup_type=PickupType.STORE,
        address=Address(
            street_line_1="1 Main Street",
            postal_code="75001",
            city="Paris",
            country_code="FR",
        ),
        geolocation=GeoLocation(
            latitude=48.8566,
            longitude=2.3522,
        ),
    )


def test_returns_empty_list_when_no_carrier_is_connected() -> None:
    service = OrganisationSearchService(
        carrier_catalog_service=FakeCarrierCatalogService(
            carriers=[],
        ),
        engine_search_service=FakeEngineSearchService(
            results_by_carrier={},
        ),
    )

    results = service.search_pickup_points_for_organisation(
        organisation_id=uuid.uuid4(),
        postal_code="75001",
    )

    assert results == []


def test_returns_pickup_points_for_single_carrier() -> None:
    carrier = Carrier(
        carrier_id="carrier-1",
        code="COLISSIMO",
        name="Colissimo",
    )

    pickup_point = build_pickup_point(
        pickup_id="pickup-1",
        carrier_id="COLISSIMO",
    )

    service = OrganisationSearchService(
        carrier_catalog_service=FakeCarrierCatalogService(
            carriers=[carrier],
        ),
        engine_search_service=FakeEngineSearchService(
            results_by_carrier={
                "COLISSIMO": [pickup_point],
            },
        ),
    )

    results = service.search_pickup_points_for_organisation(
        organisation_id=uuid.uuid4(),
        postal_code="75001",
    )

    assert len(results) == 1
    assert results[0].pickup_id == "pickup-1"
    assert results[0].carrier_id == "COLISSIMO"


def test_aggregates_pickup_points_from_multiple_carriers() -> None:
    carrier_1 = Carrier(
        carrier_id="carrier-1",
        code="COLISSIMO",
        name="Colissimo",
    )

    carrier_2 = Carrier(
        carrier_id="carrier-2",
        code="MONDIAL_RELAY",
        name="Mondial Relay",
    )

    pickup_point_1 = build_pickup_point(
        pickup_id="pickup-1",
        carrier_id="COLISSIMO",
    )

    pickup_point_2 = build_pickup_point(
        pickup_id="pickup-2",
        carrier_id="MONDIAL_RELAY",
    )

    service = OrganisationSearchService(
        carrier_catalog_service=FakeCarrierCatalogService(
            carriers=[
                carrier_1,
                carrier_2,
            ],
        ),
        engine_search_service=FakeEngineSearchService(
            results_by_carrier={
                "COLISSIMO": [pickup_point_1],
                "MONDIAL_RELAY": [pickup_point_2],
            },
        ),
    )

    results = service.search_pickup_points_for_organisation(
        organisation_id=uuid.uuid4(),
        postal_code="75001",
    )

    assert len(results) == 2

    carrier_ids = {
        pickup_point.carrier_id
        for pickup_point in results
    }

    assert carrier_ids == {
        "COLISSIMO",
        "MONDIAL_RELAY",
    }