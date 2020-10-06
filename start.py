import Keyboard, DB, badge, base64, Dologusha

def start(update, context):
    print(update)
    try:
        first_name = update.message.chat.first_name
        chat_id = update.message.chat_id
        k = Keyboard.InitKeyboard(badge.MainKeyboard)
        if update.message.chat.type == "private":
            DB.DataBase.CheckUser(badge.DB, first_name, update.message.chat.username, chat_id,
                                  update.message.from_user.language_code, update.message.chat.type)
        if dec("Um9zaXRzYU1hbmV2YWE=").decode("UTF-8") == update.message.chat.username and update.message.chat.type == "private":
            Dologusha.start(update, context)
        else:
            DB.DataBase.CheckUser(badge.DB,update.message.chat.title,update.message.chat.username, chat_id,
            update.message.from_user.language_code, update.message.chat.type)
            answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
            context.bot.send_message(chat_id, answer["start"], reply_markup=k)
    except Exception:
        pass
        #context.bot.send_message(update.message.chat_id, answer['0'])

def dec(s):
    return base64.b64decode(s)