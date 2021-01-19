from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import Setting, badge, Dologusha, Meme, Rest, Youtube, Cut, Thread, weather, DogAndCat, Book

def InitKeyboard(NameButton):
    LevelOne = []
    LevelTwo = []
    LevelThree = []
    Button = []
    for i in range(len(NameButton)):
        if i<6:
            LevelOne.append(KeyboardButton(NameButton[i]))
        elif (i>=6) and (i<9):
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
        if res == "Rest": Thread.Thread(Rest.Rest,(update, context, False))
        elif res == "MemeChange": Thread.Thread(Meme.MoreMeme,(update, context))
        elif res == "SettingTranslate": Thread.Thread(Setting.SettingTranslate,(update, context))
        elif res == "Dologusha": Thread.Thread(Dologusha.start,(update, context))
        elif res == "LangBot": Thread.Thread(Setting.LanguageBot,(update, context))
        elif res == "Confirm" or res == "Check"or res == "BookLang"or res == "FormatBook":  Thread.Thread(Book.UploadBook, (update, context))
        elif res == "SeveralResult":Thread.Thread(Book.SearchBook,(update,context))
        elif res == "ConfirmTypeFile":Thread.Thread(Book.GetFile,(update,context))
        elif query.data == badge.CancelButton[0]: Thread.Thread(Book.Cancel, (update, context))
    elif query.data == "0":
        Thread.Thread(Setting.SettingTranslate,(update ,context))
    elif query.data =="1":
        Thread.Thread(Setting.LanguageBot, (update,context))
    elif query.data == "2":
        Thread.Thread(weather.StateWeather, (update,context))
    elif query.data == "3":
        Thread.Thread(DogAndCat.SysAnimal, (update,context))
    elif query.data == "4":
        Thread.Thread(Meme.CountMem,(update, context))
    elif query.data == "Скачати Відео":
        Thread.Thread(Youtube.Get_Video,(update, context))
    elif query.data == "Скачати Аудіо":
        Thread.Thread(Youtube.Get_Audio,(update, context))
    elif query.data == "Обрізати Відео":
        Thread.Thread(Cut.CutVideo,(update, context))
    elif query.data == "Обрізати Аудіо":
        Thread.Thread(Cut.CutAudio,(update, context))
    elif query.data == "Скачати та Обрізати":
        Thread.Thread(Cut.GetCutStart,(update, context))
    elif query.data == badge.CancelButton[0]:
        Thread.Thread(Book.Cancel,(update,context))
    elif query.data == "Пошук по назві":
        Thread.Thread(Book.SearchBook,(update,context))
    elif query.data == "Завантажування книги":
        Thread.Thread(Book.UploadBook, (update, context))
    elif query.data == "Додати книгу до прочитаних":
        Thread.Thread(Book.AddBookInReadList, (update,context))
    elif query.data == "Отримати файл книги":
        Thread.Thread(Book.GetFile,(update,context))
    else:
        Thread.Thread(Setting.ExistentialResponse,(update, context))
    return query