import telegram

NameButton = ["/Evtuh","/Weather","/Voice", "/ShevchenkoStyle", "/Cat", "/Dog", "/Help"]

def InitKeyboard():
    Button = []
    for i in range(len(NameButton)):
        Button = telegram.KeyboardButton(NameButton[i])
    return telegram.ReplyKeyboardMarkup(Button, resize_keyboard=True)