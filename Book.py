import Mafina, Thread, DB, Keyboard, os

class Book:
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        self.book_lang = None
        self.file_id = None
        self.format = None
        self.full_file_name = ""

def GetFile(update, context, answer, chat_id):
    print("GETFILE")
    if str(chat_id) in Mafina.Mafina.UseCommand.keys():
        if Mafina.Mafina.UseCommand[str(chat_id)] == "ConfirmTypeFile":
            context.bot.edit_message_text(chat_id=chat_id, text=answer["53"],
                                          message_id=update.callback_query.message.message_id)
            DownloadBook(update, context, Mafina.Mafina.KeyboardFormat[str(chat_id)][update.callback_query.data], update.callback_query.data)
            Mafina.Mafina.UseCommand.pop(str(chat_id))
            Mafina.Mafina.KeyboardFormat.pop(str(chat_id))
    else:
        fileID = DB.DataBase.GetFile(Mafina.Mafina.DB, Mafina.Mafina.ResultSearch[str(chat_id)])
        Mafina.Mafina.KeyboardFormat[str(chat_id)] = {}
        for x in fileID:
            for y in range(len(x)):
                if str(x[y]) != "":
                    Mafina.Mafina.KeyboardFormat[str(chat_id)][Mafina.Mafina.NameFormat[y]] = x[y]

        keys = list(Mafina.Mafina.KeyboardFormat[str(chat_id)].keys())
        if len(keys) == 1:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["53"],
                                          message_id=update.callback_query.message.message_id)
            DownloadBook(update, context, Mafina.Mafina.KeyboardFormat[str(chat_id)][keys[0]], keys[0])
            Mafina.Mafina.KeyboardFormat.pop(str(chat_id))
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["52"], message_id=update.callback_query.message.message_id)
            context.bot.edit_message_reply_markup(chat_id=chat_id,
                                                  reply_markup=Keyboard.InlineKeyboard(keys, False),
                                                  message_id=update.callback_query.message.message_id)
            Mafina.Mafina.UseCommand[str(chat_id)] = "ConfirmTypeFile"

def DownloadBook(update, context, fileID, format, chat_id):
    file = context.bot.getFile(fileID)
    title = ("{0}{1}").format(str(Mafina.Mafina.ResultSearch[str(chat_id)]), format)
    file.download(title)
    context.bot.send_document(chat_id, open(title, 'rb'))
    Mafina.Mafina.ResultSearch.pop(str(chat_id))
    os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), title))

def AddBookInReadList(update, context, answer, chat_id):
    print(Mafina.Mafina.ResultSearch[str(chat_id)])
    DB.DataBase.AddBookInListRead(Mafina.Mafina.DB, chat_id, Mafina.Mafina.ResultSearch[str(chat_id)])
    context.bot.edit_message_text(chat_id=chat_id, text=answer["50"],
                                  message_id=update.callback_query.message.message_id)
    Mafina.Mafina.ResultSearch.pop(str(chat_id))

def SendListReadBooks(update, context, answer, lang, chat_id):
    if str(chat_id) in Mafina.Mafina.UseCommand.keys():
        if Mafina.Mafina.UseCommand[chat_id] == "GetBook":
            if update.callback_query.data == "Відміна пошуку":
                Cancel(update, context)
            val = Mafina.Mafina.ResultSearch[str(chat_id)][int(update.callback_query.data) - 1]
            Mafina.Mafina.ResultSearch[chat_id] = str(val)[3:]
            Mafina.Mafina.UseCommand.pop(str(chat_id))
            context.bot.edit_message_text(chat_id=chat_id, text=str(answer["60"] + "\n" +val),message_id=update.callback_query.message.message_id)
            context.bot.edit_message_reply_markup(chat_id=chat_id, reply_markup=Keyboard.InlineKeyboard(Mafina.Mafina.BookStateKeyboardDelete[lang], False),
                                                  message_id=update.callback_query.message.message_id)
    else:
        result = DB.DataBase.GetBookInReadList(Mafina.Mafina.DB, chat_id)
        value, key, val = RefactoringData(result)
        if len(value) == 0:
            context.bot.send_message(chat_id, answer["62"],
                                     reply_markup=Keyboard.InlineKeyboard(Mafina.Mafina.MenuBookKeyboard, False))
            Mafina.Mafina.UseCommand.pop(str(chat_id))
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=str(answer["56"] + "\n" + val),
                                          message_id=update.callback_query.message.message_id)
            context.bot.edit_message_reply_markup(chat_id=chat_id, reply_markup=Keyboard.InlineKeyboard(key, False),
                                                  message_id=update.callback_query.message.message_id)
            Mafina.Mafina.ResultSearch[chat_id] = value
            Mafina.Mafina.UseCommand[chat_id] = "GetBook"


