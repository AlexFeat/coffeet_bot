from pydantic import BaseModel
from datetime import date, datetime, time
from sqlalchemy import and_, func

from models import pg
from models.meet.requests import meet_requests_table as meet_request


class MeetRequest(BaseModel):
    id: int
    ts_create: datetime
    user_id: int
    date_meet: date
    meet_from: time
    meet_to: time
    date_expire: date

    @classmethod
    async def create(cls, data):
        if 'date_meet' in data and isinstance(data['date_meet'], str):
            data['date_meet'] = datetime.strptime(data['date_meet'], '%Y-%m-%d')
        if 'date_expire' in data and isinstance(data['date_expire'], str):
            data['date_expire'] = datetime.strptime(data['date_expire'], '%Y-%m-%d')
        if 'meet_from' in data and isinstance(data['meet_from'], str):
            data['meet_from'] = datetime.strptime(data['meet_from'], '%H:%M')
        if 'meet_to' in data and isinstance(data['meet_to'], str):
            data['meet_to'] = datetime.strptime(data['meet_to'], '%H:%M')

        mr_ins_query = meet_request.insert().values(
            **data,
        ).returning(meet_request)
        meet_req = await pg.fetchrow(mr_ins_query)

        return MeetRequest(**meet_req)

    @classmethod
    async def get_firsts(cls, user_id, count=5):
        mr_query = meet_request.select().where(
            and_(
                meet_request.c.user_id == user_id,
                meet_request.c.date_meet > func.now(),
                meet_request.c.date_expire > func.now(),
            )
        ).limit(count)
        result = []
        for row in await pg.fetch(mr_query):
            result.append(MeetRequest(**row))
        return result

    async def get_similar(self):
        pass
