import asyncio
import logging 
from aiogram import Bot, Dispatcher, types,F
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ContentType
import random
import requests
logging.basicConfig(level=logging.INFO)
bot = Bot(token='7404224531:AAG6DIPxsYc6J06OsTO3ZUZBrp5EZgYcuHE')
dp = Dispatcher()

@dp.message(Command('weather'))
async def start_cammand(message:types.Message):
    await message.answer('Выберите город для погоды?')

@dp.message(F.text)
async def get_weather(message:types.Message):
    city = message.text
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347"
        weather_data = requests.get(url).json()

        temperature = weather_data['main']['temp']
        temperature_feels = weather_data['main']['feels_like']
        wind_speed = weather_data['wind']['speed']
        cloud_cover = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']

        await message.answer(f"🌍 Город: {city}\n"
                             f"🌡 Температура: {temperature}°C\n"
                             f"❄️ Ощущается как: {temperature_feels}°C\n"
                             f"🌤 Погода: {cloud_cover}\n"
                             f"💧 Влажность: {humidity}%\n"
                             f"💨 Скорость ветра: {wind_speed} м/с")
        pass
    except KeyError:
        await message.answer('Не удалось определить город')



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
