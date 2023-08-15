from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message 
import random


API_TOKEN: str = '6589467938:AAH9J5TbIUlBnZn7GGorR04Pk2HwqqLx97Y'
id_users: dict = {
}
data_base: dict = {
    'in_game': False,
    'correct_number': None,
    'attempts': None,
    'games': 0,
    'wins': 0
}

attempts: int = 5

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


def generate_random_number() -> int:
    return random.randint(1,100)


@dp.message(Command(commands=["close"]))
async def start_command(message: Message):
    await message.answer('Вы покинули игру:(')
    data_base['in_game'] == False

@dp.message(Command(commands=["start"]))
async def start_command(message: Message):
    if message.from_user.id not in id_users:
        id_users[message.from_user.id] = data_base
    print(id_users[message.from_user.id])
    await message.answer('Напишите /play чтобы начать игру \nНапишите /help чтобы узнать правила')
    


@dp.message(Command(commands=["play"]))
async def start_command(message: Message):
    data_base['in_game'] = True
    data_base['correct_number'] = generate_random_number()
    data_base['attempts'] = attempts
    await message.answer('Угадайте число от 1 до 100, которое я загадал. У вас есть 5 попыток')

@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    if data_base['in_game'] == True:
        if int(message.text) == data_base['correct_number']:
            await message.answer('Ты угадал! Молодец!')
            data_base['games'] += 1
            data_base['wins'] += 1
            data_base['in_game'] = False

        if int(message.text) < data_base['correct_number']:
            await message.answer('Больше!') 
            data_base['attempts'] -= 1
            print(data_base['attempts'])

        if int(message.text) > data_base['correct_number']:
            await message.answer('Меньше!') 
            data_base['attempts'] -= 1
            print(data_base['attempts'])
        
        if data_base['attempts'] == 0:
            await message.answer('Ты проиграл!')
            data_base['games'] += 1
            data_base['in_game'] = False
    
    else:
        await message.answer('Зайди в игру чтобы писать числа!')

@dp.message(Command(commands=["help"]))
async def start_command(message: Message):
    await message.answer('Вы должны угадать число от 1 до 100 за пять попыток \n '
                         'Команды: \n'
                         '/close - выйти \n '
                         '/play - играть \n '
                         '/stat - статистика \n '
                         '/help - помощь \n '
                         '/start - начать \n ')


@dp.message(Command(commands=['stat']))
async def process_stat_command(message: Message):
    await message.answer(f'Всего игр сыграно: {id_users[message.from_user.id]["games"]}\n'
                         f'Игр выиграно: {id_users[message.from_user.id]["wins"]}')


if __name__ == '__main__':
    dp.run_polling(bot)
