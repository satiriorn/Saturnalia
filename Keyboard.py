from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import Setting, badge, Dologusha, Meme, Rest, Youtube, Cut, Thread, weather, DogAndCat, Book

def InitKeyboard(NameButton):
    LevelOne = []
    LevelTwo = []
    LevelThree = []
    LevelFour = []
    Button = []
    for i in range(len(NameButton)):
        if i<5:
            LevelOne.append(KeyboardButton(NameButton[i]))
        elif (i>=5) and (i<8):
            LevelTwo.append(KeyboardButton(NameButton[i]))
        elif (i >= 8) and (i < 12):
            LevelThree.append(KeyboardButton(NameButton[i]))
        else:
            LevelFour.append(KeyboardButton(NameButton[i]))
    Button.append(LevelOne)
    Button.append(LevelTwo)
    Button.append(LevelThree)
    Button.append(LevelFour)
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
        if res == "Rest": Thread.Thread(Rest.Rest, (update, context, False))
        elif res == "MemeChange": Thread.Thread(Meme.MoreMeme, (update, context))
        elif res == "SettingTranslate": Thread.Thread(Setting.SettingTranslate, (update, context))
        elif res == "Dologusha": Thread.Thread(Dologusha.start, (update, context))
        elif res == "LangBot": Thread.Thread(Setting.LanguageBot, (update, context))
        elif res == "Confirm" or res == "Check"or res == "BookLang"or res == "FormatBook": Thread.Thread(Book.UploadBook, (update, context))
        elif res == "SeveralResult":Thread.Thread(Book.SearchBook, (update, context))
        elif res == "ConfirmTypeFile":Thread.Thread(Book.GetFile, (update, context))
        elif res == "GetBookViaAuthor"or res == "SelectBookByAuthor": Thread.Thread(Book.SearchAuthor, (update, context))
        elif res == "GetBook":Thread.Thread(Book.SendListReadBooks, (update, context))
        elif query.data == badge.CancelButton["uk"][0] or query.data == badge.CancelButton["en"][0]or query.data == badge.CancelButton["be"][0]: Thread.Thread(Book.Cancel, (update, context))
    elif query.data == "0":
        Thread.Thread(Setting.SettingTranslate, (update, context))
    elif query.data =="1":
        Thread.Thread(Setting.LanguageBot, (update, context))
    elif query.data == "2":
        Thread.Thread(weather.StateWeather, (update, context))
    elif query.data == "3":
        Thread.Thread(DogAndCat.SysAnimal, (update, context))
    elif query.data == "4":
        Thread.Thread(Meme.CountMem,(update, context))
    elif query.data == "5":
        Thread.Thread(Setting.SettingAnswer, (update, context))
    elif query.data == badge.YoutubeKeyboard["uk"][0] or query.data == badge.YoutubeKeyboard["en"][0] or query.data == badge.YoutubeKeyboard["be"][0]:
        Thread.Thread(Youtube.Get_Video, (update, context))
    elif query.data == badge.YoutubeKeyboard["uk"][1] or query.data == badge.YoutubeKeyboard["en"][1] or query.data == badge.YoutubeKeyboard["be"][1]:
        Thread.Thread(Youtube.Get_Audio, (update, context))
    elif query.data == badge.CutKeyboard["uk"][0] or query.data == badge.CutKeyboard["en"][0] or query.data == badge.CutKeyboard["be"][0]:
        Thread.Thread(Cut.CutVideo, (update, context))
    elif query.data == badge.CutKeyboard["uk"][1] or query.data == badge.CutKeyboard["en"][1] or query.data == badge.CutKeyboard["be"][1]:
        Thread.Thread(Cut.CutAudio, (update, context))
    elif query.data == badge.YoutubeKeyboard["uk"][2] or query.data == badge.YoutubeKeyboard["en"][2] or query.data == badge.YoutubeKeyboard["be"][2]:
        Thread.Thread(Cut.GetCutStart, (update, context))
    elif query.data == badge.CancelButton["uk"][0] or query.data == badge.CancelButton["en"][0]or query.data == badge.CancelButton["be"][0]:
        Thread.Thread(Book.Cancel, (update, context))
    elif query.data == badge.MenuBookKeyboard["uk"][2] or query.data == badge.MenuBookKeyboard["en"][2] or query.data == badge.MenuBookKeyboard["be"][2]:
        Thread.Thread(Book.SearchBook, (update, context))
    elif query.data == badge.MenuBookKeyboard["uk"][0] or query.data == badge.MenuBookKeyboard["en"][0] or query.data == badge.MenuBookKeyboard["be"][0]:
        Thread.Thread(Book.UploadBook, (update, context))
    elif query.data == badge.BookStateKeyboard["uk"][1] or query.data == badge.BookStateKeyboard["en"][1] or query.data == badge.BookStateKeyboard["be"][1]:
        Thread.Thread(Book.GetFile, (update, context))
    elif query.data == badge.MenuBookKeyboard["uk"][1] or query.data == badge.MenuBookKeyboard["en"][1] or query.data == badge.MenuBookKeyboard["be"][1]:
        Thread.Thread(Book.SearchAuthor, (update, context))
    elif query.data == badge.MenuBookKeyboard["uk"][3] or query.data == badge.MenuBookKeyboard["en"][3] or query.data == badge.MenuBookKeyboard["be"][3]:
        Thread.Thread(Book.CountBookInDB, (update, context))
    elif query.data == badge.BookStateKeyboard["uk"][0] or query.data == badge.BookStateKeyboard["en"][0] or query.data == badge.BookStateKeyboard["be"][0]:
        Thread.Thread(Book.AddBookInReadList, (update, context))
    elif query.data == badge.MenuBookKeyboard["uk"][4] or query.data == badge.MenuBookKeyboard["en"][4] or query.data == badge.MenuBookKeyboard["be"][4]:
        Thread.Thread(Book.SendListReadBooks, (update, context))
    elif query.data == badge.BookStateKeyboardDelete["uk"][0] or query.data == badge.BookStateKeyboardDelete["en"][0] or query.data == badge.BookStateKeyboardDelete["be"][0]:
        Thread.Thread(Book.DeleteInReadList, (update, context))
    else:
        Thread.Thread(Setting.ExistentialResponse, (update, context))
    return query