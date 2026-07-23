from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from universal_pudo_saas.shared.entities import BaseEntity


class Organisation(BaseEntity):
    __tablename__ = "organisations"

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

