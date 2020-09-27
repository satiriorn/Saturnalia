from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import Setting
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

def InlineKeyboard(NameButton):
    keyboard = []
    i = 0
    while i < len(NameButton):
        if (i+1) == True:
            keyboard.append([InlineKeyboardButton(NameButton[i], callback_data=str(i)),
                         InlineKeyboardButton(NameButton[i+1], callback_data=str(i + 1))])
            i+=2
        else:
            keyboard.append([InlineKeyboardButton(NameButton[i], callback_data=str(i))])
            i += 1
    for x in range(len(keyboard)):
        print(keyboard[x])
    return  InlineKeyboardMarkup(keyboard)

def button(update,context):
    query = update.callback_query
    print(query.data)
    if query.data == "0":
        Setting.SettingTranslate(update,context)

    return query

