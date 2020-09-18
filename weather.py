import requests
def weather(update, context):
    try:
        count = 0
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'q': 'Kharkiv', 'units': 'metric', 'lang': 'uk', 'APPID': 'WeatherToken'})
        data = res.json()
        for i in data['list']:
            date = i['dt_txt']
            temp = '{0:+3.0f}'.format(i['main']['temp'])
            description = i['weather'][0]['description']
            count += 1
            if '12:00:00' in i['dt_txt'] or '18:00:00' in i['dt_txt']:
                context.bot.send_message(update.message.chat_id, '''Дата: ''' + date + '\n'
                                                                               '''Температура:''' + temp + '\n'
                                                                                                           '''Стан неба: ''' + description)
    except Exception:
        context.bot.send_message(update.message.chat_id, 'Погода дала сбой, но я все равно с тобой')

def CurrentWeather(update, context, status=True):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': 'Kharkiv', 'units': 'metric', 'lang': 'uk', 'APPID': 'WeatherToken'})
        data = res.json()
        description_weather = 'Стан погоди, поки ти сидиш вдома: ' + data['weather'][0]['description']
        temp = 'Температура твого міста: ' + str(data['main']['temp'])
        wind = 'Швидкість вітру: ' + str(data['wind']['speed']) + 'м/с'
        text = description_weather + '. ' + temp + '. \n' + wind
        if status == True:
            context.bot.send_message(update.message.chat.id, text)
        else:
            return text
    except Exception:
        context.bot.send_message(update.message.chat_id, "Та що таке, ти створюєш одні проблеми для мене")