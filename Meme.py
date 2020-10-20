import requests, badge, DB, telegram.ext, Keyboard

def Link():
    return requests.get('https://meme-api.herokuapp.com/gimme').json()['url']

def Get_meme(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
    try:
        context.bot.send_photo(update.message.chat_id, Link())
    except Exception:
        context.bot.send_message(update.message.chat_id, answer["3"])

def CountMem(update, context):
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text="Оберіть кількість мемів:",
                                  reply_markup=Keyboard.InlineKeyboard(badge.CountMeme),
                                  message_id=update.callback_query.message.message_id)
    badge.MemeChange = True

def MoreMeme(update, context):
    value = {"0":"0","1":"900","2":"1800", "3":"3600", "4":"7200"}
    if value[str(update.callback_query.data)] != "0":
        if (update.callback_query.message.chat.type=='group'or update.callback_query.message.chat.type=='supergroup'):
            badge.job.run_repeating(MemeChatGroup, interval=int(value[str(update.callback_query.data)]), first=0)
    else:
        badge.job.schedule_removal()
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=badge.CountMeme[int(update.callback_query.data)], message_id=update.callback_query.message.message_id)
    badge.MemeChange = False
def MemeChatGroup(context: telegram.ext.CallbackContext):
    context.bot.send_photo('-1001477418565', Link())