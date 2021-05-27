from datetime import datetime as dt
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    Date,
    Time,
    DateTime,
    ForeignKey,
    SmallInteger,
)
from models.user.objects import users_table

metadata = MetaData()

meet_requests_table = Table(
    'requests',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('ts_create', DateTime, nullable=False, default=dt.utcnow(), server_default='now()'),
    Column('user_id', ForeignKey(users_table.c.id),
           comment='Идентификатор пользователя оставившего заявку'),
    Column('date_meet', Date, nullable=False,
           comment='Дата проведения встречи'),
    Column('meet_from', Time, nullable=False,
           comment='Встреча должна начаться не раньше указанного времени'),
    Column('meet_to', Time, nullable=False,
           comment='Встреча должна закнчиться не позже указанного времени'),
    Column('date_expire', Date, nullable=False,
           comment='Дата истечения срока актуальности заявки'),
    Column('status', SmallInteger, nullable=False, default="1", server_default="1",
           comment='Статус заявки'),
    schema='meet',
)
