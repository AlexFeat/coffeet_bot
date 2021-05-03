"""first migration

Revision ID: 76b9e5f7e8ab
Revises: 
Create Date: 2021-05-03 18:58:54.285270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76b9e5f7e8ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE SCHEMA "user"')
    op.execute('CREATE SCHEMA "meet"')
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('date_birthday', sa.Date(), nullable=True),
    sa.Column('telegram_id', sa.String(), nullable=False),
    sa.Column('moderated_status', sa.SmallInteger(), server_default='0', nullable=False),
    sa.Column('ts_create', sa.DateTime(), server_default='now()', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='user'
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ts_create', sa.DateTime(), server_default='now()', nullable=False),
    sa.Column('first_user_id', sa.Integer(), nullable=True),
    sa.Column('second_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['first_user_id'], ['user.items.id'], ),
    sa.ForeignKeyConstraint(['second_user_id'], ['user.items.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='meet'
    )
    op.create_table('ratings',
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ratings', schema='user')
    op.drop_table('items', schema='meet')
    op.drop_table('items', schema='user')
    # ### end Alembic commands ###
    op.execute('DROP SCHEMA "user"')
    op.execute('DROP SCHEMA "meet"')