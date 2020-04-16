from main import bot, dp
from aiogram.types import Message
from config import admin_id
from keyboards import ListOfButtons
from filters import *
from vebinar import *
from covid_kg import *
from covid_world import *
from news_actual import *
from news_main import *


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Bot is working')


@dp.message_handler(Button('Обучение'))
async def btn1(message: Message):
    inline_keyboard = ListOfButtons(
        text=['Регистрация'],
        callback=['regis'],
        align=[1]  # 2-это сколько кнопок в одном ряду
    ).inline_keyboard
    await message.reply(f'Вы в разделе "Обучение"\n\n{veb_title}\n{veb_text}\n{veb_link}', reply_markup=inline_keyboard)


@dp.message_handler(Button('Рассылка'))
async def btn2(message: Message):
    await message.answer(f'Вы в разделе "Рассылка"\n\n{veb_title}\n{veb_text}\n{veb_link}')


@dp.message_handler(Button('Анкетирование'))
async def btn3(message: Message):
    await message.answer('Вы в разделе "Анкетирование"')


@dp.message_handler(Button('COVID-19'))
async def btn3(message: Message):
    inline_keyboard = ListOfButtons(
        text=['Ситуация в КР', 'Ситуация в мире'],
        callback=['kg', 'world'],
        align=[1, 1]
    ).inline_keyboard
    await message.reply(text=message.text, reply_markup=inline_keyboard)


@dp.message_handler(Button('Новости'))
async def btn3(message: Message):
    inline_keyboard = ListOfButtons(
        text=['Актуальные новости', 'Все новости'],
        callback=['act_news', 'all_news'],
        align=[1, 1]
    ).inline_keyboard
    await message.reply(text=message.text, reply_markup=inline_keyboard)


@dp.callback_query_handler(Button('kg'))
async def btn1(call: CallbackQuery):
    await call.message.reply(f'Общее количество: {total}\nЗа сутки: {today}\nИзлечились: {cured}\nУмерло: {died_kg}')


@dp.callback_query_handler(Button('world'))
async def btn1(call: CallbackQuery):
    await call.message.reply(f'Общее количество: {total_world}\nУмерло: {died_world}')


@dp.callback_query_handler(Button('act_news'))
async def btn2(call: CallbackQuery):
    inline_keyboard = ListOfButtons(
        text=['Все новости'],
        callback=['all_news'],
        align=[1]
    ).inline_keyboard
    await call.message.answer(f'{news_1_main}\n{link_1_main}')
    await call.message.answer(f'{news_2_main}\n{link_2_main}')
    await call.message.answer(f'{news_3_main}\n{link_3_main}')
    await call.message.answer(f'{news_4_main}\n{link_4_main}')
    await call.message.answer(f'{news_5_main}\n{link_5_main}')
    await call.message.answer(f'{news_6_main}\n{link_6_main}', reply_markup=inline_keyboard)


@dp.callback_query_handler(Button('all_news'))
async def btn3(call: CallbackQuery):
    inline_keyboard = ListOfButtons(
        text=['Еще'],
        callback=['next'],
        align=[1]
    ).inline_keyboard
    # await call.message.edit_reply_markup() #для того чтобы убрать клавиатуру
    await call.message.answer(f'{news_1}\n{link_1}')
    await call.message.answer(f'{news_2}\n{link_2}')
    await call.message.answer(f'{news_3}\n{link_3}')
    await call.message.answer(f'{news_4}\n{link_4}')
    await call.message.answer(f'{news_5}\n{link_5}', reply_markup=inline_keyboard)


@dp.callback_query_handler(Button('next'))
async def btn3(call: CallbackQuery):
    await call.message.edit_reply_markup() #для того чтобы убрать клавиатуру
    await call.message.answer(f'{news_6}\n{link_6}')
    await call.message.answer(f'{news_7}\n{link_7}')
    await call.message.answer(f'{news_8}\n{link_8}')
    await call.message.answer(f'{news_9}\n{link_9}')
    await call.message.answer(f'{news_10}\n{link_10}')



@dp.message_handler()
async def keyboards(message: Message):
    text = 'Выберите раздел'
    keyboard = ListOfButtons(
        text=['Обучение', 'Рассылка', 'Анкетирование', 'COVID-19', 'Новости'],
        align=[2, 2, 1]  # 2-это сколько кнопок в одном ряду
    ).reply_keyboard
    await message.reply(text=text, reply_markup=keyboard)