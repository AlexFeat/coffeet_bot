"""added is_active for user.items

Revision ID: 86cd72995698
Revises: 7730f89fa128
Create Date: 2021-05-05 17:14:47.274348

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '86cd72995698'
down_revision = '7730f89fa128'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'items',
        sa.Column('is_active', sa.Boolean(), server_default='true', nullable=False),
        schema='user'
    )


def downgrade():
    op.drop_column(
        'items',
        'is_active',
        schema='user'
    )
