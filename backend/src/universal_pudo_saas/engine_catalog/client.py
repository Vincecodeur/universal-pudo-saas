from __future__ import annotations

from typing import Protocol

from universal_pudo_saas.engine_catalog.models import (
    Carrier,
)


class EngineCatalogClient(Protocol):
    """
    Contract used by the SaaS to consume the Engine carrier catalogue.
    """

    def list_carriers(
        self,
    ) -> list[Carrier]:
        ...

    def get_carrier(
        self,
        carrier_id: str,
    ) -> Carrier | None:
        ...


class InMemoryEngineCatalogClient:
    """
    In-memory implementation used by tests and local development.
    """

    def __init__(
        self,
        carriers: list[Carrier] | None = None,
    ) -> None:
        self._carriers = carriers or []

    def list_carriers(
        self,
    ) -> list[Carrier]:
        return list(self._carriers)

    def get_carrier(
        self,
        carrier_id: str,
    ) -> Carrier | None:
        for carrier in self._carriers:
            if carrier.carrier_id == carrier_id:
                return carrier

        return None