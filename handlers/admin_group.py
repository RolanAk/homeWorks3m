from aiogram import types, Dispatcher
from config import bot, Admins

async def welcome_users(message: types.Message):
    for member in message.new_chat_members:
        await message.answer(f'welcome home, {member.full_name}\n\n'
                             f'group rule:\n'
                             f'do not say n word')

user_warnings = {}

async def user_warning(message:types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in Admins:
            await message.answer('u have no rights')
        elif not message.reply_to_message:
            await message.answer('commands should been answer for message')
        else:
            user_id = message.reply_to_message.from_user.id
            user_name = message.reply_to_message.from_user.full_name
            user_warnings[user_id] = user_warnings.get(user_id, 0) + 1

            for admin in Admins:
                await bot.send_message(chat_id=admin,
                                       text=f'{user_name} get warning ({user_warnings[user_id]}\3)')
                if user_warnings[user_id] >= 3:
                    await bot.kick_chat_member(message.chat.id, user_id)
                    await bot.unban_chat_member(message.chat.id, user_id)

                    await bot.send_message(chat_id=message.chat.id,
                                           text=f'{user_name}u were deleted cuz u looks like a gay')
words = ['durak', 'gay', 'nigger']

async def filter_words(message: types.Message):
    message.text = message.text.lower()

    for word in words:
        if word in message.text:

            await message.answer(f' do not say bad words {message.from_user.full_name}')

            await message.delete()

            user_id = message.reply_to_message.from_user.id
            user_name = message.reply_to_message.from_user.full_name
            user_warnings[user_id] = user_warnings.get(user_id, 0) + 1

            for admin in Admins:
                await bot.send_message(chat_id=admin,
                                       text=f'{user_name} get warning ({user_warnings[user_id]}\3)')
            break


async def pin_message(message: types.Message):
    await bot.pin_chat_message(chat_id=message.chat.id, message_id=message.reply_to_message)

def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(welcome_users, content_types=[types.ContentType.NEW_CHAT_MEMBERS])
    dp.register_message_handler(user_warning, commands=['ban'])
    dp.register_message_handler(pin_message, commands=['pin'])
    dp.register_message_handler(filter_words)