from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import Setting, badge, Dologusha, Meme, Rest, Youtube, Cut

def InitKeyboard(NameButton):
    LevelOne = []
    LevelTwo = []
    LevelThree = []
    Button = []
    for i in range(len(NameButton)):
        if i<5:
            LevelOne.append(KeyboardButton(NameButton[i]))
        elif (i>=5) and (i<8):
            LevelTwo.append(KeyboardButton(NameButton[i]))
        else:
            LevelThree.append(KeyboardButton(NameButton[i]))
    Button.append(LevelOne)
    Button.append(LevelTwo)
    Button.append(LevelThree)
    return ReplyKeyboardMarkup(Button, resize_keyboard=True)

def InlineKeyboard(NameButton, Status=True):
    keyboard = []
    i = 0
    data = lambda NameButton, Status, i: i if Status == True else NameButton[i]
    while i < len(NameButton):
        if ((i+1)<len(NameButton)):
            keyboard.append([InlineKeyboardButton(NameButton[i], callback_data= data(NameButton,Status,i)),
                         InlineKeyboardButton(NameButton[i+1], callback_data= data(NameButton,Status,i+1))])
            i+=2
        else:
            keyboard.append([InlineKeyboardButton(NameButton[i], callback_data= data(NameButton,Status,i))])
            i += 1
    return  InlineKeyboardMarkup(keyboard)

def button(update,context):
    query = update.callback_query
    print(query.data)
    if str(update.callback_query.message.chat_id) in badge.UseCommand.keys():
        res = badge.UseCommand[str(update.callback_query.message.chat_id)]
        if res == "Rest": Rest.Rest(update, context, False)
        elif res == "MemeChange": Meme.MoreMeme(update, context)
        elif res == "SettingTranslate": Setting.SettingTranslate(update, context)
        elif res == "Dologisha": Dologusha.start(update, context)
        elif res == "LangBot": Setting.LanguageBot(update, context)
    elif query.data == "0":
        Setting.SettingTranslate(update,context)
    elif query.data =="1":
        Setting.LanguageBot(update,context)
    elif query.data == "2":
        Meme.CountMem(update,context)
    elif query.data == "Скачати Відео":
        Youtube.Get_Video(update,context)
    elif query.data == "Скачати Аудіо":
        Youtube.Get_Audio(update,context)
    elif query.data == "Обрізати Відео":
        Cut.CutVideo(update,context)
    elif query.data == "Обрізати Аудіо":
        Cut.CutAudio(update,context)
    else:
        Setting.ExistentialResponse(update,context)
    return query

