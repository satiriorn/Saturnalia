import DB, badge, Url, telegram.ext, datetime, os

def Cat_photo(update, context):
    answer, lang = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    try:
        Url.Photo(Url.get_url('https://api.thecatapi.com/v1/images/search'), update, context)
    except Exception:
        context.bot.send_message(context.bot_data[update.poll_answer.poll_id], answer["6"])

def Dog_photo(update, context):
    answer, lang = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
    try:
        Url.Photo(Url.get_url('https://random.dog/woof.json'), update, context)
    except Exception:
        context.bot.send_message(context.bot_data[update.poll_answer.poll_id], answer["7"])

def StartSysAnimal():
    cursor = DB.DataBase.UsersSysAnimal(badge.DB)
    target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
    target_time = None
    for x in cursor:
        for y in range(len(x)):
            if y + 1 < len(x) and x[y + 1] == True:
                for i in range(4):
                    if i==0:
                        target_time = datetime.time(hour=9, minute=00, second=25).replace(tzinfo=target_tzinfo)
                    elif i == 1:
                        target_time = datetime.time(hour=13, minute=00, second=25).replace(tzinfo=target_tzinfo)
                    elif i == 2:
                        target_time = datetime.time(hour=18, minute=00, second=25).replace(tzinfo=target_tzinfo)
                    else:
                        target_time = datetime.time(hour=22, minute=00, second=25).replace(tzinfo=target_tzinfo)
                    badge.jobchat[str(x[y])] = badge.job.run_daily(AnimalJob, target_time, context=x[y])

def SysAnimal(update,context):
    chat_id = update.callback_query.message.chat_id
    answer, lang = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    cursor = DB.DataBase.UsersSysAnimal(badge.DB)
    target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
    target_time = datetime.time(hour=9, minute=00, second=25).replace(tzinfo=target_tzinfo)
    NewUser = True
    for x in cursor:
        for y in range(len(x)):
            if str(x[y]) == str(chat_id):
                state = (lambda x, y: True if x[y+1] == False else False) (x,y)
                DB.DataBase.UpdateSysAnimal(badge.DB, chat_id, state)
                if str(chat_id) in badge.jobchat.keys() and state==False:
                    badge.jobchat[str(chat_id)].schedule_removal()
                    badge.jobchat.pop(str(chat_id))
                    context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                                  message_id=update.callback_query.message.message_id)
                    NewUser = False
                    break
                else:
                    badge.jobchat[str(chat_id)] = badge.job.run_daily(AnimalJob, target_time, context=chat_id)
                    context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                                  message_id=update.callback_query.message.message_id)
                    NewUser = False
                break
    if NewUser:
        DB.DataBase.InsertSysAnimal(badge.DB, update.callback_query.message.chat_id, True)
        badge.jobchat[str(chat_id)] = badge.job.run_daily(AnimalJob, target_time, context=chat_id)
        context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                      message_id=update.callback_query.message.message_id)


def AnimalJob(context: telegram.ext.CallbackContext):
    x = DB.DataBase.GetCountAnimal(badge.DB, context.job.context)
    fileID = DB.DataBase.GetFileId(badge.DB, x)
    if x==1:
        context.bot.send_message(context.job.context,"Увімкнута система котиків.\nКотики будуть надсилатися у заданий час два рази на день, якщо вони вам не потрібні або заважають, можете вимкнути через налаштування бота.\n Якщо немає клавіатури бота -> /Help.\n Якщо клавіатура не потрібна-> /SettingBot.\n Кількість котиків на даний момент вистачає на півроку.\n Насолоджуйтесь.\n Якщо у вас є непогана кількість унікальних мімімішних котиків пишіть @Satiriorn.")
    file = context.bot.getFile(fileID)
    title = ("{0}.gif").format(context.job.context)
    file.download(title)
    try:
        context.bot.send_video(context.job.context, open(title, 'rb'))
    except Exception:
        context.bot.send_animation(context.job.context, open(title, 'rb'))
    DB.DataBase.UpCountAnimal(badge.DB, context.job.context)
    os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), title))