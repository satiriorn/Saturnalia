import badge, DB, telegram.ext, Keyboard, Url

def Get_meme(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
    try:
        Url.Photo(Url.get_url('https://meme-api.herokuapp.com/gimme'), update, context)
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
        badge.job.run_repeating(MemeChatGroup, interval=int(value[str(update.callback_query.data)]), first=0, context=update.callback_query.message.chat_id)
    else:
        badge.job.schedule_removal()
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=badge.CountMeme[int(update.callback_query.data)], message_id=update.callback_query.message.message_id)
    badge.MemeChange = False

def MemeChatGroup(context: telegram.ext.CallbackContext):
    url = Url.get_url('https://meme-api.herokuapp.com/gimme')
    if Url.is_image(url):
        context.bot.send_photo(context.job.context, url)
    elif Url.is_animation(url):
        context.bot.send_animation(context.job.context, url)