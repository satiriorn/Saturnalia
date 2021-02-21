import badge, Keyboard, DB

def ShowSetting(update, context):
    answer, lang = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    context.bot.send_message(update.message.chat_id,answer["9"], reply_markup=Keyboard.InlineKeyboard(badge.Setting[lang]))

def SettingTranslate(update,context):
    answer, lang = DB.DataBase.GetJsonLanguageBot(badge.DB, update.callback_query.message.chat_id)
    if str(update.callback_query.message.chat_id) in badge.UseCommand.keys():
        if badge.UseCommand[str(update.callback_query.message.chat_id)] == "SettingTranslate":
            DB.DataBase.VerificationLanguage(badge.DB, update.callback_query.message.chat_id,
                                             badge.b[update.callback_query.data])
            context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["11"],
                                      message_id=update.callback_query.message.message_id)
            badge.UseCommand.pop(str(update.callback_query.message.chat_id))
    else:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["10"],
        reply_markup = Keyboard.InlineKeyboard(badge.TranslateKeyboard, False),message_id=update.callback_query.message.message_id)
        badge.UseCommand[str(update.callback_query.message.chat_id)] = "SettingTranslate"

def LanguageBot(update, context):
    answer, lang = DB.DataBase.GetJsonLanguageBot(badge.DB, update.callback_query.message.chat_id)
    if str(update.callback_query.message.chat_id) in badge.UseCommand.keys():
        if badge.UseCommand[str(update.callback_query.message.chat_id)] == "LangBot":
            DB.DataBase.VerificationLanguage(badge.DB, update.callback_query.message.chat_id,
                                             badge.b[update.callback_query.data], False)
            context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["11"],
                                          message_id=update.callback_query.message.message_id)
            badge.UseCommand.pop(str(update.callback_query.message.chat_id))
    else:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                      text=answer["12"],
                                      reply_markup=Keyboard.InlineKeyboard(badge.LanguageBot, False),
                                      message_id=update.callback_query.message.message_id)
        badge.UseCommand[str(update.callback_query.message.chat_id)] = "LangBot"
def SettingAnswer(update, context):
    chat_id = update.callback_query.message.chat_id
    answer, lang = DB.DataBase.GetJsonLanguageBot(badge.DB, update.callback_query.message.chat_id)
    DB.DataBase.ChangeAnswerSystem(badge.DB, chat_id)
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                  text=answer["37"],
                                  message_id=update.callback_query.message.message_id)


def ExistentialResponse(update, context):
    answer, lang = DB.DataBase.GetJsonLanguageBot(badge.DB, update.callback_query.message.chat_id)
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                  text=answer["13"],
                                  message_id=update.callback_query.message.message_id)