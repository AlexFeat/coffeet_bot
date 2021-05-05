from aiogram import Bot
from dotenv import dotenv_values

bot = Bot(token=dotenv_values('.env').get('TG_BOT_TOKEN'))
