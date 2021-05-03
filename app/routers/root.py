from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter()


@router.get("/", status_code=200)
async def index_page():
    r_data = {
        'msg': 'Hello friend!',
        'project': 'Coffeet',
        'about': 'This is a study project',
        'author': 'Aleksey Galaev aka Alex Feat'
    }
    return r_data
