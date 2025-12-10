"""add content column to posts table

Revision ID: e805141f7f68
Revises: e248302be6d0
Create Date: 2025-12-10 23:52:34.746768

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e805141f7f68'
down_revision: Union[str, Sequence[str], None] = 'e248302be6d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
