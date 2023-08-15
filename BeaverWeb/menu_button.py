from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


API_TOKEN: str = '6589467938:aAH9J5TbIUlBnZn7GGorR04Pk2HwqqLx97Y'


bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


button_yes: KeyboardButton = KeyboardButton(text='Да')
button_no: KeyboardButton = KeyboardButton(text='Нет')

button_1: KeyboardButton = KeyboardButton(text='1')
button_2: KeyboardButton = KeyboardButton(text='2')
button_3: KeyboardButton = KeyboardButton(text='3')

keyboard_noandyes: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_yes, button_no]])

keyboard_num: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2, button_3]])


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Хотите поучавствовать в истории?',
                         reply_markup=keyboard_noandyes,)
    
@dp.message(F.text.lower().in_(['да']))
async def process_dog_answer(message: Message):
    await message.answer(text='Вы проснулись в темной комнате.\n'
                        'Ваши глаза постепенно привыкают к темноте, и вы замечаете маленькую лампочку, которая светится в углу.\n'
                        'В комнате также есть три двери: одна красная, одна синяя и одна зеленая. \n'
                        'Что будете делать?!\n\n'
                        '1 Выбрать красную дверь. \n'
                        '2 Выбрать синюю дверь. \n'
                        '3 Выбрать зеленую дверь. \n\n'
                        'Выберите цифру, соответствующую вашему выбору.',
                         reply_markup=keyboard_num)

@dp.message(F.text.lower().in_(['1']))
async def process_dog_answer(message: Message):
    await message.answer(text='Вы решаете выбрать красную дверь.\n'
                        'Подойдя к ней, вы замечаете, что дверь заперта. На ее поверхности есть записка с надписью: "Найдите ключ в ящике справа от двери, чтобы открыть ее".'
                        'Что будете делать?!\n\n'
                        '1 Попробовать открыть ящик справа от двери и найти ключ.\n'
                        '2 Исследовать синюю дверь.\n\n'
                        'Выберите цифру, соответствующую вашему выбору.',
                         reply_markup=keyboard_num)
    

@dp.message(F.text.lower().in_(['2']))
async def process_dog_answer(message: Message):
    await message.answer(text='Вы решаете исследовать синюю дверь. Она открывается без проблем, и перед вами предстает выбор между двумя путями: лестница ведет вниз, а дверь направо ведет в темную комнату.\n'
                        'У вас есть два варианта действий:'
                        'Что будете делать?!\n\n'
                        '1 Спуститься по лестнице.\n'
                        '2 Пройти через дверь направо в темную комнату. \n\n'
                        'Выберите цифру, соответствующую вашему выбору.',
                         reply_markup=keyboard_num)


@dp.message(F.text.lower().in_(['3']))
async def process_dog_answer(message: Message):
    await message.answer(text='Вы решились исследовать зеленую дверь. Она открывается без каких-либо проблем, и перед вами открывается новая комната. Что бы вы хотели сделать дальше?\n'
                        'У вас есть два варианта действий:'
                        'Что будете делать?!\n\n'
                        '1 Выйти.\n'
                        '2 Остаться. \n\n'
                        'Выберите цифру, соответствующую вашему выбору.',
                         reply_markup=keyboard_num)


if __name__ == '__main__':
    dp.run_polling(bot)

