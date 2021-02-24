import Keyboard, time, Mafina

def Rest(update, context, answer, lang, chat_id, status = True):
    Mafina.Mafina.UseCommand[str(chat_id)] = "Rest"
    if status: context.bot.send_message(chat_id=chat_id, text=answer["65"], reply_markup=Keyboard.InlineKeyboard(Mafina.Mafina.RestButton[lang], False))
    else:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=Mafina.Mafina.RestButton[lang][0], message_id=update.callback_query.message.message_id)
        for i in range(6):
            if i == 0: time.sleep(5)
            context.bot.send_message(chat_id=chat_id, text=answer["66"])
            time.sleep(5)
            context.bot.send_message(chat_id=chat_id, text=answer["67"])
            time.sleep(5)
        context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=answer["68"])
        Mafina.Mafina.UseCommand.pop(str(chat_id))