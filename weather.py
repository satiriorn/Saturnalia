import requests, os, badge, DB, telegram.ext, datetime

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

def StartSysWeather():
    cursor = DB.DataBase.UsersSysWeather(badge.DB)
    target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
    target_time = datetime.time(hour=9, minute=00, second=20).replace(tzinfo=target_tzinfo)
    for x in cursor:
        for y in range(len(x)):
            if y+1< len(x) and x[y+1] == True:
                badge.jobchat[str(x[y])] = badge.job.run_daily(WeatherJob, target_time, context=x[y])

def StateWeather(update, context):
    chat_id = update.callback_query.message.chat_id
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    cursor = DB.DataBase.UsersSysWeather(badge.DB)
    target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
    target_time = datetime.time(hour=9, minute=00, second=00).replace(tzinfo=target_tzinfo)
    NewUser = True
    for x in cursor:
        for y in range(len(x)):
            if str(x[y]) == str(chat_id):
                state = (lambda x, y: True if x[y+1] == False else False) (x,y)
                DB.DataBase.UpdateSysWeather(badge.DB, chat_id, state)
                if str(chat_id) in badge.jobchat.keys() and state==False:
                    badge.jobchat[str(chat_id)].schedule_removal()
                    badge.jobchat.pop(str(chat_id))
                    context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                                  message_id=update.callback_query.message.message_id)
                    NewUser = False
                    break
                else:
                    badge.jobchat[str(chat_id)] = badge.job.run_daily(WeatherJob, target_time, context=chat_id)
                    context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                                  message_id=update.callback_query.message.message_id)
                    NewUser = False
                break
    if NewUser:
        print('dsakfhadskjf')
        DB.DataBase.InsertSysWeather(badge.DB, update.callback_query.message.chat_id, True)
        badge.jobchat[str(chat_id)] = badge.job.run_daily(WeatherJob, target_time, context=chat_id)
        context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                      message_id=update.callback_query.message.message_id)

def WeatherJob(context: telegram.ext.CallbackContext):
    context.bot.send_message(context.job.context, WeatherNow(context.job.context))