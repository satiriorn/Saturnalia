import telegram

def InitKeyboard(NameButton):
    LevelOne = []
    LevelTwo = []
    LevelThree = []
    Button = []
    for i in range(len(NameButton)):
        if i<4:
            LevelOne.append(telegram.KeyboardButton(NameButton[i]))
        elif (i>=4) and (i<7):
            LevelTwo.append(telegram.KeyboardButton(NameButton[i]))
        else:
            LevelThree.append(telegram.KeyboardButton(NameButton[i]))
    Button.append(LevelOne)
    Button.append(LevelTwo)
    Button.append(LevelThree)
    return telegram.ReplyKeyboardMarkup(Button, resize_keyboard=True)

