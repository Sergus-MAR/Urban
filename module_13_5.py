from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_2 = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
kb_1.add(button_1, button_2)
kb_2.add(button_2)

class UserState (StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет, я бот помогающий твоему здоровью.', reply_markup=kb_1)


@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer('Введите свой возраст:', reply_markup=kb_2)
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:', reply_markup=kb_2)
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:', reply_markup=kb_2)
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    men_calories = round(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    women_calories = round(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161)
    await message.answer(f'Если Вы мужчина - вам требуется {men_calories} коллорий')
    await message.answer(f'Если Вы женщина - вам требуется {women_calories} коллорий', reply_markup=kb_1)
    await state.finish()


@dp.message_handler()
async def set_age(message):
    await message.answer('Для начала работы введите "Расчитать" или нажмите на кнопку', reply_markup=kb_1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

