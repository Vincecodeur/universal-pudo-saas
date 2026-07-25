from __future__ import annotations

import uuid

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from universal_pudo_saas.shared.entities import BaseEntity


class CarrierCredential(BaseEntity):
    __tablename__ = "carrier_credentials"

    carrier_account_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("carrier_accounts.id"),
        nullable=False,
    )

    credential_key: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    credential_value: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )