"""Map service presentation layer.

This package contains presentation-oriented structures and services used to
transform SearchResult data into map-ready projections.

The map service must not introduce persistence, SQLAlchemy models, Alembic
migrations, or Universal PUDO Engine modifications.
"""

from universal_pudo_saas.map_service.models import (
    MapCenter,
    MapMarker,
    MapPopup,
    MapProjectionResult,
    MapViewState,
)
from universal_pudo_saas.map_service.service import MapService

__all__ = [
    "MapCenter",
    "MapMarker",
    "MapPopup",
    "MapProjectionResult",
    "MapService",
    "MapViewState",
]