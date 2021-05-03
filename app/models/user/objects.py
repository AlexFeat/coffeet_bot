from datetime import datetime as dt
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Date,
    DateTime,
    SmallInteger,
    ForeignKey,
    PrimaryKeyConstraint,
)
#from .meets import meets_table

metadata = MetaData()

users_table = Table(
    'items',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('date_birthday', Date, nullable=True),
    Column('telegram_id', String, nullable=False),
    Column('moderated_status', SmallInteger, nullable=False, default='0', server_default='0'),
    Column('ts_create', DateTime, nullable=False, default=dt.utcnow(), server_default='now()'),
    schema='user',
)

'''
user_ratings_table = Table(
    'ratings',
    metadata,
    Column('user_id', ForeignKey(users_table.c.id)),
    Column('meet_id', ForeignKey(meets_table.c.id)),
    Column('author_id', ForeignKey(users_table.c.id)),
    Column('rating', SmallInteger, nullable=False, default=5, server_default=5),
    Column('comment', String, nullable=True, default='', server_default=''),
    PrimaryKeyConstraint('user_id', 'meet_id', name='rating_pk'),
    schema='user',
)
'''
