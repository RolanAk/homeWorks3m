
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
import os


async def quiz_1(message: types.Message):

    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    button = InlineKeyboardButton('next', callback_data='quiz_2')

    keyboard.add(button)

    question = 'where are u from'

    options = ['bishkek', 'tokyo', 'toronto']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=options,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='gay',
        open_period=5,
        reply_markup=keyboard
    )


async def quiz_2(call: types.CallbackQuery):

    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    button = InlineKeyboardButton('next', callback_data='quiz_3')

    keyboard.add(button)

    question = 'choose country'

    options = ['kg', 'kz', 'russia', 'canada']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=options,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='chochun',
        open_period=5,
        reply_markup=keyboard
    )


async def quiz_3(call: types.CallbackQuery):

    with open("D:\python\less1M3\media\img_1.png", 'rb') as photo:
        await bot.send_photo(chat_id=call.from_user.id, photo=photo)

    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    button = InlineKeyboardButton('next', callback_data='quiz_3')

    keyboard.add(button)

    question = 'which dragon in GoT was biggest'

    options = ['caraxes', 'balerion', 'dreamfire', 'drogon']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=options,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation='u fail',
        open_period=5,
        reply_markup=keyboard
    )


async def game_dice(message: types.Message):

    await bot.send_dice(
        chat_id=message.from_user.id,
        disable_notification=None,
        reply_to_message_id=None,
        reply_markup=None,
        emoji=None,
        protect_content=None,

    )


def register_handler_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text=['quiz_2'])
    dp.register_callback_query_handler(quiz_3, text=['quiz_3'])
    dp.register_message_handler(game_dice, commands=['game'])



