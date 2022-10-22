import logging
import random
import config
from Joke import joke
import get_brouse as gb
import get_ip as gp
import requests
import markups as mks
import openMems
from openMems import mems
from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup as BS 


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

for i in range(1, 31):
    r = requests.get(f'https://4tob.ru/anekdots/tag/short/page{i}')
    html = BS(r.content, 'html.parser')

    for el in html.select('.section > .q'):
        title = el.select('.text > p')
        if title != []:
            title = title[0].text
            joke.append(title)
        else:
            title = title

def check(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False

CHAT_ID = '@chat_123'

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if check(await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, 
                            f'Привет {message.from_user.first_name}'.format(message.from_user), 
                            reply_markup=mks.mainJoke)
    else:
        await message.answer(f'Для работы с ботом подпишитесь на канал {CHAT_ID}')

@dp.message_handler(commands=['get_ip'])
async def get_ip(message: types.Message):
    await message.answer('Введите IP который хотите пробить\nПример "8,8,1,4"')

    if ',' in message.text:
        ip = list(str(message.text))
        string = ''
        for i in ip:
            if i == ',':
                string += '.'
            else:
                string += i
        await message.answer(gp.get_info_by_ip(string))

@dp.message_handler(commands=['mem'])
async def get_mems(message: types.Message):
    try:
        await bot.send_photo(message.from_user.id, random.choice(openMems.mems))
    except ValueError: 
        print("Error by photo")
        await bot.send_photo(message.from_user.id, random.choice(openMems.mems))

@dp.message_handler(commands=['joke'])
async def joke_by_Jokers(message: types.Message):
    try:
        await message.answer(random.choice(joke))
    except ValueError:
        await message.answer('На сегодня шутки закончились(')

@dp.message_handler(commands=['get_brose'])
async def get_brose(message: types.Message):
    gb.YouTube()

@dp.message_handler()
async def handler(message: types.Message):
    if message.text == 'Рандомный видос Куплинова':
        gb.YouTube()
        
    elif message.text == 'Шутка':
        try:
            await message.answer(random.choice(joke))
        except ValueError:
            await message.answer('На сегодня шутки закончились(')

    elif message.text == "Мем":
        try:
            await bot.send_photo(message.from_user.id, random.choice(openMems.mems))
        except ValueError: 
            print("Error by photo")
            await bot.send_photo(message.from_user.id, random.choice(openMems.mems))

    elif message.text == 'Пробить IP адрес':
        await  message.answer('Введите IP который хотите пробить\nПример "8,8,1,4"')
        if ',' in message.text:
            ip = list(str(message.text))
            string = ''
            for i in ip:
                if i == ',':
                    string += '.'
                else:
                    string += i
            await message.answer(gp.get_info_by_ip(string))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)