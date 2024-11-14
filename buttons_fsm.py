
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

a = True

cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=a)
cancel_button = KeyboardButton('cancel')
cancel.add(cancel_button)