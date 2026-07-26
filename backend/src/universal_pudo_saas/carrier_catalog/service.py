from __future__ import annotations

import uuid

from universal_pudo_saas.carrier_accounts.repository import (
    list_carrier_accounts_by_organisation,
)
from universal_pudo_saas.engine_catalog.models import (
    Carrier,
)
from universal_pudo_saas.engine_catalog.service import (
    EngineCatalogService,
)


class CarrierCatalogService:
    def __init__(
        self,
        engine_catalog_service: EngineCatalogService,
    ) -> None:
        self._engine_catalog_service = engine_catalog_service

    def list_available_carriers(
        self,
    ) -> list[Carrier]:
        return self._engine_catalog_service.list_visible_carriers()

    def list_organisation_carriers(
        self,
        organisation_id: uuid.UUID,
    ) -> list[Carrier]:
        carrier_accounts = list_carrier_accounts_by_organisation(
            organisation_id,
        )

        carrier_codes = {
            carrier_account.carrier_code
            for carrier_account in carrier_accounts
        }

        return [
            carrier
            for carrier in self._engine_catalog_service.list_visible_carriers()
            if carrier.code in carrier_codes
        ]

    def list_activatable_carriers_for_organisation(
        self,
        organisation_id: uuid.UUID,
    ) -> list[Carrier]:
        carrier_accounts = list_carrier_accounts_by_organisation(
            organisation_id,
        )

        existing_carrier_codes = {
            carrier_account.carrier_code
            for carrier_account in carrier_accounts
        }

        return [
            carrier
            for carrier in self._engine_catalog_service.list_activatable_carriers()
            if carrier.code not in existing_carrier_codes
        ]