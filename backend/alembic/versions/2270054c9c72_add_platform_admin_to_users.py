"""add_platform_admin_to_users

Revision ID: 2270054c9c72
Revises: 2871e90d88b8
Create Date: 2026-07-25 22:07:24.743044

"""
from typing import Sequence
from typing import Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2270054c9c72"
down_revision: Union[str, Sequence[str], None] = "2871e90d88b8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "is_platform_admin",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
        ),
    )

    op.alter_column(
        "users",
        "is_platform_admin",
        server_default=None,
    )


def downgrade() -> None:
    op.drop_column(
        "users",
        "is_platform_admin",
    )