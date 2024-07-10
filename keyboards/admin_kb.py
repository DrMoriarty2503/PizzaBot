from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# кнопки клавиатруы админа
button_load = KeyboardButton('/Загрузить')
button_delete=KeyboardButton('/Удалить')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).row(button_load, button_delete)

#кнопки для выбора категории загрузки
menu_pizza_load=KeyboardButton('/Пицца')
menu_rolls_load=KeyboardButton('/Роллы')
menu_drinks_load=KeyboardButton('/Напитки')
back_button_1=KeyboardButton('/обратно')
choise_menu_load=ReplyKeyboardMarkup(resize_keyboard=True).row(menu_pizza_load,menu_rolls_load,menu_drinks_load).add(back_button_1)

menu_pizza_del=KeyboardButton('/Удалить_пиццу')
menu_rolls_del=KeyboardButton('/Удалить_роллы')
menu_drinks_del=KeyboardButton('/Удалить_напиток')
back_button_2=KeyboardButton('/обратно')
choise_menu_del=ReplyKeyboardMarkup(resize_keyboard=True).row(menu_pizza_del,menu_rolls_del,menu_drinks_del).add(back_button_2)