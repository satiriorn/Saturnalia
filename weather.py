import requests, os, telegram.ext, datetime
class Weather(object):
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            Weather._instance = super(Weather, cls).__new__(cls)
            Weather._mafina = M
            return Weather._instance

    @classmethod
    def weather(self, update, context, answer):
        try:
            context.bot.send_message(update.message.chat_id, self.PrognosisWeather(answer))
        except Exception:
            context.bot.send_message(update.message.chat_id, answer["27"])

    @staticmethod
    def PrognosisWeather(answer, OneDay = True):
        text = ""
        count = 0
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'q': 'Kharkiv', 'units': 'metric', 'lang': 'uk', 'APPID': os.getenv("WeatherToken")})
        data = res.json()
        for i in data['list']:
            date = i['dt_txt']
            temp = '{0:+3.0f}'.format(i['main']['temp'])
            description = i['weather'][0]['description']
            if ' 09:00:00' in i['dt_txt'] or '12:00:00' in i['dt_txt'] or '18:00:00' in i['dt_txt'] or '21:00:00'in i['dt_txt']:
                if OneDay and count == 4:
                    break
                else:
                    text += answer["26"].format(date, temp, description)+'. \n\n'
                    count += 1
        return text

    @classmethod
    def WeatherNow(self, chat_id):
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': 'Kharkiv', 'units': 'metric', 'lang': 'uk', 'APPID': os.getenv("WeatherToken")})
        data = res.json()
        answer, lang = self._mafina._DB.GetJsonLanguageBot(chat_id)
        description_weather = answer["28"] + data['weather'][0]['description']
        temp = answer["29"] + str(data['main']['temp'])
        wind = answer["30"] + str(data['wind']['speed']) + 'м/с'
        text = description_weather + '. ' + temp + '. \n' + wind+'\n\n'
        target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
        now = datetime.datetime.now().replace(tzinfo=target_tzinfo)
        print(now)
        if "10:00" in str(now) or "08:00" in str(now):
            text += answer["38"]+self.PrognosisWeather(answer, True)
        return text

    @classmethod
    def CurrentWeather(self, update, context, answer):
        try:
            text = self.WeatherNow(update.message.chat.id)
            context.bot.send_message(update.message.chat.id, text)
        except Exception:
            context.bot.send_message(update.message.chat_id, answer["27"])

    @classmethod
    def StartSysWeather(self):
        cursor = self._mafina._DB.UsersSysWeather()
        target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
        target_time = datetime.time(hour=9, minute=00, second=20).replace(tzinfo=target_tzinfo)
        for x in cursor:
            for y in range(len(x)):
                if y + 1 < len(x) and x[y + 1] == True:
                    for i in range(3):
                        if i == 0:
                            target_time = datetime.time(hour=10, minute=00, second=00).replace(tzinfo=target_tzinfo)
                        elif i == 1:
                            target_time = datetime.time(hour=15, minute=00, second=00).replace(tzinfo=target_tzinfo)
                        else:
                            target_time = datetime.time(hour=18, minute=00, second=00).replace(tzinfo=target_tzinfo)
                        self._mafina.jobchat[str(x[y])] = self._mafina.job.run_daily(self.WeatherJob, target_time, context=x[y])

    @staticmethod
    def WeatherJob(context: telegram.ext.CallbackContext):
        context.bot.send_message(context.job.context, Weather.WeatherNow(context.job.context))

    @classmethod
    def StateWeather(self, update, context, answer, chat_id):
        cursor = self._mafina._DB.UsersSysWeather()
        target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
        target_time = datetime.time(hour=9, minute=00, second=00).replace(tzinfo=target_tzinfo)
        NewUser = True
        for x in cursor:
            for y in range(len(x)):
                if str(x[y]) == str(chat_id):
                    state = (lambda x, y: True if x[y + 1] == False else False)(x, y)
                    self._mafina._DB.UpdateSysWeather(chat_id, state)
                    if str(chat_id) in self._mafina.jobchat.keys() and state == False:
                        self._mafina.jobchat[str(chat_id)].schedule_removal()
                        self._mafina.jobchat.pop(str(chat_id))
                        context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                                      message_id=update.callback_query.message.message_id)
                        NewUser = False
                        break
                    else:
                        self._mafina.jobchat[str(chat_id)] = self._mafina.job.run_daily(self.WeatherJob, target_time, context=chat_id)
                        context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                                      message_id=update.callback_query.message.message_id)
                        NewUser = False
                    break
        if NewUser:
            self._mafina._DB.InsertSysWeather(update.callback_query.message.chat_id, True)
            self._mafina.jobchat[str(chat_id)] = self._mafina.job.run_daily(self.WeatherJob, target_time, context=chat_id)
            context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                          message_id=update.callback_query.message.message_id)