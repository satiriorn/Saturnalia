import badge, Keyboard, DB
def ShowSetting(update, context):
    context.bot.send_message(update.message.chat_id, "Ви увійшли в налаштування бота оберіть бажані зміни.",
                             reply_markup=Keyboard.InlineKeyboard(badge.Setting))
def SettingTranslate(update,context):
    #context.bot.edit_message_text(text="Selected option: {}".format(query.data),
     #                     chat_id=query.message.chat_id,
    #                      message_id=query.message.message_id)
    if badge.CommandSettingTranslate !=True:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text="Оберіть потрібну вам мову на яку бот буде перекладати:",
                                 reply_markup = Keyboard.InlineKeyboard(badge.TranslateKeyboard),message_id=update.callback_query.message.message_id)
        badge.CommandSettingTranslate = True
        return
    if update.message.chat.type == "private":
        DB.DataBase.VerificationLanguage(badge.DB, update.message.chat.first_name, badge.b[update.message.text])
    else:
        DB.DataBase.VerificationLanguage(badge.DB, update.message.chat.title, badge.b[update.message.text])

    context.bot.send_message(update.message.chat_id, "Ваша обрана мова встановлена.",
                             reply_markup=Keyboard.InitKeyboard(badge.MainKeyboard))
    badge.CommandSettingTranslate = False