def SearchBook(update, context, answer, lang, chat_id):
    if str(chat_id) in Mafina.Mafina.UseCommand.keys():
        if Mafina.Mafina.UseCommand[str(chat_id)] == "SearchViaName":
            result = DB.DataBase.SearchBook(Mafina.Mafina.DB, update.message.text)
            value, key, val = RefactoringData(result)
            if len(value) == 0:
                context.bot.send_message(chat_id, answer["54"], reply_markup=Keyboard.InlineKeyboard(Mafina.Mafina.MenuBookKeyboard[lang], False))
                Mafina.Mafina.UseCommand.pop(str(chat_id))
            elif len(value) == 1:
                context.bot.send_message(chat_id, answer["48"] + value[0], reply_markup=Keyboard.InlineKeyboard(Mafina.Mafina.BookStateKeyboard[lang], False))
                Mafina.Mafina.UseCommand.pop(str(chat_id))
                Mafina.Mafina.ResultSearch[str(chat_id)] = str(value[0])[3:]
            else:
                context.bot.send_message(chat_id, str(answer["49"]+"\n"+val), reply_markup=Keyboard.InlineKeyboard(key, False))
                Mafina.Mafina.ResultSearch[str(chat_id)] = value
                Mafina.Mafina.UseCommand[str(chat_id)] = "SeveralResult"

        elif Mafina.Mafina.UseCommand[str(chat_id)] == "SeveralResult":
            val = Mafina.Mafina.ResultSearch[str(chat_id)][int(update.callback_query.data)-1]
            v = val.split("—")
            Mafina.Mafina.ResultSearch[str(chat_id)] = str(v[0])[3:]
            Mafina.Mafina.UseCommand.pop(str(chat_id))
            context.bot.edit_message_text(chat_id=chat_id, text=answer["44"], message_id=update.callback_query.message.message_id)
            context.bot.send_message(chat_id, answer["48"] + str(val)[3:], reply_markup=Keyboard.InlineKeyboard(Mafina.Mafina.BookStateKeyboard[lang], False))
    else:
        context.bot.edit_message_text(chat_id=chat_id, text=answer["47"],
                                      message_id=update.callback_query.message.message_id)
        Mafina.Mafina.UseCommand[str(chat_id)] = "SearchViaName"

