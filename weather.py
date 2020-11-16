import requests, os, badge, DB,  telegram.ext

def weather(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat.id)
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

def CurrentWeather(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat.id)
    print(answer)
    try:
        text = WeatherNow(update.message.chat.id)
        context.bot.send_message(update.message.chat.id, text)
    except Exception:
        context.bot.send_message(update.message.chat_id, answer["27"])

def WeatherNow(chat_id):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'q': 'Kharkiv', 'units': 'metric', 'lang': 'uk', 'APPID': os.getenv("WeatherToken")})
    data = res.json()
    description_weather = answer["28"] + data['weather'][0]['description']
    temp = answer["29"] + str(data['main']['temp'])
    wind = answer["30"] + str(data['wind']['speed']) + 'м/с'
    text = description_weather + '. ' + temp + '. \n' + wind
    return text

def StartSysWeather(update,context):
    pass

def WeatherJob(context: telegram.ext.CallbackContext):
    context.bot.send_message(context.job.context, WeatherNow(context.job.context))