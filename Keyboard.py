import telegram
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

NameButton = ["/Evtuh","/Weather","/Voice", "/ShevchenkoStyle", "/Cat", "/Dog", "/Help"]

def InitKeyboard():
    Button = []
    for i in range(len(NameButton)):
        Button = telegram.KeyboardButton(NameButton[i])
    markup = ReplyKeyboardMarkup().row(Button[0],Button[1],Button[2])
    return markup