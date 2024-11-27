from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

async def reply_webapp(message: types.Message):

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)

    geeks_online = KeyboardButton('geeks online', web_app=WebAppInfo(url='https://online.geeks.kg/'))
    youtube = KeyboardButton('you tube', web_app=WebAppInfo(url='https://www.youtube.com/'))
    instagram = KeyboardButton('instagram', web_app=WebAppInfo(url='https://www.instagram.com/'))
    shikimori = KeyboardButton('shikimori', web_app=WebAppInfo(url='https://shikimori.one/'))
    twitch = KeyboardButton('twitch', web_app=WebAppInfo(url='https://www.twitch.tv/'))

    keyboard.add(geeks_online)

    await message.answer(text='webapp buttons', reply_markup=keyboard)


async def inline_webapp(message: types.Message):

    keyboard = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)

    geeks_online = InlineKeyboardButton('utube', web_app=WebAppInfo(url='https://www.youtube.com/'))

    keyboard.add(geeks_online)

    await message.answer(text='webapp buttons', reply_markup=keyboard)

def register_webapp_hanlders(dp: Dispatcher):
    dp.register_message_handler(reply_webapp, commands='webapp_r')
    dp.register_message_handler(inline_webapp, commands='webapp_i')
