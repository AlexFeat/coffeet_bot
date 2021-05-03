from datetime import datetime as dt
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    String,
    DateTime,
    SmallInteger,
    ForeignKey,
    PrimaryKeyConstraint,
)
from ..meet.objects import meets_table
from .objects import users_table

metadata = MetaData()

user_ratings_table = Table(
    'ratings',
    metadata,
    Column('user_id', ForeignKey(users_table.c.id)),
    Column('meet_id', ForeignKey(meets_table.c.id)),
    Column('author_id', ForeignKey(users_table.c.id)),
    Column('ts_create', DateTime, nullable=False, default=dt.utcnow(), server_default='now()'),
    Column('rating', SmallInteger, nullable=False, default='5', server_default='5'),
    Column('comment', String, nullable=True, default='', server_default=''),
    PrimaryKeyConstraint('user_id', 'meet_id', name='rating_pk'),
    schema='user',
)
