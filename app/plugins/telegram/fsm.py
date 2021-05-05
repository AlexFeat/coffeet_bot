from aiogram import types
from app.plugins.telegram.dispatcher import dispatcher
from app.schemas.user import User


@dispatcher.message_handler(commands=['me'])
async def echo_me(message: types.Message):
    user = await User.get_by_tg(message.from_user)
    text = f'''
Пользовател {user.name} (id: {user.id})
Создан: {user.ts_create}
Статус: {user.moderated}
Активен: {(user.is_active and 'Да') or'Нет'}
    '''
    return await message.answer(text)


@dispatcher.message_handler(commands=['help'])
async def echo_help(message: types.Message):
    return await message.answer(f"Help hasn't been written yet")


# Хэндлер на любое сообщение боту
@dispatcher.message_handler(content_types=types.ContentType.ANY)
async def echo_message(message: types.Message):
    user = await User.get_by_tg(message.from_user)
    return await message.answer(f"Hello {user.name}! I don't understand you! Try /help")
