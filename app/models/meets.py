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
from .users import users_table


metadata = MetaData()

meets_table = Table(
    'items',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('ts_create', DateTime, nullable=False, default=dt.utcnow(), server_default='now()'),
    Column('first_user_id', ForeignKey(users_table.c.id)),
    Column('second_user_id', ForeignKey(users_table.c.id)),
    schema='meet',
)
