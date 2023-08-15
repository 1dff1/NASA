from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
import requests
import random

API_KEY_NASA = 'gzqsdkV4kxwPsuFQ10VTUPhja4n8QDIMCQSvOkbp'
API_TOKEN: str = '6589467938:AAH9J5TbIUlBnZn7GGorR04Pk2HwqqLx97Y'

in_rover = False
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()
    

async def set_main_menu(bot: Bot):
    menu = [
        BotCommand(command='/help',
                   description='Список команд'),
        BotCommand(command='/start',
                   description='Начало'),
        BotCommand(command='/donat',
                   description='Поддержать бобров бревном 89198900641'),
        BotCommand(command='/image',
                   description='Получить фото с марса'),
        BotCommand(command='/',
                   description='Получить фото с марса')]
    await bot.set_my_commands(menu)

    
@dp.message(Command(commands=["start"]))
async def start_command(message: Message):
    await message.answer('Напишите /help чтобы узнать подробнее о роверах')


@dp.message(Command(commands=["help"]))
async def start_command(message: Message):
    await message.answer('/start - начать\n'
                         '/help - помощь\n'
                         '/image - фото с марса\n'
                         '/donat - поддержка создателя и бобров')


@dp.message(Command(commands=["image"]))
async def start_command(message: Message):
    await message.answer('Выбор:\n'
                         '/curiosity\n'
                         '/spirit\n'
                         '/opportunity\n')


@dp.message(Command(commands=["curiosity"]))
async def start_command(message: Message):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={random.randint(1,1000)}&api_key={API_KEY_NASA}"
    response = requests.get(url)
    if response.status_code == 200:
        photo_url = response.json()["photos"][random.randint(1,50)]["img_src"]
        await message.answer(photo_url)
    await message.answer('Количество запросов превышено')


@dp.message(Command(commands=["spirit"]))
async def start_command(message: Message):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos?sol={random.randint(1,1000)}&api_key={API_KEY_NASA}"
    response = requests.get(url)
    if response.status_code == 200:
        photo_url = response.json()["photos"][random.randint(1,10)]["img_src"]
        await message.answer(photo_url)
    await message.answer('Количество запросов превышено')


@dp.message(Command(commands=["opportunity"]))
async def start_command(message: Message):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?sol={random.randint(1,1000)}&api_key={API_KEY_NASA}"
    response = requests.get(url)
    if response.status_code == 200:
        photo_url = response.json()["photos"][random.randint(1,10)]["img_src"]
        await message.answer(photo_url)
    await message.answer('Количество запросов превышено')


@dp.message(Command(commands=["donat"]))
async def start_command(message: Message):
    await message.answer('Кидать деньги сюда 89198900641 и сюда https://urbananimal.ru/beaver?ysclid=llam65ynnb368640553')


if __name__ == '__main__':
    dp.startup.register(set_main_menu)
    dp.run_polling(bot)