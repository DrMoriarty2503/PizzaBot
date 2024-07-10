from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import  State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ID=None
#fsm для загрузки пиццы
class FSMAdmin_1(StatesGroup):
    photo = State()
    name = State()
    description=State()
    price = State()

#fsm для загрузки rolls
class FSMAdmin_2(StatesGroup):
    photo = State()
    name = State()
    description=State()
    price = State()


# fsm для загрузки drinks
class FSMAdmin_3(StatesGroup):
    photo = State()
    name = State()
    description=State()
    price = State()

# получаем айди текущего модератора(нужно для админки)
# @dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id,'Какая функция администратора вам нужна ?', reply_markup=admin_kb.button_case_admin)
    await message.delete()


# @dp.message_handler(commands=['admin','обратно')
async def start_admin(message: types.Message):
    if message.from_user.id==ID:
        await bot.send_message(message.from_user.id, 'Какая функция администратора вам нужна ?',
                               reply_markup=admin_kb.button_case_admin)
# # @dp.message_handler(commands='Удалить')
# async def delete(message: types.Message):
#     if message.from_user.id == ID:
#         bot.send_message(message.from_user.id,'Выберите категорию удаления',reply_markup=admin_kb.choise_menu_del)

# выбор категории загрузки
# @dp.message_handler(commands= 'Загрузить')
async def loads(message: types.Message):
    if message.from_user.id==ID:
        await bot.send_message(message.from_user.id, 'Выберите категорию меню для загрузки ', reply_markup=admin_kb.choise_menu_load)

# начало диалога загрузки нового пункта меню
# @dp.message_handler(commands= 'Пицца', state = None)
async def cm_start_1(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin_1.photo.set()
        await message.reply('Загрузи фото')


# выход из состояний
# @dp.message_handler(state='*', commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state=await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')

# ловим первый ответ и пишем в словарь
# @dp.message_handler(content_types=['photo'],state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_1:
            data_1['photo']=message.photo[0].file_id
        await FSMAdmin_1.next()
        await message.reply('Теперь введите название')

# ловим второй ответ
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_1:
            data_1['name']=message.text
        await FSMAdmin_1.next()
        await message.reply('Введите описание')

# ловим третий ответ
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_1:
            data_1['description']=message.text
        await FSMAdmin_1.next()
        await message.reply('Теперь укажи цену')

# ловим последнйи ответ и используем полученные данные
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_1:
            data_1['price']=float(message.text)
        # async with state.proxy() as data:
        #     await message.reply(str(data))
        await sqlite_db.sql_add_pizza_menu(state)

        await state.finish()


# начало диалога загрузки нового пункта меню
# @dp.message_handler(commands= 'Роллы', state = None)
async def cm_start_2(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin_2.photo.set()
        await message.reply('Загрузи фото')


# выход из состояний
# @dp.message_handler(state='*', commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state=await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')

# ловим первый ответ и пишем в словарь
# @dp.message_handler(content_types=['photo'],state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_2:
            data_2['photo']=message.photo[0].file_id
        await FSMAdmin_2.next()
        await message.reply('Теперь введите название')

# ловим второй ответ
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_2:
            data_2['name']=message.text
        await FSMAdmin_2.next()
        await message.reply('Введите описание')

# ловим третий ответ
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_2:
            data_2['description']=message.text
        await FSMAdmin_2.next()
        await message.reply('Теперь укажи цену')

# ловим последнйи ответ и используем полученные данные
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_2:
            data_2['price']=float(message.text)
        # async with state.proxy() as data:
        #     await message.reply(str(data))
        await sqlite_db.sql_add_rolls_menu(state)

        await state.finish()

# ''''''''''''''''''''''''''''''''''''
#


# начало диалога загрузки нового пункта меню
# @dp.message_handler(commands= 'Напитки', state = None)
async def cm_start_3(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin_3.photo.set()
        await message.reply('Загрузи фото')


# выход из состояний
# @dp.message_handler(state='*', commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state=await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')

# ловим первый ответ и пишем в словарь
# @dp.message_handler(content_types=['photo'],state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_3:
            data_3['photo']=message.photo[0].file_id
        await FSMAdmin_3.next()
        await message.reply('Теперь введите название')

# ловим второй ответ
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_3:
            data_3['name']=message.text
        await FSMAdmin_3.next()
        await message.reply('Введите описание')

# ловим третий ответ
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_3:
            data_3['description']=message.text
        await FSMAdmin_3.next()
        await message.reply('Теперь укажи цену')

# ловим последнйи ответ и используем полученные данные
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data_3:
            data_3['price']=float(message.text)
        # async with state.proxy() as data:
        #     await message.reply(str(data))
        await sqlite_db.sql_add_drinks_menu(state)

        await state.finish()




# @dp.message_handler(commands='Удалить')
async def delete(message: types.Message):
    if message.from_user.id == ID:
        await bot.send_message(message.from_user.id,'Выберите категорию удаления',reply_markup=admin_kb.choise_menu_del)



@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run_1(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_pizza(callback_query.data.replace('del ',''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена', show_alert=True)

# @dp.message_handler(commands='Удалить_пиццу')
async def delete_pizza(message: types.Message):
        if message.from_user.id ==ID:
            read=await sqlite_db.sql_del_1()
            for ret in read:
                await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')
                await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                       add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run_2(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_rolls(callback_query.data.replace('del ',''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена', show_alert=True)

# @dp.message_handler(commands='Удалить_роллы')
async def delete_rolls(message: types.Message):
        if message.from_user.id ==ID:
            read=await sqlite_db.sql_del_2()
            for ret in read:
                await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')
                await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                       add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run_3(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_drinks(callback_query.data.replace('del ',''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена', show_alert=True)

# @dp.message_handler(commands='Удалить_напиток')
async def delete_drinks(message: types.Message):
        if message.from_user.id ==ID:
            read=await sqlite_db.sql_del_3()
            for ret in read:
                await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')
                await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                       add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))




# регистрируем хэндлеры
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(loads,commands= 'Загрузить')
    dp.register_message_handler(delete, commands='Удалить')
    dp.register_message_handler(start_admin,commands=['admin','обратно'])
    dp.register_message_handler(delete_pizza, commands='Удалить_пиццу')
    dp.register_message_handler(delete_rolls, commands='Удалить_роллы')
    dp.register_message_handler(delete_drinks, commands='Удалить_напиток')
    dp.register_message_handler(cm_start_1,commands= 'Пицца', state = None)
    dp.register_message_handler(cm_start_2, commands='Роллы', state=None)
    dp.register_message_handler(cm_start_3, commands='Напитки', state=None)
    dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(load_photo,content_types=['photo'], state=FSMAdmin_1.photo)
    dp.register_message_handler(load_name,state=FSMAdmin_1.name)
    dp.register_message_handler(load_description,state=FSMAdmin_1.description)
    dp.register_message_handler(load_price,state=FSMAdmin_1.price)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin_2.photo)
    dp.register_message_handler(load_name, state=FSMAdmin_2.name)
    dp.register_message_handler(load_description, state=FSMAdmin_2.description)
    dp.register_message_handler(load_price, state=FSMAdmin_2.price)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin_3.photo)
    dp.register_message_handler(load_name, state=FSMAdmin_3.name)
    dp.register_message_handler(load_description, state=FSMAdmin_3.description)
    dp.register_message_handler(load_price, state=FSMAdmin_3.price)




