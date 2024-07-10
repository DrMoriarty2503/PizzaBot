from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
b4=KeyboardButton('/Корзина')
# b4 = KeyboardButton('Поделиться номером телефона', request_contact=True)
# b5 = KeyboardButton('Поделиться расположением', request_location = True)

kb_client=ReplyKeyboardMarkup(resize_keyboard=True)
# one_time_keyboard=True - скрывает кнопки(пользователь может их открыть обратно


kb_client.add(b1).insert(b2).add(b3)#row(b4,b5)
# kb_client.row(b1,b2,b3)

bm1 = KeyboardButton('/Пицца🍕')
bm2 = KeyboardButton('/Роллы🍱')
bm3 = KeyboardButton('/Напитки🍹')
back_button=KeyboardButton('/В_начало')
menu_categories=ReplyKeyboardMarkup(resize_keyboard=True)
menu_categories.row(bm1,bm2,bm3).add(back_button)

