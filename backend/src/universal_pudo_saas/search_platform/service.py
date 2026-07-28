from __future__ import annotations

from universal_pudo_saas.multi_carrier_search.service import (
    MultiCarrierSearchService,
)

from .models import (
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

    Non-responsibilities:

    - Persistence
    - Ranking
    - Enrichment
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
        pickup_points = (
            self._multi_carrier_search_service
            .search_pickup_points(
                organisation_id=request.organisation_id,
                country_code=request.country_code,
                postal_code=request.postal_code,
                city=request.city,
            )
        )

        return SearchResult(
            pickup_points=pickup_points,
            total_results=len(pickup_points),
            executed_carriers=request.carrier_codes.copy(),
            failed_carriers=[],
        )