class SettingMafina:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            SettingMafina._instance = super(SettingMafina, cls).__new__(cls)
            SettingMafina._mafina = M
            return SettingMafina._instance

    @classmethod
    def ShowSetting(self, update, context, answer, chat_id, lang):
        context.bot.send_message(chat_id, answer["9"],
                                 reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.Setting[lang]))

    @classmethod
    def SettingTranslate(self, update, context, answer, chat_id):
        if chat_id in self._mafina.UseCommand.keys():
            if self._mafina.UseCommand[chat_id] == "SettingTranslate":
                self._mafina._DB.VerificationLanguage(chat_id, self._mafina._keyboard.b[update.callback_query.data])
                context.bot.edit_message_text(chat_id=chat_id, text=answer["11"],
                                          message_id=update.callback_query.message.message_id)
                self._mafina.UseCommand.pop(chat_id)
        else:
            context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["10"],
            reply_markup = self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.TranslateKeyboard, False),message_id=update.callback_query.message.message_id)
            self._mafina.UseCommand[chat_id] = "SettingTranslate"

    @classmethod
    def LanguageBot(self, update, context, answer, chat_id):
        if chat_id in self._mafina.UseCommand.keys():
            if self._mafina.UseCommand[str(update.callback_query.message.chat_id)] == "LangBot":
                self._mafina._DB.VerificationLanguage(chat_id, self._mafina._keyboard.b[update.callback_query.data], False)
                context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["11"],
                                              message_id=update.callback_query.message.message_id)
                self._mafina.UseCommand.pop(chat_id)
        else:
            context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                          text=answer["12"],
                                          reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.LanguageBot, False),
                                          message_id=update.callback_query.message.message_id)
            self._mafina.UseCommand[chat_id] = "LangBot"

    @classmethod
    def SettingAnswer(self, update, context, answer, chat_id):
        self._mafina._DB.ChangeAnswerSystem(chat_id)
        context.bot.edit_message_text(chat_id=chat_id, text=answer["37"], message_id=update.callback_query.message.message_id)

    @staticmethod
    def ExistentialResponse(update, context, answer, chat_id):
        context.bot.edit_message_text(chat_id=chat_id, text=answer["13"], message_id=update.callback_query.message.message_id)