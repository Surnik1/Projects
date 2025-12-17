import telebot
import requests
from telebot import types
tg_token = 'TOKEN_FROM_BOTFATHER'
weather_token = 'TOKEN_FROM_http://api.weatherapi.com'

bot = telebot.TeleBot(tg_token)

def weather_today(city):
    try:
        url = (
            f'http://api.weatherapi.com/v1/current.json?key={weather_token}&q={city}&aqi=no'
        )
        response = requests.get(url)
        data = response.json()

        if 'error' in data:
            return 'City not found'

        location = data['location']['name']
        country = data['location']['country']
        current = data['current']
        cond = current['condition']['text']
        temp = current['temp_c']
        hum=current['humidity']
        wind =current['wind_kph']
        weather_rep = (
            f'📢{location}, {country}\n'
            f'☁️ {cond}\n'
            f'🌡️ Temperature: {temp}°C\n'
            f'💧 Humidity: {hum}%\n'
            f'🍃 Wind: {wind} km/h'
        )

        return weather_rep
    except:
        return 'Error getting weather'

def weather_5days(city):
    try:
        url = (
            f'http://api.weatherapi.com/v1/forecast.json?key={weather_token}&q={city}&days=5'
        )
        response = requests.get(url)
        data = response.json()

        if 'error' in data:
            return ' City not found'

        location = data['location']['name']
        country = data['location']['country']

        text = f'🗓️ 5-Day forecast for {location}, {country}\n\n'

        for day in data['forecast']['forecastday']:
            date = day['date']
            cond = day['day']['condition']['text']
            tempmi = day['day']['mintemp_c']
            tempma =day['day']['maxtemp_c']
            rain = day['day']['daily_chance_of_rain']
            text += (
                f'📅 {date}\n'
                f'☁️ {cond}\n'
                f'🌡️ {tempmi}°C - {tempma}°C\n'
                f'☔ Rain chance: {rain}%\n\n'
            )

        return text

    except:
        return ' Error getting forecast'

reply_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
reply_kb.add(
    types.KeyboardButton('Astana'),
    types.KeyboardButton('Almaty'),
    types.KeyboardButton('Taldykorgan')
)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        'Welcome! 😊\
        \nI can help you check the weather in any city around the world 🌍\
        \nJust send me the city name!',
        reply_markup=reply_kb
    )


@bot.message_handler(func=lambda message: True)
def send_weather(message):
    city = message.text.strip()

    weather = weather_today(city)

    inline_kb = types.InlineKeyboardMarkup()
    inline_kb.add(
        types.InlineKeyboardButton(
            '📅 Forecast for 5 days',
            callback_data=f'forecast_5:{city}'
        )
    )

    bot.reply_to(message, weather, reply_markup=inline_kb)

@bot.callback_query_handler(func=lambda call: call.data.startswith('forecast_5'))
def callback(call):
    city = call.data.split(':')[1]
    forecast = weather_5days(city)

    bot.send_message(call.message.chat.id, forecast)
    bot.answer_callback_query(call.id)

bot.infinity_polling()
