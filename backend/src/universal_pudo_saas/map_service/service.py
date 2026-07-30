"""Service layer for map-ready projections.

The MapService transforms SearchResult-compatible objects into UI-facing
projections without modifying the original SearchResult.

This service must remain presentation-oriented:
- no persistence
- no SQLAlchemy
- no Alembic migration
- no Universal PUDO Engine modification
"""

from __future__ import annotations

from typing import Any

from universal_pudo_saas.map_service.models import (
    MapCenter,
    MapMarker,
    MapPopup,
    MapProjectionResult,
    MapViewState,
)


class MapService:
    """Builds map-ready projections from SearchResult data."""

    def build_map_projection(
        self,
        search_result: Any,
        visible_carriers: list[str] | None = None,
        selected_pickup_point_id: str | None = None,
        carrier_branding: dict[str, dict[str, str | None]] | None = None,
    ) -> MapProjectionResult:
        """Build a complete map projection from a SearchResult-compatible object.

        Args:
            search_result: Object exposing pickup_points, executed_carriers and
                failed_carriers attributes.
            visible_carriers: Optional list of carrier codes currently visible
                to the user.
            selected_pickup_point_id: Optional selected pickup point id.
            carrier_branding: Optional mapping by carrier code.

        Returns:
            MapProjectionResult containing markers, popups and view state.
        """

        pickup_points = list(getattr(search_result, "pickup_points", []))
        visible_carriers = list(visible_carriers or [])
        carrier_branding = carrier_branding or {}

        projected_pickup_points = self._filter_visible_pickup_points(
            pickup_points=pickup_points,
            visible_carriers=visible_carriers,
        )

        markers: list[MapMarker] = []
        popups: dict[str, MapPopup] = {}

        for pickup_point in projected_pickup_points:
            carrier_code = self._extract_carrier_code(pickup_point)
            branding = carrier_branding.get(carrier_code, {})

            marker = self.create_marker_projection(
                pickup_point=pickup_point,
                branding=branding,
            )
            popup = self.create_popup_projection(pickup_point=pickup_point)

            markers.append(marker)
            popups[marker.pickup_point_id] = popup

        valid_selected_pickup_point_id = self._resolve_selected_pickup_point_id(
            selected_pickup_point_id=selected_pickup_point_id,
            markers=markers,
        )

        view_state = MapViewState(
            selected_pickup_point_id=valid_selected_pickup_point_id,
            visible_carriers=visible_carriers,
        )

        return MapProjectionResult(
            markers=markers,
            popups=popups,
            view_state=view_state,
            total_markers=len(markers),
            executed_carriers=list(getattr(search_result, "executed_carriers", [])),
            failed_carriers=list(getattr(search_result, "failed_carriers", [])),
        )

    def create_marker_projection(
        self,
        pickup_point: Any,
        branding: dict[str, str | None] | None = None,
    ) -> MapMarker:
        """Create a map marker from a pickup point-compatible object."""

        branding = branding or {}

        pickup_point_id = self._extract_pickup_point_id(pickup_point)
        carrier_code = self._extract_carrier_code(pickup_point)
        latitude, longitude = self._extract_coordinates(pickup_point)

        return MapMarker(
            pickup_point_id=pickup_point_id,
            latitude=latitude,
            longitude=longitude,
            carrier_code=carrier_code,
            carrier_display_name=branding.get("display_name") or carrier_code,
            carrier_logo_url=branding.get("logo_url"),
            carrier_color=branding.get("color"),
        )

    def create_popup_projection(self, pickup_point: Any) -> MapPopup:
        """Create marker popup information from a pickup point-compatible object."""

        pickup_point_id = self._extract_pickup_point_id(pickup_point)
        carrier_code = self._extract_carrier_code(pickup_point)

        return MapPopup(
            pickup_point_id=pickup_point_id,
            pickup_point_name=getattr(pickup_point, "name", None),
            carrier=carrier_code,
            address=self._format_address(getattr(pickup_point, "address", None)),
            distance=getattr(pickup_point, "distance", None),
            opening_hours=getattr(pickup_point, "opening_hours", None),
            details_link=getattr(pickup_point, "details_link", None),
        )

    def _filter_visible_pickup_points(
        self,
        pickup_points: list[Any],
        visible_carriers: list[str],
    ) -> list[Any]:
        if not visible_carriers:
            return pickup_points

        return [
            pickup_point
            for pickup_point in pickup_points
            if self._extract_carrier_code(pickup_point) in visible_carriers
        ]

    def _resolve_selected_pickup_point_id(
        self,
        selected_pickup_point_id: str | None,
        markers: list[MapMarker],
    ) -> str | None:
        if selected_pickup_point_id is None:
            return None

        marker_ids = {marker.pickup_point_id for marker in markers}

        if selected_pickup_point_id in marker_ids:
            return selected_pickup_point_id

        return None

    def _extract_pickup_point_id(self, pickup_point: Any) -> str:
        pickup_point_id = (
            getattr(pickup_point, "id", None)
            or getattr(pickup_point, "pickup_point_id", None)
            or getattr(pickup_point, "code", None)
        )

        if pickup_point_id is None:
            raise ValueError("Pickup point id is required for map projection.")

        return str(pickup_point_id)

    def _extract_carrier_code(self, pickup_point: Any) -> str:
        carrier_code = (
            getattr(pickup_point, "carrier_code", None)
            or getattr(pickup_point, "carrier", None)
        )

        if carrier_code is None:
            raise ValueError("Carrier code is required for map projection.")

        return str(carrier_code)

    def _extract_coordinates(self, pickup_point: Any) -> tuple[float, float]:
        location = (
            getattr(pickup_point, "location", None)
            or getattr(pickup_point, "geo_location", None)
            or getattr(pickup_point, "geolocation", None)
        )

        latitude = (
            getattr(location, "latitude", None)
            if location is not None
            else getattr(pickup_point, "latitude", None)
        )
        longitude = (
            getattr(location, "longitude", None)
            if location is not None
            else getattr(pickup_point, "longitude", None)
        )

        if latitude is None or longitude is None:
            raise ValueError("Latitude and longitude are required for map projection.")

        return float(latitude), float(longitude)

    def _format_address(self, address: Any) -> str | None:
        if address is None:
            return None

        if isinstance(address, str):
            return address

        address_parts = [
            getattr(address, "line1", None),
            getattr(address, "street", None),
            getattr(address, "postal_code", None),
            getattr(address, "city", None),
            getattr(address, "country", None),
        ]

        cleaned_parts = [str(part) for part in address_parts if part]

        if not cleaned_parts:
            return None

        return ", ".join(cleaned_parts)