def SearchAuthor(update, context, answer, lang, chat_id):
    if chat_id in Mafina.Mafina.UseCommand.keys():
        if Mafina.Mafina.UseCommand[chat_id] == "SearchViaAuthor":
            result = DB.DataBase.SearchAuthor(Mafina.Mafina.DB, update.message.text)
            value, key, val = RefactoringData(result)
            if len(value) == 0:
                context.bot.send_message(chat_id, answer["57"], reply_markup=Keyboard.InlineKeyboard(Mafina.Mafina.MenuBookKeyboard[lang], False))
                Mafina.Mafina.UseCommand.pop(chat_id)
            else:
                context.bot.send_message(chat_id, str(answer["56"]+"\n"+val), reply_markup=Keyboard.InlineKeyboard(key, False))
                Mafina.Mafina.ResultSearch[chat_id] = value
                Mafina.Mafina.UseCommand[chat_id] = "GetBookViaAuthor"
        elif Mafina.Mafina.UseCommand[chat_id] == "GetBookViaAuthor":
            if update.callback_query.data == "Відміна пошуку":
                Cancel(update, context)
            val = Mafina.Mafina.ResultSearch[str(chat_id)][int(update.callback_query.data) - 1]
            result = DB.DataBase.GetBookViaAuthor(Mafina.Mafina.DB, val[3:])
            value, key, val = RefactoringData(result)
            Mafina.Mafina.ResultSearch[chat_id] = value
            context.bot.edit_message_text(chat_id=chat_id, text=str(answer["49"] + "\n" + val), message_id = update.callback_query.message.message_id)
            context.bot.edit_message_reply_markup(chat_id=chat_id, reply_markup= Keyboard.InlineKeyboard(key, False), message_id =update.callback_query.message.message_id)
            Mafina.Mafina.UseCommand[chat_id] = "SelectBookByAuthor"
        elif Mafina.Mafina.UseCommand[chat_id] == "SelectBookByAuthor":
            if update.callback_query.data == "Відміна пошуку":
                Cancel(update, context)
            val = Mafina.Mafina.ResultSearch[chat_id][int(update.callback_query.data) - 1]
            Mafina.Mafina.ResultSearch[chat_id] = str(val)[3:]
            Mafina.Mafina.UseCommand.pop(str(chat_id))
            context.bot.edit_message_text(chat_id=chat_id, text=str(answer["60"] + "\n" +val),message_id=update.callback_query.message.message_id)
            context.bot.edit_message_reply_markup(chat_id=chat_id, reply_markup=Keyboard.InlineKeyboard(Mafina.Mafina.BookStateKeyboard[lang], False),
                                                  message_id=update.callback_query.message.message_id)
    else:
        context.bot.edit_message_text(chat_id=chat_id, text=answer["55"], message_id=update.callback_query.message.message_id)
        Mafina.Mafina.UseCommand[str(chat_id)] = "SearchViaAuthor"

def CountBookInDB(update, context, chat_id):
    val = DB.DataBase.CountBook(Mafina.Mafina.DB)
    context.bot.edit_message_text(chat_id=chat_id, text=val, message_id=update.callback_query.message.message_id)

def RefactoringData(result):
    count = 1
    value, key, v = [], [], []
    val = ""
    for x in result:
        v.append(x[0])
        value.append(str(count) + ". " + x[0])
        key.append(str(count))
        if len(x)>1: val += str(count) + ". " + x[0]+"\nАвтор: "+x[1]+"\nМова: "+Mafina.Mafina.d[x[2]] + "\n\n"
        else: val += str(count) + ". " + x[0]+"\n"
        count += 1
    key.append("Відміна пошуку")
    return value, key, val

