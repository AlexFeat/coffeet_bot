from aiogram import Bot, Dispatcher, types
from plugins.telegram.dependencies import bot_dispatcher
from fastapi import APIRouter, Body, Depends
from typing import (
    Dict,
    Any,
)

router = APIRouter(
    prefix='/callback'
)


@router.post("/tg")
async def callback_telegram(
        request: Dict[str, Any] = Body(...),
        dp: Dispatcher = Depends(bot_dispatcher)):
    Bot.set_current(dp.bot)
    Dispatcher.set_current(dp)
    telegram_update = types.Update(**request)
    await dp.process_update(telegram_update)
    return {'status': 'OK'}


@router.on_event("shutdown")
async def disconnect_storage():
    dp = bot_dispatcher()
    await dp.storage.close()
    await dp.storage.wait_closed()
