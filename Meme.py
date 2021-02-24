import Mafina, DB, telegram.ext, Keyboard, Url, datetime

def Get_meme(update, context):
    answer, lang = DB.DataBase.GetJsonLanguageBot(Mafina.Mafina.DB, update.message.chat_id)
    try:
        Url.Photo(Url.get_url('https://meme-api.herokuapp.com/gimme'), update, context)
    except Exception:
        context.bot.send_message(update.message.chat_id, answer["3"])

def CountMem(update, context):
    answer, lang = DB.DataBase.GetJsonLanguageBot(Mafina.Mafina.DB, update.message.chat_id)
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["64"],
                                  reply_markup=Keyboard.InlineKeyboard(Mafina.Mafina.CountMeme[lang]),
                                  message_id=update.callback_query.message.message_id)
    Mafina.Mafina.UseCommand[str(update.callback_query.message.chat_id)] = "MemeChange"

def StartSystemMeme():
    cursor = DB.DataBase.UsersSysMeme(Mafina.Mafina.DB)
    for x in cursor:
        for y in range(len(x)):
            if y+2< len(x) and x[y+2]==1:
                Mafina.Mafina.jobchat[str(x[y])]=Mafina.Mafina.job.run_repeating(MemeChatGroup, interval=int(x[y+1]), first= 0,
                                    context=int(x[y]))

def MoreMeme(update, context):
    value = {"0":"0","1":"900","2":"1800", "3":"3600", "4":"7200"}
    chat_id = update.callback_query.message.chat_id
    cursor = DB.DataBase.UsersSysMeme(Mafina.Mafina.DB)
    NewUser = True
    for x in cursor:
        for y in range(len(x)):
            if y+2< len(x) and x[y+2]==1:
                if str(x[y])==str(chat_id):
                    x[y]
                    NewUser = False
    if value[str(update.callback_query.data)] != "0":
        if str(chat_id) in Mafina.Mafina.jobchat.keys():
            Mafina.Mafina.jobchat[str(chat_id)].schedule_removal()
            Mafina.Mafina.jobchat[str(chat_id)] = Mafina.Mafina.job.run_repeating(MemeChatGroup, interval=int(value[str(update.callback_query.data)]), first=datetime.datetime.now(),
                                    context=chat_id)
            DB.DataBase.UpdateSysMeme(Mafina.Mafina.DB,chat_id, True, int(value[str(update.callback_query.data)]))
        elif NewUser == True:
            Mafina.Mafina.jobchat[str(chat_id)] = Mafina.Mafina.job.run_repeating(MemeChatGroup, interval=int(value[str(update.callback_query.data)]), first=datetime.datetime.now(),
                                context=chat_id)
            DB.DataBase.InsertSysMeme(Mafina.Mafina.DB, chat_id, True, int(value[str(update.callback_query.data)]))
    else:
        Mafina.Mafina.jobchat[str(chat_id)].schedule_removal()
        DB.DataBase.UpdateSysMeme(Mafina.Mafina.DB, chat_id, False, 0)
        Mafina.Mafina.jobchat.pop(str(chat_id))
    context.bot.edit_message_text(chat_id=chat_id, text=Mafina.Mafina.CountMeme[int(update.callback_query.data)], message_id=update.callback_query.message.message_id)
    Mafina.Mafina.UseCommand.pop(str(chat_id))

def MemeChatGroup(context: telegram.ext.CallbackContext):
    url = Url.get_url('https://meme-api.herokuapp.com/gimme')
    if Url.is_image(url):
        context.bot.send_photo(context.job.context, url)
    elif Url.is_animation(url):
        context.bot.send_animation(context.job.context, url)