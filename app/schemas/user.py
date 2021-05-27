from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime

from models import pg
from models.user.objects import users_table as user_object

moderated_enum = {
    0: 'Не определён',
    1: 'Премодерация',
    2: 'Одобрен',
    3: 'Постмодерация',
    -1: 'Заблокирован',
}


class User(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]
    date_birthday: Optional[date]
    telegram_id: int
    moderated_status: int
    ts_create: datetime
    is_active: bool

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def moderated(self):
        return moderated_enum.get(self.moderated_status) or moderated_enum.get(0)

    @classmethod
    async def get_by_tg(cls, data, *args, **kwargs):
        """
        Метод для создания объекта User на основе данных из TG
        :param data: набор данных из сообщения TG (message.from_user)
        :param args:
        :param kwargs:
        :return:
        """
        usr_query = user_object.select().where(user_object.c.telegram_id == data.id).limit(1)
        usr = await pg.fetchrow(usr_query)
        if usr is None:
            usr_ins_query = user_object.insert().values(
                telegram_id=data.id,
                first_name=data.first_name,
                last_name=data.last_name,
                moderated_status=1,
            ).returning(user_object)
            usr = await pg.fetchrow(usr_ins_query)
        return User(**usr)

    @classmethod
    async def get_by_id(cls, user_id: int, *args, **kwargs):
        """
        Метод для создания объекта User из БД
        :param user_id:
        :param args:
        :param kwargs:
        :return:
        """
        usr_query = user_object.select().where(user_object.c.telegram_id == user_id).limit(1)
        usr = await pg.fetchrow(usr_query)
        return User(**usr)
