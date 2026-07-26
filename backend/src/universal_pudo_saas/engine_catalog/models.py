from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class CarrierCapability(StrEnum):
    """
    Capabilities exposed by Universal PUDO Engine carriers.

    These values mirror the current Engine v1.0.0 public model.
    """

    SEARCH_PICKUP_POINTS = "SEARCH_PICKUP_POINTS"
    GET_PICKUP_DETAILS = "GET_PICKUP_DETAILS"
    RESOLVE_PICKUP_POINT = "RESOLVE_PICKUP_POINT"


class CarrierLifecycle(StrEnum):
    """
    Lifecycle states exposed by Universal PUDO Engine carriers.

    The SaaS consumes these values but does not own their meaning.
    """

    ACTIVE = "ACTIVE"
    DEPRECATED = "DEPRECATED"
    UNLISTED = "UNLISTED"
    SUNSET = "SUNSET"
    REMOVED = "REMOVED"


@dataclass(slots=True)
class Carrier:
    """
    SaaS read model representing a carrier exposed by Universal PUDO Engine.

    This is not a SQLAlchemy model.

    The Engine remains the source of truth.
    The SaaS only consumes this projection.
    """

    carrier_id: str
    code: str
    name: str
    lifecycle: CarrierLifecycle = CarrierLifecycle.ACTIVE
    supported_countries: list[str] = field(
        default_factory=list,
    )
    capabilities: list[CarrierCapability] = field(
        default_factory=list,
    )

    def is_visible(self) -> bool:
        return self.lifecycle in {
            CarrierLifecycle.ACTIVE,
            CarrierLifecycle.DEPRECATED,
            CarrierLifecycle.SUNSET,
        }

    def is_activatable(self) -> bool:
        return self.lifecycle in {
            CarrierLifecycle.ACTIVE,
            CarrierLifecycle.DEPRECATED,
        }