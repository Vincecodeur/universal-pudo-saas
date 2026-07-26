from __future__ import annotations

from universal_pudo_saas.engine_catalog.client import (
    EngineCatalogClient,
)
from universal_pudo_saas.engine_catalog.models import (
    Carrier,
)


class EngineCatalogService:
    def __init__(
        self,
        client: EngineCatalogClient,
    ) -> None:
        self._client = client

    def list_all_carriers(
        self,
    ) -> list[Carrier]:
        return self._client.list_carriers()

    def list_visible_carriers(
        self,
    ) -> list[Carrier]:
        return [
            carrier
            for carrier in self._client.list_carriers()
            if carrier.is_visible()
        ]

    def list_activatable_carriers(
        self,
    ) -> list[Carrier]:
        return [
            carrier
            for carrier in self._client.list_carriers()
            if carrier.is_activatable()
        ]

    def get_carrier(
        self,
        carrier_id: str,
    ) -> Carrier | None:
        return self._client.get_carrier(carrier_id)

    def get_visible_carrier(
        self,
        carrier_id: str,
    ) -> Carrier | None:
        carrier = self.get_carrier(carrier_id)

        if carrier is None:
            return None

        if not carrier.is_visible():
            return None

        return carrier

    def get_activatable_carrier(
        self,
        carrier_id: str,
    ) -> Carrier | None:
        carrier = self.get_carrier(carrier_id)

        if carrier is None:
            return None

        if not carrier.is_activatable():
            return None

        return carrier