def UploadBook(update, context, answer, lang, chat_id):
    if str(chat_id) in Mafina.Mafina.UseCommand.keys():
        if Mafina.Mafina.UseCommand[str(chat_id)] == "Check":
            context.bot.send_message(chat_id, answer["43"],
                                     reply_markup=Keyboard.InlineKeyboard(Mafina.Mafina.ConfirmKeyboard[lang], False))
            data = (update.message.text).split('\n')
            Mafina.Mafina.Book[str(chat_id)] = Book(Name=data[0], Author=data[1])
            Mafina.Mafina.UseCommand.pop(str(chat_id))
            Mafina.Mafina.UseCommand[str(chat_id)] = "Confirm"
        elif Mafina.Mafina.UseCommand[str(chat_id)] == "Confirm":
            if(str(update.callback_query.data) == "Так" or str(update.callback_query.data) == "Yes"):
                Mafina.Mafina.UseCommand.pop(str(chat_id))
                context.bot.edit_message_text(chat_id=chat_id,text=answer["40"],
                                              message_id=update.callback_query.message.message_id)
                context.bot.edit_message_reply_markup(chat_id, reply_markup=Keyboard.InlineKeyboard(Mafina.Mafina.TranslateKeyboard, False),
                                                      message_id=update.callback_query.message.message_id)
                Mafina.Mafina.UseCommand[str(chat_id)] = "BookLang"
            else:
                Mafina.Mafina.UseCommand.pop(str(chat_id))
                Mafina.Mafina.Book.pop(str(chat_id))
                UploadBook(update, context)
        elif Mafina.Mafina.UseCommand[str(chat_id)] == "BookLang":
            Mafina.Mafina.Book[str(chat_id)].book_lang = Mafina.Mafina.b[update.callback_query.data]
            Mafina.Mafina.UseCommand.pop(str(chat_id))
            Mafina.Mafina.UseCommand[str(chat_id)] = "UploadFile"
            context.bot.edit_message_text(chat_id=chat_id, text=answer["42"],
                                          message_id=update.callback_query.message.message_id)
            context.bot.edit_message_reply_markup(chat_id, reply_markup = Keyboard.InlineKeyboard(Mafina.Mafina.CancelButton[lang], False),message_id=update.callback_query.message.message_id)
        elif Mafina.Mafina.UseCommand[str(chat_id)] == "UploadFile":
            Mafina.Mafina.Book[str(chat_id)].file_id = update.message.document.file_id
            Mafina.Mafina.Book[str(chat_id)].full_file_name = update.message.document.file_name
            DetectFormat(update, context)
            result = DB.DataBase.BookSystem(Mafina.Mafina.DB, Mafina.Mafina.Book[str(chat_id)])
            if result and Mafina.Mafina.Book[str(chat_id)].format in update.message.document.file_name:
                context.bot.send_message(chat_id, text=answer["45"])
            else:
                context.bot.send_message(chat_id, text=answer["46"])
            Mafina.Mafina.UseCommand.pop(str(chat_id))
            Mafina.Mafina.Book.pop(str(chat_id))
    else:
        context.bot.edit_message_text(chat_id=chat_id, text=answer["41"], message_id=update.callback_query.message.message_id)
        Mafina.Mafina.UseCommand[str(chat_id)] = "Check"

def Cancel(update, context, answer, chat_id):
    context.bot.edit_message_text(chat_id=chat_id, text=answer["51"], message_id=update.callback_query.message.message_id)
    Mafina.Mafina.UseCommand.pop(str(chat_id))
    Mafina.Mafina.Book.pop(str(chat_id))


def MenuBook(update, context, answer, lang):
    context.bot.send_message(update.message.chat_id, answer["39"], reply_markup=Keyboard.InlineKeyboard(Mafina.Mafina.MenuBookKeyboard[lang], False))

def FileStream(update, context):
    print(update)
    if str(update.message.chat_id) in Mafina.Mafina.UseCommand.keys():
        res = Mafina.Mafina.UseCommand[str(update.message.chat_id)]
        if res == "UploadFile": Thread.Thread(UploadBook, (update, context))

def DetectFormat(update, context):
    chat_id = Mafina.Mafina.GetChatID(update)
    if ".epub" in Mafina.Mafina.Book[str(chat_id)].full_file_name.lower():
        Mafina.Mafina.Book[str(chat_id)].format = ".epub"
    elif ".pdf"in Mafina.Mafina.Book[str(chat_id)].full_file_name.lower():
        Mafina.Mafina.Book[str(chat_id)].format = ".pdf"
    elif ".fb2"in Mafina.Mafina.Book[str(chat_id)].full_file_name.lower():
        Mafina.Mafina.Book[str(chat_id)].format = ".fb2"

def DeleteInReadList(update, context, answer, chat_id):
    DB.DataBase.DeleteBookInReadList(Mafina.Mafina.DB, chat_id, Mafina.Mafina.ResultSearch[chat_id])
    context.bot.edit_message_text(chat_id=chat_id, text=answer["63"], message_id=update.callback_query.message.message_id)