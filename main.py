import logging

from aiogram import executor

from config import bot, dp, Admins
from handlers import commands, quiz, fsm_reg, echo, fsm_hw,webapp,admin_group
from db_main import db
from db_hw import db_hw_main


async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='bot in work')


async def on_shutdown(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='bot is off')


commands.register_commands(dp)
quiz.register_handler_quiz(dp)
fsm_reg.reg_handler_fsm_registration(dp)
fsm_hw.reg_handler_fsm_store(dp)
webapp.register_webapp_hanlders(dp)
admin_group.register_admin_handlers(dp)
echo.register_echo(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, allowed_updates=['callback'],
                           on_startup=on_startup, on_shutdown=on_shutdown)

