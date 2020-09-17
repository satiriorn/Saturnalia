import telegram
NameButton = ["/Evtuh", "/Weather", "/Voice", "/GetMusic", "/Translate", "/ShevchenkoStyle", "/Cat", "/Dog", "/Help", "/Meme"]

def InitKeyboard():
    LevelOne = []
    LevelThree = []
    Button = []
    for i in range(len(NameButton)):
        if i<5:
            LevelOne.append(telegram.KeyboardButton(NameButton[i]))
        elif i==5:
            Button.append(LevelOne)
            Button.append([telegram.KeyboardButton(NameButton[i])])
        else:
            LevelThree.append(telegram.KeyboardButton(NameButton[i]))
    Button.append(LevelThree)
    return telegram.ReplyKeyboardMarkup(Button, resize_keyboard=True)
