import Keyboard, badge, DB

def help(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    context.bot.send_message(update.message.chat_id,answer["8"] ,reply_markup = Keyboard.InitKeyboard(badge.MainKeyboard))