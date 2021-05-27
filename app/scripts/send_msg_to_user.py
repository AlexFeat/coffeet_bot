import asyncio
from plugins.telegram.bot import bot


async def do():
    await bot.send_message(428498052, 'message.text test')


if __name__ == '__main__':
    asyncio.run(do())
