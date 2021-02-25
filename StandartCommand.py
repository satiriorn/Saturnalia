import base64, time
class StandartCommand:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            StandartCommand._instance = super(StandartCommand, cls).__new__(cls)
            StandartCommand._mafina = M
            return StandartCommand._instance
    @classmethod
    def start(self, update, context, answer, chat_id):
        try:
            first_name = update.message.chat.first_name
            if update.message.chat.type == "private":
                self._mafina._DB.CheckUser(first_name, update.message.chat.username, chat_id,
                                            update.message.from_user.language_code, update.message.chat.type)
            if self.dec("Um9zaXRzYU1hbmV2YQ==").decode("UTF-8") == update.message.chat.username and update.message.chat.type == "private":
                self._mafina.Dologusha.start(update, context)
            else:
                self._mafina._DB.CheckUser(update.message.chat.title, update.message.chat.username, chat_id,
                update.message.from_user.language_code, update.message.chat.type)
            context.bot.send_message(chat_id, answer["start"], reply_markup =self._mafina._keyboard.InitKeyboard(self._mafina._keyboard.MainKeyboard))
        except Exception:
            context.bot.send_message(update.message.chat_id, "щось пішло не так")
    @classmethod
    def help(self, update, context, answer):
        context.bot.send_message(update.message.chat_id, answer["8"],
                                 reply_markup = self._mafina._keyboard.InitKeyboard(self._mafina._keyboard.MainKeyboard))

    @classmethod
    def Rest(self, update, context, answer, lang, chat_id, status=True):
        self._mafina.Mafina.UseCommand[chat_id] = "Rest"
        if status:
            context.bot.send_message(chat_id=chat_id, text=answer["65"],
                                     reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.RestButton[lang], False))
        else:
            context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                          text=self._mafina._keyboard.RestButton[lang][0],
                                          message_id=update.callback_query.message.message_id)
            for i in range(6):
                if i == 0: time.sleep(5)
                context.bot.send_message(chat_id=chat_id, text=answer["66"])
                time.sleep(5)
                context.bot.send_message(chat_id=chat_id, text=answer["67"])
                time.sleep(5)
            context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=answer["68"])
            self._mafina.UseCommand.pop(chat_id)

    @staticmethod
    def dec(s):
        return base64.b64decode(s)