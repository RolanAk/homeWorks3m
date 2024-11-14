from aiogram import types, Dispatcher
from config import bot, dp
import os


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f' hello {message.from_user.first_name} \n '
                                f'this is your telegram id - {message.from_user.id}')


async def send_mem(message: types.Message):
    photo_path = os.path.join("media", "img.png")

    with open(photo_path, "rb") as image:
        await message.answer_photo(photo=image,
                                   caption='Mem')


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(send_mem, commands=["mem"])

