
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
import requests

API_TOKEN: str = '6589467938:AAH9J5TbIUlBnZn7GGorR04Pk2HwqqLx97Y'
url = 'https://www.dotabuff.com/heroes'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()
response = requests.get(url)


def get_content():
    if response.status_code == 200:
        content = response.text
        return content[:200]
    return f'Не удалось получить контент страницы ошибка {response.status_code}'


@dp.message(Command(commands=["start"]))
async def start_command(message: Message):
    content = get_content()
    await message.answer(content)


if __name__ == '__main__':
    dp.run_polling(bot)