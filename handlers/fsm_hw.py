from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from db_main import db
import buttonsForFsmHw


class store_fsm(StatesGroup):

    name = State()
    category = State()
    size = State()
    price = State()
    photo = State()
    submit = State()


async def start_fsm_store(message: types.Message):
    await store_fsm.name.set()
    await message.answer(text='Введите название товара: ',
                         reply_markup=buttonsForFsmHw.cancel)


async def load_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.answer("Введите категорию для товара: ")
    await store_fsm.next()


async def load_category(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await message.answer("Введите размер товара: ")
    await store_fsm.next()


async def load_size(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await message.answer("Введите цену товара: ")
    await store_fsm.next()


async def load_price(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await message.answer("Отправьте фото товара: ")
    await store_fsm.next()


async def load_photo(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer_photo(photo=data['photo'],
                               caption=f"Заполненный товар: \n"
                                       f"Название - {data['name']}\n"
                                       f"категория - {data['category']}\n"
                                       f"Размер - {data['size']}\n"
                                       f"Цена - {data['price']}\n")

    await message.answer("Верные ли данные?", reply_markup=buttonsForFsmHw.submit)
    await store_fsm.next()


async def submit(message: types.Message, state=FSMContext):
    if message.text == 'Да':
        kb_remove = types.ReplyKeyboardRemove()
        await message.answer('Отлично, товар в базе!', reply_markup=kb_remove)

        async with state.proxy() as data:
            await db.sql_insert_store(
                name=data['name'],
                category=data['category'],
                size=data['size'],
                price=data['price'],
                photo=data['photo'],
            )

    elif message.text == 'Нет':
        kb_remove = types.ReplyKeyboardRemove()
        await message.answer('canceld', reply_markup=kb_remove)

    else:
        await message.answer('Введите Да или Нет')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    kb_remove = types.ReplyKeyboardRemove()

    if current_state is not None:
        await state.finish()
        await message.answer('canceld', reply_markup=kb_remove)


def reg_handler_fsm_store(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='cancel', ignore_case=True),
                                state="*")

    dp.register_message_handler(start_fsm_store, commands=['store'])
    dp.register_message_handler(load_name, state=store_fsm.name)
    dp.register_message_handler(load_category, state=store_fsm.category)
    dp.register_message_handler(load_size, state=store_fsm.size)
    dp.register_message_handler(load_price, state=store_fsm.price)
    dp.register_message_handler(load_photo, state=store_fsm.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=store_fsm.submit)



