import badge, Thread, DB, Keyboard

class Book:
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        self.book_lang = None
        self.file_id = None

def SearchBook():
    pass

def UploadBook(update, context):
    chat_id = GetChatID(update)
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    if str(chat_id) in badge.UseCommand.keys():
        if badge.UseCommand[str(chat_id)] == "Check":
            context.bot.send_message(chat_id, answer["43"],
                                     reply_markup=Keyboard.InlineKeyboard(badge.ConfirmKeyboard , False))
            data = (update.message.text).split('\n')
            badge.Book[str(chat_id)] = Book(Name=data[0], Author=data[1])
            print(badge.Book[str(chat_id)].Name)
            badge.UseCommand.pop(str(chat_id))
            badge.UseCommand[str(chat_id)] = "Confirm"

        elif badge.UseCommand[str(chat_id)] == "Confirm":
            if(str(update.callback_query.data) =="Так"):
                badge.UseCommand.pop(str(chat_id))
                context.bot.edit_message_text(chat_id=chat_id,text=answer["44"],
                                              message_id=update.callback_query.message.message_id)
                context.bot.send_message(chat_id,text=answer["40"],
                                         reply_markup=Keyboard.InlineKeyboard(badge.TranslateKeyboard, False))
                badge.UseCommand[str(chat_id)] = "BookLang"
            else:
                print("R")
                badge.UseCommand.pop(str(chat_id))
                badge.Book.pop(str(chat_id))
                UploadBook(update, context)

        elif badge.UseCommand[str(chat_id)] == "BookLang":
            badge.Book[str(chat_id)].book_lang = badge.b[update.callback_query.data]
            badge.UseCommand.pop(str(chat_id))
            badge.UseCommand[str(chat_id)] = "UploadFile"
            context.bot.edit_message_text(chat_id=chat_id, text=answer["42"],
                                          message_id=update.callback_query.message.message_id)
            print(badge.Book[str(chat_id)].book_lang)
        elif badge.UseCommand[str(chat_id)] == "UploadFile":
            badge.Book[str(chat_id)].file_id = update.message.document.file_id
            print(badge.Book[str(chat_id)].file_id)
            result = DB.DataBase.BookSystem(badge.DB, badge.Book[str(chat_id)])
            if result:
                context.bot.send_message(chat_id, text=answer["45"])
            else:
                context.bot.send_message(chat_id, text=answer["46"])
            badge.UseCommand.pop(str(chat_id))
            badge.Book.pop(str(chat_id))
    else:
        context.bot.edit_message_text(chat_id=chat_id, text=answer["41"], message_id=update.callback_query.message.message_id)
        badge.UseCommand[str(chat_id)] = "Check"

def MenuBook(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    context.bot.send_message(update.message.chat_id, answer["39"], reply_markup=Keyboard.InlineKeyboard(badge.MenuBookKeyboard, False))

def MonitorDoc(update, context):
    if str(update.message.chat_id) in badge.UseCommand.keys():
        res = badge.UseCommand[str(update.message.chat_id)]
        if res == "UploadFile": Thread.Thread(UploadBook, (update, context))
    print("jopa"+str(update))

def GetChatID(update):
    try:
        return update.callback_query.message.chat_id
    except Exception:
        return update.message.chat_id

