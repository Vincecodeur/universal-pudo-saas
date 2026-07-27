from __future__ import annotations

from universal_pudo_saas.engine_search.client import (
    EngineSearchClient,
)
from universal_pudo_saas.engine_search.models import (
    PickupPoint,
)


class EngineSearchService:
    def __init__(
        self,
        client: EngineSearchClient,
    ) -> None:
        self._client = client

    def search_pickup_points(
        self,
        *,
        carrier_id: str | None = None,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
        pickup_type: str | None = None,
    ) -> list[PickupPoint]:
        return self._client.search_pickup_points(
            carrier_id=carrier_id,
            country_code=country_code,
            postal_code=postal_code,
            city=city,
            pickup_type=pickup_type,
        )

    def search_pickup_points_by_radius(
        self,
        *,
        latitude: float,
        longitude: float,
        radius_km: float,
    ) -> list[PickupPoint]:
        return self._client.search_pickup_points_by_radius(
            latitude=latitude,
            longitude=longitude,
            radius_km=radius_km,
        )

    def get_pickup_point(
        self,
        pickup_id: str,
    ) -> PickupPoint | None:
        return self._client.get_pickup_point(
            pickup_id,
        )

    def list_carrier_pickup_points(
        self,
        carrier_id: str,
    ) -> list[PickupPoint]:
        return self._client.list_carrier_pickup_points(
            carrier_id,
        )