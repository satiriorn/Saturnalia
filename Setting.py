import badge, Keyboard, DB

def ShowSetting(update, context):
    context.bot.send_message(update.message.chat_id, "Ви увійшли в налаштування бота оберіть бажані зміни.",
                             reply_markup=Keyboard.InlineKeyboard(badge.Setting))
def SettingTranslate(update,context):
    if badge.CommandSettingTranslate !=True:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text="Оберіть потрібну вам мову на яку бот буде перекладати:",
                                 reply_markup = Keyboard.InlineKeyboard(badge.TranslateKeyboard, False),message_id=update.callback_query.message.message_id)
        badge.CommandSettingTranslate = True
        return
    if update.callback_query.message.chat.type == "private":
        DB.DataBase.VerificationLanguage(badge.DB, update.callback_query.message.chat.first_name, badge.b[update.callback_query.data])
    else:
        DB.DataBase.VerificationLanguage(badge.DB,  update.callback_query.message.chat.title, badge.b[update.callback_query.data])

    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text="Ваша обрана мова встановлена.", message_id=update.callback_query.message.message_id)
    badge.CommandSettingTranslate = False

def LanguageBot(update, context):
    if badge.CommandLangBot != True:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                      text="Оберіть мову бота:",
                                      reply_markup=Keyboard.InlineKeyboard(badge.LanguageBot, False),
                                      message_id=update.callback_query.message.message_id)
        badge.CommandLangBot = True
        return
    if update.callback_query.message.chat.type == "private":
        DB.DataBase.VerificationLanguage(badge.DB, update.callback_query.message.chat.first_name, badge.b[update.callback_query.data], False)
    else:
        DB.DataBase.VerificationLanguage(badge.DB,  update.callback_query.message.chat.title, badge.b[update.callback_query.data], False)
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text="Ваша обрана мова встановлена.", message_id=update.callback_query.message.message_id)
    badge.CommandLangBot = False
