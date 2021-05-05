from dotenv import dotenv_values
from asyncpgsa import pg


async def connect():
    print('DB connecting')
    await pg.init(
        user=dotenv_values('.env').get('DB_USER'),
        password=dotenv_values('.env').get('DB_PASS'),
        database=dotenv_values('.env').get('DB_NAME'),
        host=dotenv_values('.env').get('DB_HOST'),
        port=dotenv_values('.env').get('DB_PORT'),
        # loop=loop,
        min_size=5,
        max_size=10
    )
    return pg


__all__ = [
    pg,
]
