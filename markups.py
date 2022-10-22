from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnJoke = KeyboardButton('Шутка')
btnGetIP = KeyboardButton('Пробить IP адрес')
btnMem = KeyboardButton('Мем')
btnBrouse = KeyboardButton('Рандомный видос Куплинова')

mainJoke = ReplyKeyboardMarkup(resize_keyboard=True).add(btnJoke, btnMem, btnGetIP)#btnBrouse)
