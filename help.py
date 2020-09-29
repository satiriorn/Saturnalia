import Keyboard, badge, DB
def help(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
    context.bot.send_message(update.message.chat_id,answer["9"] ,reply_markup = Keyboard.InitKeyboard(badge.MainKeyboard))