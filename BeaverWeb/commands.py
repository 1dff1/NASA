from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message 
import random


API_TOKEN: str = '6589467938:AAH9J5TbIUlBnZn7GGorR04Pk2HwqqLx97Y'


bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def start_command(message: Message):
    await message.answer('Напишите /choice чтобы было')


@dp.message(Command(commands=["choice"]))
async def start_command(message: Message):
    await message.answer(random.choice(['Да', 'Нет', 'Возможно', 'Тошно тошно', 'Бобры и Шлепы лучшие']))


@dp.message(Command(commands=["help"]))
async def start_command(message: Message):
    await message.answer('Напишите /start')


if __name__ == '__main__':
    dp.run_polling(bot)