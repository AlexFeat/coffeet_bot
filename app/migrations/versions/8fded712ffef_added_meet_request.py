"""added meet.request

Revision ID: 8fded712ffef
Revises: 86cd72995698
Create Date: 2021-05-14 18:21:09.851283

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8fded712ffef'
down_revision = '86cd72995698'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'requests',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('ts_create', sa.DateTime(), server_default='now()', nullable=False),
        sa.Column('user_id', sa.BigInteger(), nullable=True, comment='Идентификатор пользователя оставившего заявку'),
        sa.Column('date_meet', sa.Date(), nullable=False, comment='Дата проведения встречи'),
        sa.Column('meet_from', sa.Time(), nullable=False,
                  comment='Встреча должна начаться не раньше указанного времени'),
        sa.Column('meet_to', sa.Time(), nullable=False,
                  comment='Встреча должна закнчиться не позже указанного времени'),
        sa.Column('date_expire', sa.Date(), nullable=False, comment='Дата истечения срока актуальности заявки'),
        sa.ForeignKeyConstraint(['user_id'], ['user.items.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='meet'
    )


def downgrade():
    op.drop_table('requests', schema='meet')
