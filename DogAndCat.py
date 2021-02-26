import Url, telegram.ext, datetime, os

class Animal:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            Animal._instance = super(Animal, cls).__new__(cls)
            Animal._mafina = M
            return Animal._instance

    @staticmethod
    def Cat_photo(update, context, answer):
        try:
            Url.Photo(Url.get_url('https://api.thecatapi.com/v1/images/search'), update, context)
        except Exception:
            context.bot.send_message(context.bot_data[update.poll_answer.poll_id], answer["6"])

    @staticmethod
    def Dog_photo(update, context, answer):
        try:
            Url.Photo(Url.get_url('https://random.dog/woof.json'), update, context)
        except Exception:
            context.bot.send_message(context.bot_data[update.poll_answer.poll_id], answer["7"])
    @classmethod
    def StartSysAnimal(self):
        cursor = self._mafina._DB.UsersSysAnimal()
        target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
        target_time = None
        for x in cursor:
            for y in range(len(x)):
                if y + 1 < len(x) and x[y + 1] == True:
                    for i in range(4):
                        if i==0:
                            target_time = datetime.time(hour=9, minute=00, second=25).replace(tzinfo=target_tzinfo)
                        elif i == 1:
                            target_time = datetime.time(hour=13, minute=00, second=25).replace(tzinfo=target_tzinfo)
                        elif i == 2:
                            target_time = datetime.time(hour=18, minute=00, second=25).replace(tzinfo=target_tzinfo)
                        else:
                            target_time = datetime.time(hour=22, minute=00, second=25).replace(tzinfo=target_tzinfo)
                        self._mafina.jobchat[str(x[y])] = self._mafina.job.run_daily(self.AnimalJob, target_time, context=x[y])
    @classmethod
    def SysAnimal(self, update, context, answer, chat_id):
        cursor = self._mafina._DB.UsersSysAnimal()
        target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
        target_time = datetime.time(hour=9, minute=00, second=25).replace(tzinfo=target_tzinfo)
        NewUser = True
        for x in cursor:
            for y in range(len(x)):
                if str(x[y]) == str(chat_id):
                    state = (lambda x, y: True if x[y+1] == False else False) (x,y)
                    self._mafina._DB.UpdateSysAnimal(chat_id, state)
                    if str(chat_id) in self._mafina.jobchat.keys() and state==False:
                        self._mafina.jobchat[str(chat_id)].schedule_removal()
                        self._mafina.jobchat.pop(str(chat_id))
                        context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                                      message_id=update.callback_query.message.message_id)
                        NewUser = False
                        break
                    else:
                        self._mafina.jobchat[str(chat_id)] = self._mafina.job.run_daily(self.AnimalJob, target_time, context=chat_id)
                        context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                                      message_id=update.callback_query.message.message_id)
                        NewUser = False
                    break
        if NewUser:
            self._mafina._DB.InsertSysAnimal(update.callback_query.message.chat_id, True)
            self._mafina.jobchat[str(chat_id)] = self._mafina.job.run_daily(self.AnimalJob, target_time, context=chat_id)
            context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                          message_id=update.callback_query.message.message_id)

    @staticmethod
    def AnimalJob(context: telegram.ext.CallbackContext):
        x = Animal._mafina._DB.GetCountAnimal(context.job.context)
        fileID = Animal._mafina._DB.GetFileId(x)
        if x==1:
            context.bot.send_message(context.job.context,"Увімкнута система котиків.\nКотики будуть надсилатися у заданий час два рази на день, якщо вони вам не потрібні або заважають, можете вимкнути через налаштування бота.\n Якщо немає клавіатури бота -> /Help.\n Якщо клавіатура не потрібна-> /SettingBot.\n Кількість котиків на даний момент вистачає на півроку.\n Насолоджуйтесь.\n Якщо у вас є непогана кількість унікальних мімімішних котиків пишіть @Satiriorn.")
        file = context.bot.getFile(fileID)
        title = ("{0}.gif").format(context.job.context)
        file.download(title)
        try:
            context.bot.send_video(context.job.context, open(title, 'rb'))
        except Exception:
            context.bot.send_animation(context.job.context, open(title, 'rb'))
        Animal._mafina._DB.UpCountAnimal(context.job.context)
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), title))