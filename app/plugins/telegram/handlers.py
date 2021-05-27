import aiogram.utils.markdown as md
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode

import re

from plugins.telegram.dispatcher import dispatcher
from schemas.user import User
from schemas.meet import MeetRequest


# States
class MeetRequestState(StatesGroup):
    date_meet = State()
    meet_from = State()
    meet_to = State()
    date_expire = State()


# msg handlers
@dispatcher.message_handler(commands=['help', 'start'])
async def echo_help(message: types.Message):
    await User.get_by_tg(message.from_user)
    text = f'''
/help - подсказки по командам
/me - информация о себе
/meet_request_add - создать заявку
/meet_request_list - список активных заявок
/cancel - отмена заполнения формы
        '''
    return await message.answer(text)


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


@dispatcher.message_handler(commands=['rating'])
async def echo_rating(message: types.Message):
    return await message.answer("The command 'rating' is not yet supported. Sorry!")


@dispatcher.message_handler(commands=['meet_request_list'])
async def send_meet_request(message: types.Message):
    user = await User.get_by_tg(message.from_user)
    strings = []
    for mr in await MeetRequest.get_firsts(user.id, 5):
        strings.append(
            md.text('Встреча', f'{mr.date_meet},', 'время начала с', mr.meet_from, 'до', mr.meet_to)
        )
        strings.append(
            md.text('Актуальна до', mr.date_expire)
        )

    if len(strings) == 0:
        await message.bot.send_message(
            message.chat.id,
            md.text('У вас нет назначенных заявок на встречи:')
        )
        return

    await message.bot.send_message(
        message.chat.id,
        md.text(
            md.text('Назначенные вами заявки на ближайшие встречи'),
            *strings,
            sep='\n',
        ),
        parse_mode=ParseMode.MARKDOWN,
    )


@dispatcher.message_handler(commands=['meet_request_add'])
async def send_meet_request(message: types.Message):
    await MeetRequestState.date_meet.set()
    await message.reply("Введите удобную дату для проведения встречи (YYYY-MM-DD)")


@dispatcher.message_handler(state='*', commands='cancel')
@dispatcher.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Заполнение формы отменено.', reply_markup=types.ReplyKeyboardRemove())


# create meet request by state
@dispatcher.message_handler(state=MeetRequestState.date_meet)
async def process_name(message: types.Message, state: FSMContext):
    if not re.match('^\d{4}-\d{2}-\d{2}$', message.text):
        await message.reply("Введите удобную дату для проведения встречи (YYYY-MM-DD)")
        return
    async with state.proxy() as data:
        data['date_meet'] = message.text
    await MeetRequestState.next()
    await message.reply("Введите минимально приемлимое время начала встречи (HH-MM)")


@dispatcher.message_handler(state=MeetRequestState.meet_from)
async def process_name(message: types.Message, state: FSMContext):
    if not re.match('^[0-1][0-9]:[0-5][0-9]$', message.text):
        await message.reply("Введите минимально приемлимое время начала встречи (HH-MM)")
        return
    async with state.proxy() as data:
        data['meet_from'] = message.text
    await MeetRequestState.next()
    await message.reply("Введите максимально приемлимое время начала встречи (HH-MM)")


@dispatcher.message_handler(state=MeetRequestState.meet_to)
async def process_name(message: types.Message, state: FSMContext):
    if not re.match('^[0-1][0-9]:[0-5][0-9]$', message.text):
        await message.reply("Введите максимально приемлимое время начала встречи (HH-MM)")
        return
    async with state.proxy() as data:
        data['meet_to'] = message.text
    await MeetRequestState.next()
    await message.reply("Введите дату истечения срока заявки (YYYY-MM-DD)")


@dispatcher.message_handler(state=MeetRequestState.date_expire)
async def process_name(message: types.Message, state: FSMContext):
    if not re.match('^\d{4}-\d{2}-\d{2}$', message.text):
        await message.reply("Введите дату истечения срока заявки (YYYY-MM-DD)")
        return
    user = await User.get_by_tg(message.from_user)
    async with state.proxy() as data:
        data['date_expire'] = message.text
        data['user_id'] = user.id

        await MeetRequest.create(data)
        await message.bot.send_message(
            message.chat.id,
            md.text(
                md.text('Ваши данные'),
                md.text('Дата проведения:', data['date_meet']),
                md.text('Время начада: с', data['meet_from'], 'по', data['meet_to']),
                md.text('Заявка потеряет актуальность:', data['date_expire']),
                md.text('Как только мы найдём вам коллегу, то сразу сообщим!'),
                sep='\n',
            ),
            parse_mode=ParseMode.MARKDOWN,
        )

    await state.finish()


# Хэндлер на любое сообщение боту
@dispatcher.message_handler(content_types=types.ContentType.ANY)
async def echo_message(message: types.Message):
    user = await User.get_by_tg(message.from_user)
    return await message.answer(f"Hello {user.name}! I don't understand you! Try /help")
