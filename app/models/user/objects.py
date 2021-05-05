from datetime import datetime as dt
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    String,
    Date,
    DateTime,
    SmallInteger,
    BigInteger,
    Boolean,
)

metadata = MetaData()

users_table = Table(
    'items',
    metadata,
    Column('id', BigInteger, primary_key=True),
    Column('first_name', String, nullable=False),
    Column('last_name', String, nullable=False),
    Column('date_birthday', Date, nullable=True),
    Column('telegram_id', BigInteger, nullable=False, unique=True),
    Column('moderated_status', SmallInteger, nullable=False, default=0, server_default='0'),
    Column('ts_create', DateTime, nullable=False, default=dt.utcnow(), server_default='now()'),
    Column('is_active', Boolean, nullable=False, default=True, server_default='true'),
    schema='user',
)
