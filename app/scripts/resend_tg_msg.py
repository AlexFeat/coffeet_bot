import logging
import aiohttp
import json

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from dotenv import dotenv_values, load_dotenv
from time import time


# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize bot and dispatcher
bot = Bot(token=dotenv_values('.env').get('TG_BOT_TOKEN'))
dp = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())

url = 'http://127.0.0.1:8000' + f"{dotenv_values('.env').get('TG_BOT_CB_URL')}"


async def next_update_id():
    num = 1
    while True:
        yield num
        num += 1


@dp.message_handler(content_types=types.ContentType.ANY)
async def echo_message(message: types.Message):
    # user_sender = message.from_user
    print(message.as_json())
    async with aiohttp.ClientSession() as session:
        body = {
            'message': dict(message),
            'update_id': int(time()),
        }
        print(body)
        async with session.post(url, data=json.dumps(body)) as resp:
            logging.debug(resp)
    return True


if __name__ == "__main__":
    upd_id = next_update_id()
    executor.start_polling(dp)
