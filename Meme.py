import badge, DB, telegram.ext, Keyboard, Url, datetime

def Get_meme(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
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

def StartSystemMeme():
    cursor = DB.DataBase.UsersSysMeme(badge.DB)
    for x in cursor:
        for y in range(len(x)):
            if y+2< len(x) and x[y+2]==True:
                badge.jobchat[str(x[y])]=badge.job.run_repeating(MemeChatGroup, interval=int(x[y+1]), first= 0,
                                    context=int(x[y]))
            y+=2

def MoreMeme(update, context):
    value = {"0":"0","1":"900","2":"1800", "3":"3600", "4":"7200"}
    chat_id = update.callback_query.message.chat_id
    if value[str(update.callback_query.data)] != "0":
        if str(chat_id) in badge.jobchat.keys():
            badge.jobchat[str(chat_id)].schedule_removal()
            badge.jobchat[str(chat_id)] = badge.job.run_repeating(MemeChatGroup, interval=int(value[str(update.callback_query.data)]), first=datetime.datetime.now(),
                                    context=chat_id)
            DB.DataBase.UpdateSysMeme(badge.DB,chat_id, True, int(value[str(update.callback_query.data)]))
        else:
            badge.jobchat[str(chat_id)] = badge.job.run_repeating(MemeChatGroup, interval=int(value[str(update.callback_query.data)]), first=datetime.datetime.now(),
                                context=chat_id)
            DB.DataBase.InsertSysMeme(badge.DB, chat_id, True, int(value[str(update.callback_query.data)]))
    else:
        badge.jobchat[str(chat_id)].schedule_removal()
        DB.DataBase.UpdateSysMeme(badge.DB, chat_id, False, 0)
        badge.jobchat.pop(str(chat_id))
    context.bot.edit_message_text(chat_id=chat_id, text=badge.CountMeme[int(update.callback_query.data)], message_id=update.callback_query.message.message_id)
    badge.MemeChange = False

def MemeChatGroup(context: telegram.ext.CallbackContext):
    url = Url.get_url('https://meme-api.herokuapp.com/gimme')
    if Url.is_image(url):
        context.bot.send_photo(context.job.context, url)
    elif Url.is_animation(url):
        context.bot.send_animation(context.job.context, url)