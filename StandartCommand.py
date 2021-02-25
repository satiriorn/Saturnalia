import base64

def start(update, context, answer, Mafina, chat_id):
    try:
        first_name = update.message.chat.first_name
        if update.message.chat.type == "private":
            Mafina.DB.CheckUser(first_name, update.message.chat.username, chat_id,
                                        update.message.from_user.language_code, update.message.chat.type)
        if dec("Um9zaXRzYU1hbmV2YQ==").decode("UTF-8") == update.message.chat.username and update.message.chat.type == "private":
            Mafina.Dologusha.start(update, context)
        else:
            Mafina.DB.CheckUser(update.message.chat.title, update.message.chat.username, chat_id,
            update.message.from_user.language_code, update.message.chat.type)
        context.bot.send_message(chat_id, answer["start"], reply_markup = Mafina.keyboard.InitKeyboard(Mafina.keyboard.MainKeyboard))
    except Exception:
        context.bot.send_message(update.message.chat_id, "щось пішло не так")

def help(update, context, answer, Mafina):
    context.bot.send_message(update.message.chat_id, answer["8"],
                             reply_markup = Mafina.keyboard.InitKeyboard(Mafina.keyboard.MainKeyboard))

def dec(s):
    return base64.b64decode(s)