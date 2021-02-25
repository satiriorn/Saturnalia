import telegram.ext, Url, datetime

class Meme:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            Meme._instance = super(Meme, cls).__new__(cls)
            Meme._mafina = M
            return Meme._instance
    @staticmethod
    def Get_meme(update, context,  answer):
        try:
            Url.Photo(Url.get_url('https://meme-api.herokuapp.com/gimme'), update, context)
        except Exception:
            context.bot.send_message(update.message.chat_id, answer["3"])
    @classmethod
    def CountMem(self, update, context, answer, lang):
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["64"],
                                      reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.CountMeme[lang]),
                                      message_id=update.callback_query.message.message_id)
        self._mafina.UseCommand[str(update.callback_query.message.chat_id)] = "MemeChange"

    @classmethod
    def StartSystemMeme(self):
        cursor = self._mafina._DB.UsersSysMeme()
        for x in cursor:
            for y in range(len(x)):
                if y+2< len(x) and x[y+2]==1:
                    self._mafina.jobchat[str(x[y])]=self._mafina.job.run_repeating(self.MemeChatGroup, interval=int(x[y+1]), first= 0,
                                        context=int(x[y]))

    @classmethod
    def MoreMeme(self, update, context):
        value = {"0":"0","1":"900","2":"1800", "3":"3600", "4":"7200"}
        chat_id = update.callback_query.message.chat_id
        cursor = self._mafina._DB.UsersSysMeme()
        NewUser = True
        for x in cursor:
            for y in range(len(x)):
                if y+2< len(x) and x[y+2]==1:
                    if str(x[y])==str(chat_id):
                        x[y]
                        NewUser = False
        if value[str(update.callback_query.data)] != "0":
            if str(chat_id) in Mafina.Mafina.jobchat.keys():
                Mafina.Mafina.jobchat[str(chat_id)].schedule_removal()
                Mafina.Mafina.jobchat[str(chat_id)] = Mafina.Mafina.job.run_repeating(self.MemeChatGroup, interval=int(value[str(update.callback_query.data)]), first=datetime.datetime.now(),
                                        context=chat_id)
                self._mafina._DB.UpdateSysMeme(chat_id, True, int(value[str(update.callback_query.data)]))
            elif NewUser == True:
                self._mafina.jobchat[str(chat_id)] =self._mafina.job.run_repeating(self.MemeChatGroup, interval=int(value[str(update.callback_query.data)]), first=datetime.datetime.now(),
                                    context=chat_id)
                self._mafina._DB.InsertSysMeme(chat_id, True, int(value[str(update.callback_query.data)]))
        else:
            self._mafina.jobchat[str(chat_id)].schedule_removal()
            self._mafina._DB.UpdateSysMeme(chat_id, False, 0)
            self._mafina.jobchat.pop(str(chat_id))
        context.bot.edit_message_text(chat_id=chat_id, text=self._mafina._keyboard.CountMeme[int(update.callback_query.data)], message_id=update.callback_query.message.message_id)
        self._mafina.UseCommand.pop(str(chat_id))
    @staticmethod
    def MemeChatGroup(context: telegram.ext.CallbackContext):
        url = Url.get_url('https://meme-api.herokuapp.com/gimme')
        if Url.is_image(url):
            context.bot.send_photo(context.job.context, url)
        elif Url.is_animation(url):
            context.bot.send_animation(context.job.context, url)