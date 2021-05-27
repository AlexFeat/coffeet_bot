from plugins.telegram.dispatcher import dispatcher
from aiogram import (
    Dispatcher,
    Bot,
)


def bot_dispatcher() -> Dispatcher:
    Bot.set_current(dispatcher.bot)
    Dispatcher.set_current(dispatcher)
    return dispatcher


def telegram_bot() -> Bot:
    return dispatcher.bot
