from __future__ import annotations

from typing import Protocol

from universal_pudo_saas.engine_search.models import (
    PickupPoint,
)


class EngineSearchClient(Protocol):
    """
    Contract used by the SaaS to consume
    Engine pickup point search capabilities.
    """

    def search_pickup_points(
        self,
        *,
        carrier_id: str | None = None,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
        pickup_type: str | None = None,
    ) -> list[PickupPoint]:
        ...

    def search_pickup_points_by_radius(
        self,
        *,
        latitude: float,
        longitude: float,
        radius_km: float,
    ) -> list[PickupPoint]:
        ...

    def get_pickup_point(
        self,
        pickup_id: str,
    ) -> PickupPoint | None:
        ...

    def list_carrier_pickup_points(
        self,
        carrier_id: str,
    ) -> list[PickupPoint]:
        ...


class InMemoryEngineSearchClient:
    """
    In-memory implementation used
    by tests and local development.
    """

    def __init__(
        self,
        pickup_points: list[PickupPoint] | None = None,
    ) -> None:
        self._pickup_points = pickup_points or []

    def search_pickup_points(
        self,
        *,
        carrier_id: str | None = None,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
        pickup_type: str | None = None,
    ) -> list[PickupPoint]:
        results = list(self._pickup_points)

        if carrier_id is not None:
            results = [
                point
                for point in results
                if point.carrier_id == carrier_id
            ]

        if country_code is not None:
            results = [
                point
                for point in results
                if point.address.country_code
                == country_code
            ]

        if postal_code is not None:
            results = [
                point
                for point in results
                if point.address.postal_code
                == postal_code
            ]

        if city is not None:
            results = [
                point
                for point in results
                if point.address.city == city
            ]

        if pickup_type is not None:
            results = [
                point
                for point in results
                if point.pickup_type.value
                == pickup_type
            ]

        return results

    def search_pickup_points_by_radius(
        self,
        *,
        latitude: float,
        longitude: float,
        radius_km: float,
    ) -> list[PickupPoint]:
        return list(self._pickup_points)

    def get_pickup_point(
        self,
        pickup_id: str,
    ) -> PickupPoint | None:
        for pickup_point in self._pickup_points:
            if pickup_point.pickup_id == pickup_id:
                return pickup_point

        return None

    def list_carrier_pickup_points(
        self,
        carrier_id: str,
    ) -> list[PickupPoint]:
        return [
            pickup_point
            for pickup_point in self._pickup_points
            if pickup_point.carrier_id == carrier_id
        ]