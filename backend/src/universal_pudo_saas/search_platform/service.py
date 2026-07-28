from __future__ import annotations

from time import perf_counter

from universal_pudo_saas.multi_carrier_search.service import (
    MultiCarrierSearchService,
)

from .models import (
    SearchExecutionMetadata,
    SearchRequest,
    SearchResult,
)


class SearchPlatformService:
    """
    SaaS Search Platform boundary.

    Responsibilities:

    - Accept SearchRequest
    - Delegate execution to MultiCarrierSearchService
    - Build SearchResult
    - Enrich SearchResult with execution metadata

    Non-responsibilities:

    - Persistence
    - Ranking
    - Export
    - Engine modifications
    """

    def __init__(
        self,
        multi_carrier_search_service: MultiCarrierSearchService,
    ) -> None:
        self._multi_carrier_search_service = (
            multi_carrier_search_service
        )

    def search(
        self,
        request: SearchRequest,
    ) -> SearchResult:
        started_at = perf_counter()

        pickup_points = (
            self._multi_carrier_search_service
            .search_pickup_points(
                organisation_id=request.organisation_id,
                country_code=request.country_code,
                postal_code=request.postal_code,
                city=request.city,
            )
        )

        duration_ms = int(
            (perf_counter() - started_at) * 1000,
        )

        return SearchResult(
            pickup_points=pickup_points,
            total_results=len(pickup_points),
            executed_carriers=request.carrier_codes.copy(),
            failed_carriers=[],
            metadata=SearchExecutionMetadata(
                duration_ms=duration_ms,
                applied_filters=self._extract_applied_filters(
                    request=request,
                ),
            ),
        )

    def _extract_applied_filters(
        self,
        *,
        request: SearchRequest,
    ) -> list[str]:
        applied_filters: list[str] = []

        if request.query is not None:
            applied_filters.append("query")

        if request.country_code is not None:
            applied_filters.append("country_code")

        if request.postal_code is not None:
            applied_filters.append("postal_code")

        if request.city is not None:
            applied_filters.append("city")

        if request.latitude is not None:
            applied_filters.append("latitude")

        if request.longitude is not None:
            applied_filters.append("longitude")

        if request.radius_km is not None:
            applied_filters.append("radius_km")

        if request.carrier_codes:
            applied_filters.append("carrier_codes")

        if request.limit != 100:
            applied_filters.append("limit")

        return applied_filters