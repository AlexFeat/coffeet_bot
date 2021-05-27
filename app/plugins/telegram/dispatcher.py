from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from plugins.telegram.bot import bot

# TODO Redis
storage = MemoryStorage()

dispatcher = Dispatcher(bot, storage=storage)
dispatcher.middleware.setup(LoggingMiddleware())
