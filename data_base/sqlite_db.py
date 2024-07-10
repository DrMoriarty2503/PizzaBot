import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base= sq.connect('pizza_cool.db')
    cur=base.cursor()
    if base:
        print('Data Base connected OK')
    base.execute('CREATE TABLE IF NOT EXISTS menu_pizza(img TEXT, name TEXT PRIMARY KEY,description TEXT, price TEXT )')
    base.commit()
    base.execute('CREATE TABLE IF NOT EXISTS menu_rolls(img TEXT, name TEXT PRIMARY KEY,description TEXT, price TEXT )')
    base.commit()
    base.execute('CREATE TABLE IF NOT EXISTS menu_drinks(img TEXT, name TEXT PRIMARY KEY,description TEXT, price TEXT )')
    base.commit()



async def sql_add_pizza_menu(state):
    async with state.proxy() as data_1:
        cur.execute('INSERT INTO menu_pizza VALUES (?, ?, ?, ?)', tuple(data_1.values()))
        base.commit()

async def sql_read_pizza_menu(message):
    for ret in cur.execute('SELECT * FROM menu_pizza').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')

async def sql_add_rolls_menu(state):
    async with state.proxy() as data_2:
        cur.execute('INSERT INTO menu_rolls VALUES (?, ?, ?, ?)', tuple(data_2.values()))
        base.commit()

async def sql_read_rolls_menu(message):
    for ret in cur.execute('SELECT * FROM menu_rolls').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')


async def sql_add_drinks_menu(state):
    async with state.proxy() as data_3:
        cur.execute('INSERT INTO menu_drinks VALUES (?, ?, ?, ?)', tuple(data_3.values()))
        base.commit()

async def sql_read_drinks_menu(message):
    for ret in cur.execute('SELECT * FROM menu_drinks').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')

async def sql_del_1():
    return cur.execute('SELECT * FROM menu_pizza').fetchall()

async def sql_delete_pizza(data):
    cur.execute('DELETE FROM menu_pizza WHERE name == ?', (data,))
    base.commit()

async def sql_del_2():
    return cur.execute('SELECT * FROM menu_rolls').fetchall()

async def sql_delete_rolls(data):
    cur.execute('DELETE FROM menu_rolls WHERE name == ?', (data,))
    base.commit()

async def sql_del_3():
    return cur.execute('SELECT * FROM menu_drinks').fetchall()

async def sql_delete_drinks(data):
    cur.execute('DELETE FROM menu_drinks WHERE name == ?', (data,))
    base.commit()
