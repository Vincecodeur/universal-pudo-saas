from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

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
class SearchExecutionMetadata:
    """
    SaaS search execution metadata DTO.

    This object enriches a SearchResult with execution context.
    It is not persisted.
    """

    search_id: UUID = field(default_factory=uuid4)

    executed_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
    )

    duration_ms: int = 0

    source: str = "search_platform"

    applied_filters: list[str] = field(default_factory=list)


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

    metadata: SearchExecutionMetadata = field(
        default_factory=SearchExecutionMetadata,
    )