import Keyboard, time, badge, DB

def Rest(update, context, status = True):
    chat_id = badge.GetChatID(update)
    answer, lang = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    badge.UseCommand[str(chat_id)] = "Rest"
    if status:
        context.bot.send_message(chat_id=chat_id, text=answer["65"], reply_markup=Keyboard.InlineKeyboard(badge.RestButton[lang], False))
    else:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=badge.RestButton[lang][0], message_id=update.callback_query.message.message_id)
        for i in range(6):
            if i == 0: time.sleep(5)
            context.bot.send_message(chat_id=chat_id, text=answer["66"])
            time.sleep(5)
            context.bot.send_message(chat_id=chat_id, text=answer["67"])
            time.sleep(5)
        context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=answer["68"])
        badge.UseCommand.pop(str(chat_id))