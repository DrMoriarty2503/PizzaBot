from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

bot = Bot(token='5527815433:AAHy9gMVGIndpjUDV8vuPKq-LAA7_PypCrQ')
dp=Dispatcher(bot, storage=storage)
