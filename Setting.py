import badge, Keyboard, DB

def ShowSetting(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
    context.bot.send_message(update.message.chat_id,answer["9"], reply_markup=Keyboard.InlineKeyboard(badge.Setting))

def SettingTranslate(update,context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.callback_query.from_user.first_name)
    if badge.CommandSettingTranslate !=True:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["10"],
        reply_markup = Keyboard.InlineKeyboard(badge.TranslateKeyboard, False),message_id=update.callback_query.message.message_id)
        badge.CommandSettingTranslate = True
        return
    if update.callback_query.message.chat.type == "private":
        DB.DataBase.VerificationLanguage(badge.DB, update.callback_query.message.chat.first_name, badge.b[update.callback_query.data])
    else:
        DB.DataBase.VerificationLanguage(badge.DB,  update.callback_query.message.chat.title, badge.b[update.callback_query.data])

    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["11"], message_id=update.callback_query.message.message_id)
    badge.CommandSettingTranslate = False

def LanguageBot(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.callback_query.from_user.first_name)
    if badge.CommandLangBot != True:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                      text=answer["12"],
                                      reply_markup=Keyboard.InlineKeyboard(badge.LanguageBot, False),
                                      message_id=update.callback_query.message.message_id)
        badge.CommandLangBot = True
        return
    if update.callback_query.message.chat.type == "private":
        DB.DataBase.VerificationLanguage(badge.DB, update.callback_query.message.chat.first_name, badge.b[update.callback_query.data], False)
    else:
        DB.DataBase.VerificationLanguage(badge.DB,  update.callback_query.message.chat.title, badge.b[update.callback_query.data], False)
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["11"], message_id=update.callback_query.message.message_id)
    badge.CommandLangBot = False

def ExistentialResponse(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.callback_query.from_user.first_name)
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                  text=answer["13"],
                                  message_id=update.callback_query.message.message_id)