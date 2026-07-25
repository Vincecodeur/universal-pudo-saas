from __future__ import annotations

import uuid

from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from universal_pudo_saas.shared.entities import BaseEntity


class CarrierAccount(BaseEntity):
    __tablename__ = "carrier_accounts"

    organisation_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("organisations.id"),
        nullable=False,
    )

    carrier_code: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )