from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class PickupType(StrEnum):
    """
    Pickup point types exposed
    by Universal PUDO Engine.
    """

    STORE = "STORE"
    LOCKER = "LOCKER"


@dataclass(slots=True)
class Address:
    """
    SaaS projection of an Engine address.
    """

    street_line_1: str
    street_line_2: str | None = None

    postal_code: str = ""
    city: str = ""

    state_or_region: str | None = None

    country_code: str = ""

    formatted_address: str | None = None


@dataclass(slots=True)
class GeoLocation:
    """
    SaaS projection of Engine coordinates.
    """

    latitude: float
    longitude: float


@dataclass(slots=True)
class PickupPoint:
    """
    SaaS read model representing
    a pickup point exposed by Engine.

    This is not a SQLAlchemy model.
    """

    pickup_id: str
    carrier_id: str

    name: str

    pickup_type: PickupType

    address: Address
    geolocation: GeoLocation

    active: bool = True

    opening_hours: str | None = None

    phone_number: str | None = None
    email: str | None = None

    services: list[str] | None = None