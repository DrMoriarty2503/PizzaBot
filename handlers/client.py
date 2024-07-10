from aiogram import types, Dispatcher
from create_bot import dp,bot
from keyboards import kb_client, client_kb
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


#обработчик начальных комманд
# @dp.message_handler(commands=['start','help','В_главное_меню])
async def start_commands(message : types.Message):
    try:
        await bot.send_message(message.from_user.id,' Пицца Хаус приветствует вас.Приятного аппетита!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через лс, напишите ему')

#обработчик команды /режим_работы
# @dp.message_handler(commands=['Режим_работы'])
async def work_time(message: types.Message):
    await bot.send_message(message.from_user.id,'Тут будет режим работы')
# reply_markup=ReplyKeyboardRemove() - удаляет клавиатуру после нажатия определенной кнопки

#обработчик команды расположение
# @dp.message_handler(commands=['Расположение'])
async def work_place(message: types.Message):
    await bot.send_message(message.from_user.id,'Тут будет адрес',)


# @dp.message_handler(commands='Меню')
async def pizza_menu_command(message: types.Message):
    # await sqlite_db.sql_read(message)
    await bot.send_message(message.from_user.id,'Выберите категорию меню',reply_markup=client_kb.menu_categories)

# @dp.message_handler(commands='Пицца🍕')
async def read_pizza_menu(message: types.Message):
    await sqlite_db.sql_read_pizza_menu(message)

# @dp.message_handler(commands='Роллы🍱')
async def read_rolls_menu(message: types.Message):
    await sqlite_db.sql_read_rolls_menu(message)

# @dp.message_handler(commands='Напитки🍹')
async def read_drinks_menu(message: types.Message):
    await sqlite_db.sql_read_drinks_menu(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_commands,commands=['start','help','В_начало'])
    dp.register_message_handler(work_time, commands=['Режим_работы'])
    dp.register_message_handler(work_place, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command,commands=['Меню'])
    dp.register_message_handler(read_pizza_menu,commands='Пицца🍕')
    dp.register_message_handler(read_rolls_menu,commands='Роллы🍱')
    dp.register_message_handler(read_drinks_menu, commands='Напитки🍹')