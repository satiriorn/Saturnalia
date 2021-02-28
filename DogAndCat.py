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
        times = [12, 9, 22, 18]
        for x in cursor:
            for y in range(len(x)):
                if y + 2 < len(x):
                    for i in range(x[y+2]):
                            target_time = datetime.time(hour=times[i], minute=00, second=25).replace(tzinfo=target_tzinfo)
                            self._mafina.jobchat[str(x[y])] = self._mafina.job.run_daily(self.AnimalJob, target_time,
                                                                                 context=x[y])

    @classmethod
    def SysAnimal(self, update, context, answer, lang, chat_id):
        if chat_id in self._mafina.UseCommand.keys():
            cursor = self._mafina._DB.CheckUserInJob(chat_id)
            target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
            target_time = datetime.time(hour=9, minute=00, second=25).replace(tzinfo=target_tzinfo)
            NewUser = True
            for x in cursor:
                    if str(x[0]) == str(chat_id):
                        #self._mafina._DB.UpdateSysAnimal(chat_id, state)
                        if str(chat_id) in self._mafina.jobchat.keys() and state==False:
                            self._mafina.jobchat[str(chat_id)].schedule_removal()
                            self._mafina.jobchat.pop(str(chat_id))
                            context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                                          message_id=update.callback_query.message.message_id)
                            NewUser = False
                        else:
                            self._mafina.jobchat[str(chat_id)] = self._mafina.job.run_daily(self.AnimalJob, target_time, context=chat_id)
                            context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                                          message_id=update.callback_query.message.message_id)
                            NewUser = False
            if NewUser:
                self._mafina._DB.InsertSysAnimal(update.callback_query.message.chat_id, True)
                self._mafina.jobchat[str(chat_id)] = self._mafina.job.run_daily(self.AnimalJob, target_time, context=chat_id)
                context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                              message_id=update.callback_query.message.message_id)
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["56"],
                                          message_id=update.callback_query.message.message_id)
            context.bot.edit_message_reply_markup(chat_id, reply_markup=self._mafina._keyboard.InlineKeyboard(
                self._mafina._keyboard.AnimalButton[lang], False),
                                                  message_id=update.callback_query.message.message_id)
            self._mafina.UseCommand[str(chat_id)] = "ChangeSysAnimal"

    @staticmethod
    def AnimalJob(context: telegram.ext.CallbackContext):
        x = Animal._mafina._DB.GetCountAnimal(context.job.context)
        fileID = Animal._mafina._DB.GetFileId(x)
        file = context.bot.getFile(fileID)
        title = ("{0}.gif").format(context.job.context)
        file.download(title)
        try:
            context.bot.send_video(context.job.context, open(title, 'rb'))
        except Exception:
            context.bot.send_animation(context.job.context, open(title, 'rb'))
        Animal._mafina._DB.UpCountAnimal(context.job.context)
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), title))