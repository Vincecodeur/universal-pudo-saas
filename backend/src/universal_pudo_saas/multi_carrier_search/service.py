from __future__ import annotations

import uuid

from universal_pudo_saas.engine_search.models import (
    PickupPoint,
)
from universal_pudo_saas.organisation_search.service import (
    OrganisationSearchService,
)


class MultiCarrierSearchService:
    def __init__(
        self,
        organisation_search_service: OrganisationSearchService,
    ) -> None:
        self._organisation_search_service = (
            organisation_search_service
        )

    def search_pickup_points(
        self,
        *,
        organisation_id: uuid.UUID,
        country_code: str | None = None,
        postal_code: str | None = None,
        city: str | None = None,
        pickup_type: str | None = None,
    ) -> list[PickupPoint]:
        return (
            self._organisation_search_service
            .search_pickup_points_for_organisation(
                organisation_id=organisation_id,
                country_code=country_code,
                postal_code=postal_code,
                city=city,
                pickup_type=pickup_type,
            )
        )