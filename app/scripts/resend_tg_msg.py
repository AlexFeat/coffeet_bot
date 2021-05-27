import logging
import aiohttp
import json
import sys
from pathlib import Path

from aiogram import Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from dotenv import dotenv_values
from time import time

current_file = Path(__file__).resolve()
sys.path.insert(0, str(current_file.parent.parent))

from plugins.telegram.bot import bot

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize dispatcher
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

url = 'http://app:8000' + f"{dotenv_values('.env').get('TG_BOT_CB_URL')}"


@dp.message_handler(content_types=types.ContentType.ANY)
async def resend_message(message: types.Message):
    async with aiohttp.ClientSession() as session:
        body = {
            'message': dict(message),
            'update_id': int(time()),
        }
        async with session.post(url, data=json.dumps(body)) as resp:
            logging.debug(resp)
    return True


if __name__ == "__main__":
    executor.start_polling(dp)
