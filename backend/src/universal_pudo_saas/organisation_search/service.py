from __future__ import annotations

import uuid

from universal_pudo_saas.carrier_catalog.service import (
    CarrierCatalogService,
)
from universal_pudo_saas.engine_search.models import (
    PickupPoint,
)
from universal_pudo_saas.engine_search.service import (
    EngineSearchService,
)


class OrganisationSearchService:
    def __init__(
        self,
        carrier_catalog_service: CarrierCatalogService,
        engine_search_service: EngineSearchService,
    ) -> None:
        self._carrier_catalog_service = carrier_catalog_service
        self._engine_search_service = engine_search_service

    def search_pickup_points_for_organisation(
        self,
        *,
        organisation_id: uuid.UUID,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
        pickup_type: str | None = None,
    ) -> list[PickupPoint]:
        carriers = (
            self._carrier_catalog_service
            .list_organisation_carriers(
                organisation_id,
            )
        )

        pickup_points: list[PickupPoint] = []

        for carrier in carriers:
            pickup_points.extend(
                self._engine_search_service.search_pickup_points(
                    carrier_id=carrier.code,
                    country_code=country_code,
                    postal_code=postal_code,
                    city=city,
                    pickup_type=pickup_type,
                )
            )

        return pickup_points