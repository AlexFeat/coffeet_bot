from datetime import datetime as dt
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    DateTime,
    ForeignKey,
)

from models.user.objects import users_table


metadata = MetaData()

'''
TODO
    дата и время начала встречи
    место встречи
'''
meets_table = Table(
    'items',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('ts_create', DateTime, nullable=False, default=dt.utcnow(), server_default='now()'),
    Column('first_user_id', ForeignKey(users_table.c.id)),
    Column('second_user_id', ForeignKey(users_table.c.id)),
    schema='meet',
)
