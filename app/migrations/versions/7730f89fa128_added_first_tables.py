"""Added first tables

Revision ID: 7730f89fa128
Revises: 
Create Date: 2021-05-05 14:22:29.717510

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7730f89fa128'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE SCHEMA "user"')
    op.execute('CREATE SCHEMA "meet"')
    op.create_table(
        'items',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=False),
        sa.Column('last_name', sa.String(), nullable=False),
        sa.Column('date_birthday', sa.Date(), nullable=True),
        sa.Column('telegram_id', sa.BigInteger(), nullable=False),
        sa.Column('moderated_status', sa.SmallInteger(), server_default='0', nullable=False),
        sa.Column('ts_create', sa.DateTime(), server_default='now()', nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('telegram_id'),
        schema='user'
    )
    op.create_table(
        'items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('ts_create', sa.DateTime(), server_default='now()', nullable=False),
        sa.Column('first_user_id', sa.Integer(), nullable=True),
        sa.Column('second_user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['first_user_id'], ['user.items.id'], ),
        sa.ForeignKeyConstraint(['second_user_id'], ['user.items.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='meet'
    )
    op.create_table(
        'ratings',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('meet_id', sa.Integer(), nullable=False),
        sa.Column('author_id', sa.Integer(), nullable=True),
        sa.Column('ts_create', sa.DateTime(), server_default='now()', nullable=False),
        sa.Column('rating', sa.SmallInteger(), server_default='5', nullable=False),
        sa.Column('comment', sa.String(), server_default='', nullable=True),
        sa.ForeignKeyConstraint(['author_id'], ['user.items.id'], ),
        sa.ForeignKeyConstraint(['meet_id'], ['meet.items.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.items.id'], ),
        sa.PrimaryKeyConstraint('user_id', 'meet_id', name='rating_pk'),
        schema='user'
    )


def downgrade():
    op.drop_table('ratings', schema='user')
    op.drop_table('items', schema='meet')
    op.drop_table('items', schema='user')
    op.execute('DROP SCHEMA "user"')
    op.execute('DROP SCHEMA "meet"')
