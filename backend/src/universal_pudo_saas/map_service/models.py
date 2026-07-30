"""Presentation models for the Map Experience.

These models are UI-facing projections.

They intentionally do not replace SearchResult, PickupPoint, or any Engine
model. They are not persisted and must not be mapped with SQLAlchemy.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class MapCenter:
    """Represents a map coordinate used by the presentation layer."""

    latitude: float
    longitude: float


@dataclass
class MapViewState:
    """Represents UI state for the map.

    This is not business data and must not be persisted.
    """

    map_center: MapCenter | None = None
    map_zoom: int | None = None
    user_location: MapCenter | None = None
    selected_pickup_point_id: str | None = None
    visible_carriers: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class MapMarker:
    """Represents a marker displayed on the map.

    A marker is derived from an existing pickup point included in SearchResult.
    """

    pickup_point_id: str
    latitude: float
    longitude: float
    carrier_code: str
    carrier_display_name: str | None = None
    carrier_logo_url: str | None = None
    carrier_color: str | None = None


@dataclass(frozen=True)
class MapPopup:
    """Represents marker popup information displayed to the user."""

    pickup_point_id: str
    pickup_point_name: str | None = None
    carrier: str | None = None
    address: str | None = None
    distance: float | None = None
    opening_hours: Any | None = None
    details_link: str | None = None


@dataclass
class MapProjectionResult:
    """Represents map-ready presentation data.

    This is a projection result for the UI. It is not a search business
    contract and must not replace SearchResult.
    """

    markers: list[MapMarker] = field(default_factory=list)
    popups: dict[str, MapPopup] = field(default_factory=dict)
    view_state: MapViewState = field(default_factory=MapViewState)
    total_markers: int = 0
    executed_carriers: list[str] = field(default_factory=list)
    failed_carriers: list[str] = field(default_factory=list)