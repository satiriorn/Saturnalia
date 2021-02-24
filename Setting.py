def ShowSetting(update, context, answer, lang, Mafina):
    context.bot.send_message(update.message.chat_id, answer["9"], reply_markup=Mafina.Keyboard.InlineKeyboard(Mafina.Keyboard.Setting[lang]))

def SettingTranslate(update, context, answer, Mafina, chat_id):
    if chat_id in Mafina.mafina.UseCommand.keys():
        if Mafina.Mafina.UseCommand[str(update.callback_query.message.chat_id)] == "SettingTranslate":
            Mafina.DB.DataBase.VerificationLanguage(Mafina.mafina.DB, update.callback_query.message.chat_id,
                                             Mafina.Keyboard.b[update.callback_query.data])
            context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["11"],
                                      message_id=update.callback_query.message.message_id)
            Mafina.Mafina.UseCommand.pop(str(update.callback_query.message.chat_id))
    else:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["10"],
        reply_markup = Mafina.Keyboard.InlineKeyboard(Mafina.Keyboard.TranslateKeyboard, False),message_id=update.callback_query.message.message_id)
        Mafina.mafina.UseCommand[str(update.callback_query.message.chat_id)] = "SettingTranslate"

def LanguageBot(update, context, answer):
    if str(update.callback_query.message.chat_id) in Mafina.Mafina.UseCommand.keys():
        if Mafina.Mafina.UseCommand[str(update.callback_query.message.chat_id)] == "LangBot":
            DB.DataBase.VerificationLanguage(Mafina.Mafina.DB, update.callback_query.message.chat_id,
                                             Mafina.Mafina.b[update.callback_query.data], False)
            context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["11"],
                                          message_id=update.callback_query.message.message_id)
            Mafina.Mafina.UseCommand.pop(str(update.callback_query.message.chat_id))
    else:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                      text=answer["12"],
                                      reply_markup=Keyboard.InlineKeyboard(Mafina.Mafina.LanguageBot, False),
                                      message_id=update.callback_query.message.message_id)
        Mafina.Mafina.UseCommand[str(update.callback_query.message.chat_id)] = "LangBot"

def SettingAnswer(update, context, answer):
    chat_id = update.callback_query.message.chat_id
    DB.DataBase.ChangeAnswerSystem(Mafina.Mafina.DB, chat_id)
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["37"], message_id=update.callback_query.message.message_id)

def ExistentialResponse(update, context, answer):
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["13"], message_id=update.callback_query.message.message_id)