from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api =''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@ dp.message_handler(commands=['start'])
async def all_messanges(messange):
    #print('Привет! Я бот помогающий твоему здоровью.')
    await messange.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def start(messange):
    #print('ведите команду /start, чтобы начать общение.')
    await messange.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)