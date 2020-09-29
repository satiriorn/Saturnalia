import requests, os, badge, DB

def weather(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
    try:
        count = 0
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'q': 'Kharkiv', 'units': 'metric', 'lang': 'uk', 'APPID': os.getenv("WeatherToken")})
        data = res.json()
        for i in data['list']:
            date = i['dt_txt']
            temp = '{0:+3.0f}'.format(i['main']['temp'])
            description = i['weather'][0]['description']
            count += 1
            if '12:00:00' in i['dt_txt'] or '18:00:00' in i['dt_txt']:
                context.bot.send_message(update.message.chat_id, answer["26"].format(date,temp,description))
    except Exception:
        context.bot.send_message(update.message.chat_id, answer["27"])

def CurrentWeather(update, context, status=True):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': 'Kharkiv', 'units': 'metric', 'lang': 'uk', 'APPID': os.getenv("WeatherToken")})
        data = res.json()
        description_weather = answer["28"] + data['weather'][0]['description']
        temp = answer["29"] + str(data['main']['temp'])
        wind = answer["30"] + str(data['wind']['speed']) + 'м/с'
        text = description_weather + '. ' + temp + '. \n' + wind
        return (lambda status:status if context.bot.send_message(update.message.chat.id, text)else text)(status)
    except Exception:
        context.bot.send_message(update.message.chat_id, )