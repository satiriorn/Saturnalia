from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import Setting, badge, Dologusha

def InitKeyboard(NameButton):
    LevelOne = []
    LevelTwo = []
    LevelThree = []
    Button = []
    for i in range(len(NameButton)):
        if i<4:
            LevelOne.append(KeyboardButton(NameButton[i]))
        elif (i>=4) and (i<7):
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
    if badge.CommandSettingTranslate == True:
        Setting.SettingTranslate(update, context)
    elif badge.StartDl == True:
        print("1")
        Dologusha.start(update, context)
    elif badge.CommandLangBot == True:
        Setting.LanguageBot(update, context)
    elif query.data == "0":
        Setting.SettingTranslate(update,context)
    elif query.data =="1":
        Setting.LanguageBot(update,context)
    else:
        Setting.ExistentialResponse(update,context)
    return query

