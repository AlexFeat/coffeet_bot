from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from app.plugins.telegram.bot import bot

dispatcher = Dispatcher(bot)
dispatcher.middleware.setup(LoggingMiddleware())
