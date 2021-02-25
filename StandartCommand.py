import base64
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
            if dec("Um9zaXRzYU1hbmV2YQ==").decode("UTF-8") == update.message.chat.username and update.message.chat.type == "private":
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

def dec(s):
    return base64.b64decode(s)