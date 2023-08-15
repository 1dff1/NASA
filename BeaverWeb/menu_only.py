from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

API_TOKEN: str = '6589467938:AAH9J5TbIUlBnZn7GGorR04Pk2HwqqLx97Y'


bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


async def set_main_menu(bot: Bot):
    menu = [
        BotCommand(command='/help',
                   description='Помощь'),
        BotCommand(command='/start',
                   description='Начало'),
        BotCommand(command='/contacts',
                   description='Контакты'),
        BotCommand(command='/donat',
                   description='Поддержать бобров бревном')]

    await bot.set_my_commands(menu)

if __name__ == '__main__':
    dp.startup.register(set_main_menu)
    dp.run_polling(bot)