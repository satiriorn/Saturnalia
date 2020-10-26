import badge, DB, telegram.ext, Keyboard, Url

def Get_meme(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
    try:
        Url.Photo(Url.get_url('https://meme-api.herokuapp.com/gimme'), update, context)
        print(badge.job.jobs())
    except Exception:
        context.bot.send_message(update.message.chat_id, answer["3"])

def CountMem(update, context):
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text="Оберіть кількість мемів:",
                                  reply_markup=Keyboard.InlineKeyboard(badge.CountMeme),
                                  message_id=update.callback_query.message.message_id)
    badge.MemeChange = True

def MoreMeme(update, context):
    value = {"0":"0","1":"900","2":"1800", "3":"3600", "4":"7200"}
    chat_id = update.callback_query.message.chat_id
    if value[str(update.callback_query.data)] != "0":
        if str(chat_id) in badge.jobchat.keys():
            badge.jobchat[str(chat_id)].schedule_removal()
            badge.jobchat[str(chat_id)] = badge.job.run_repeating(MemeChatGroup, interval=int(value[str(update.callback_query.data)]), first=0,
                                    context=chat_id)
        else:
            badge.jobchat[str(chat_id)] = badge.job.run_repeating(MemeChatGroup, interval=int(value[str(update.callback_query.data)]), first=0,
                                context=chat_id)
    else:
        badge.jobchat[str(chat_id)].schedule_removal()
        badge.jobchat.pop(str(chat_id))
    context.bot.edit_message_text(chat_id=chat_id, text=badge.CountMeme[int(update.callback_query.data)], message_id=update.callback_query.message.message_id)
    badge.MemeChange = False

def MemeChatGroup(context: telegram.ext.CallbackContext):
    url = Url.get_url('https://meme-api.herokuapp.com/gimme')
    if Url.is_image(url):
        context.bot.send_photo(context.job.context, url)
    elif Url.is_animation(url):
        context.bot.send_animation(context.job.context, url)