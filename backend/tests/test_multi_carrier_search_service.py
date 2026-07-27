from __future__ import annotations

import uuid

from universal_pudo_saas.engine_search.models import (
    Address,
    GeoLocation,
    PickupPoint,
    PickupType,
)
from universal_pudo_saas.multi_carrier_search.service import (
    MultiCarrierSearchService,
)


class FakeOrganisationSearchService:
    def __init__(
        self,
        pickup_points: list[PickupPoint],
    ) -> None:
        self._pickup_points = pickup_points

    def search_pickup_points_for_organisation(
        self,
        *,
        organisation_id: uuid.UUID,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
        pickup_type: str | None = None,
    ) -> list[PickupPoint]:
        return self._pickup_points


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


def test_returns_empty_list() -> None:
    service = MultiCarrierSearchService(
        FakeOrganisationSearchService([]),
    )

    results = service.search_pickup_points(
        organisation_id=uuid.uuid4(),
    )

    assert results == []


def test_returns_pickup_points() -> None:
    pickup_point = build_pickup_point(
        pickup_id="pickup-1",
        carrier_id="COLISSIMO",
    )

    service = MultiCarrierSearchService(
        FakeOrganisationSearchService(
            [pickup_point],
        ),
    )

    results = service.search_pickup_points(
        organisation_id=uuid.uuid4(),
    )

    assert len(results) == 1
    assert results[0].pickup_id == "pickup-1"


def test_returns_multiple_pickup_points() -> None:
    pickup_1 = build_pickup_point(
        pickup_id="pickup-1",
        carrier_id="COLISSIMO",
    )

    pickup_2 = build_pickup_point(
        pickup_id="pickup-2",
        carrier_id="MONDIAL_RELAY",
    )

    service = MultiCarrierSearchService(
        FakeOrganisationSearchService(
            [pickup_1, pickup_2],
        ),
    )

    results = service.search_pickup_points(
        organisation_id=uuid.uuid4(),
    )

    assert len(results) == 2

    carrier_ids = {
        pickup.carrier_id
        for pickup in results
    }

    assert carrier_ids == {
        "COLISSIMO",
        "MONDIAL_RELAY",
    }