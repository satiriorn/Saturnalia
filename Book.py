import badge, Thread, DB, Keyboard
def SearchBook():
    pass
def UploadBook(update, context):
    chat_id = GetChatID(update)
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    if str(chat_id) in badge.UseCommand.keys():
        if badge.UseCommand[str(chat_id)] == "Confirm":
            print(update)
            badge.UseCommand.pop(str(chat_id))
            badge.UseCommand[str(chat_id)] = "BookSettings"
            context.bot.send_message(chat_id, answer["40"],
                                     reply_markup=Keyboard.InlineKeyboard(badge.ConfirmKeyboard , False))
        elif badge.UseCommand[str(chat_id)] == "BookSettings":
            context.bot.send_message(chat_id, answer["40"],  reply_markup=Keyboard.InlineKeyboard(badge.TranslateKeyboard, False))
            badge.UseCommand.pop(str(chat_id))
            badge.UseCommand[str(chat_id)] = "f"
        elif badge.UseCommand[str(chat_id)] == "f":
            context.bot.edit_message_text(chat_id=chat_id, text=answer["42"],
                                          message_id=update.callback_query.message.message_id)
    else:
        context.bot.edit_message_text(chat_id=chat_id, text=answer["41"], message_id=update.callback_query.message.message_id)
        badge.UseCommand[str(chat_id)] = "Confirm"


def MenuBook(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    context.bot.send_message(update.message.chat_id, answer["39"], reply_markup=Keyboard.InlineKeyboard(badge.MenuBookKeyboard, False))

def MonitorDoc(update, context):
    if str(update.message.chat_id) in badge.UseCommand.keys():
        res = badge.UseCommand[str(update.message.chat_id)]
        #if res == "UploadBook" or: Thread.Thread(MenuBook)
    print("jopa"+str(update))

def GetChatID(update):
    try:
        return update.callback_query.message.chat_id
    except Exception:
        return update.message.chat_id
