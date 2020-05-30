import requests, badge

def weather(bot, update):
    try:
        count = 0
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'q': 'Kharkiv', 'units': 'metric', 'lang': 'ru', 'APPID': badge.appid})
        data = res.json()
        for i in data['list']:
            date = i['dt_txt']
            temp = '{0:+3.0f}'.format(i['main']['temp'])
            description = i['weather'][0]['description']
            count += 1
            if '12:00:00' in i['dt_txt'] or '18:00:00' in i['dt_txt']:
                bot.send_message(update.message.chat_id, '''Дата: ''' + date + '\n'
                                                                               '''Температура:''' + temp + '\n'
                                                                                                           '''Что будет за окном: ''' + description)
    except Exception:
        bot.send_message(update.message.chat_id, 'Погода дала сбой, но я все равно с тобой')

def CurrentWeather(bot, update, status=True):
    try:
        #jopa
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': 'Kharkiv', 'units': 'metric', 'lang': 'ru', 'APPID': badge.appid})
        data = res.json()
        description_weather = 'Текущее состояния погоды, пока ты сидишь дома: ' + data['weather'][0]['description']
        temp = 'Температура в твоем отсталом городе: ' + str(data['main']['temp'])
        wind = 'Скорость ветерка между ног: ' + str(data['wind']['speed']) + 'м/с'
        text = description_weather + '. ' + temp + '. \n' + wind
        #if status == True:
        #    update.message.text = text
        #    voice(bot, update)
        #else:
        bot.send_message(update.message.chat.id, text)
        return text

    except Exception:
        bot.send_message(update.message.chat_id,
                         'Ааа, со мной что-то не так, пытаюсь дышать в этой грязной и огромной сети...')