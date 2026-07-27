from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from universal_pudo_saas.engine_search.models import PickupPoint


@dataclass(slots=True)
class SearchRequest:
    """
    SaaS search request DTO.

    This object represents a search intention.
    It is not persisted.
    """

    organisation_id: UUID

    query: str | None = None

    country_code: str | None = None
    postal_code: str | None = None
    city: str | None = None

    latitude: float | None = None
    longitude: float | None = None

    radius_km: int | None = None

    carrier_codes: list[str] = field(default_factory=list)

    limit: int = 100


@dataclass(slots=True)
class SearchResult:
    """
    SaaS search result DTO.

    This object represents a consolidated search response.
    It is not persisted.
    """

    pickup_points: list[PickupPoint]

    total_results: int

    executed_carriers: list[str] = field(default_factory=list)

    failed_carriers: list[str] = field(default_factory=list)