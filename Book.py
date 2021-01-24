import badge, Thread, DB, Keyboard, os

class Book:
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        self.book_lang = None
        self.file_id = None
        self.format = None
        self.full_file_name = ""

def GetFile(update, context):
    chat_id = badge.GetChatID(update)
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    if str(chat_id) in badge.UseCommand.keys():
        if badge.UseCommand[str(chat_id)] == "ConfirmTypeFile":
            context.bot.edit_message_text(chat_id=chat_id, text=answer["53"],
                                          message_id=update.callback_query.message.message_id)
            DownloadBook(update, context, badge.KeyboardFormat[str(chat_id)][update.callback_query.data], update.callback_query.data)
            badge.UseCommand.pop(str(chat_id))
            badge.KeyboardFormat.pop(str(chat_id))
    else:
        fileID = DB.DataBase.GetFile(badge.DB, badge.ResultSearch[str(chat_id)])
        badge.KeyboardFormat[str(chat_id)] = {}
        for x in fileID:
            for y in range(len(x)):
                if str(x[y]) != "":
                    badge.KeyboardFormat[str(chat_id)][badge.NameFormat[y]] = x[y]

        keys = list(badge.KeyboardFormat[str(chat_id)].keys())
        if len(keys) == 1:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["53"],
                                          message_id=update.callback_query.message.message_id)
            DownloadBook(update, context, badge.KeyboardFormat[str(chat_id)][keys[0]], keys[0])
            badge.KeyboardFormat.pop(str(chat_id))
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["52"], message_id=update.callback_query.message.message_id)
            context.bot.edit_message_reply_markup(chat_id,
                                                  reply_markup=Keyboard.InlineKeyboard(keys, False),
                                                  message_id=update.callback_query.message.message_id)
            badge.UseCommand[str(chat_id)] = "ConfirmTypeFile"

def DownloadBook(update, context, fileID, format):
    chat_id = badge.GetChatID(update)
    file = context.bot.getFile(fileID)
    title = ("{0}{1}").format(str(badge.ResultSearch[str(chat_id)]), format)
    file.download(title)
    context.bot.send_document(chat_id, open(title, 'rb'))
    badge.ResultSearch.pop(str(chat_id))
    os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), title))

def AddBookInReadList(update, context):
    chat_id = badge.GetChatID(update)
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    print(badge.ResultSearch[str(chat_id)])
    DB.DataBase.AddBookInListRead(badge.DB, chat_id, badge.ResultSearch[str(chat_id)])
    context.bot.edit_message_text(chat_id=chat_id, text=answer["50"],
                                  message_id=update.callback_query.message.message_id)
    badge.ResultSearch.pop(str(chat_id))

def SearchBook(update,context):
    chat_id = badge.GetChatID(update)
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    if str(chat_id) in badge.UseCommand.keys():
        if badge.UseCommand[str(chat_id)] == "SearchViaName":
            result = DB.DataBase.SearchBook(badge.DB, update.message.text)
            value = []
            val = ""
            for x in result:
                for j in range(len(x)):
                    value.append(str(x[j]))
            if len(value)==1:
                context.bot.send_message(chat_id, answer["48"] + value[0],
                                         reply_markup=Keyboard.InlineKeyboard(badge.BookStateKeyboard, False))
                badge.UseCommand.pop(str(chat_id))
                badge.ResultSearch[str(chat_id)] = value[0]
            else:
                for x in result:
                    val +=str(x)+"\n"

                context.bot.send_message(chat_id, answer["49"] + val,
                                         reply_markup=Keyboard.InlineKeyboard(value, False))
                print(value)
                badge.UseCommand.pop(str(chat_id))
                badge.UseCommand[str(chat_id)] = "SeveralResult"

        elif badge.UseCommand[str(chat_id)] == "SeveralResult":
            badge.ResultSearch[str(chat_id)] = str(update.callback_query.data)
            badge.UseCommand.pop(str(chat_id))
            context.bot.edit_message_text(chat_id=chat_id, text=answer["44"],
                                          message_id=update.callback_query.message.message_id)
            context.bot.send_message(chat_id, answer["48"] + update.callback_query.data,
                                     reply_markup=Keyboard.InlineKeyboard(badge.BookStateKeyboard, False))
    else:
        context.bot.edit_message_text(chat_id=chat_id, text=answer["47"],
                                      message_id=update.callback_query.message.message_id)
        badge.UseCommand[str(chat_id)] = "SearchViaName"

def UploadBook(update, context):
    chat_id = badge.GetChatID(update)
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    if str(chat_id) in badge.UseCommand.keys():
        if badge.UseCommand[str(chat_id)] == "Check":
            context.bot.send_message(chat_id, answer["43"],
                                     reply_markup=Keyboard.InlineKeyboard(badge.ConfirmKeyboard , False))
            data = (update.message.text).split('\n')
            badge.Book[str(chat_id)] = Book(Name=Str(data[0]), Author=Str(data[1]))
            badge.UseCommand.pop(str(chat_id))
            badge.UseCommand[str(chat_id)] = "Confirm"
        elif badge.UseCommand[str(chat_id)] == "Confirm":
            if(str(update.callback_query.data) =="Так"):
                badge.UseCommand.pop(str(chat_id))
                context.bot.edit_message_text(chat_id=chat_id,text=answer["40"],
                                              message_id=update.callback_query.message.message_id)
                context.bot.edit_message_reply_markup(chat_id, reply_markup=Keyboard.InlineKeyboard(badge.TranslateKeyboard, False),
                                                      message_id=update.callback_query.message.message_id )
                badge.UseCommand[str(chat_id)] = "BookLang"
            else:
                badge.UseCommand.pop(str(chat_id))
                badge.Book.pop(str(chat_id))
                UploadBook(update, context)
        elif badge.UseCommand[str(chat_id)] == "BookLang":
            badge.Book[str(chat_id)].book_lang = Str(badge.b[update.callback_query.data])
            badge.UseCommand.pop(str(chat_id))
            badge.UseCommand[str(chat_id)] = "UploadFile"
            context.bot.edit_message_text(chat_id=chat_id, text=answer["42"],
                                          message_id=update.callback_query.message.message_id)
            context.bot.edit_message_reply_markup(chat_id, reply_markup = Keyboard.InlineKeyboard(badge.CancelButton, False),message_id=update.callback_query.message.message_id)
        elif badge.UseCommand[str(chat_id)] == "UploadFile":
            badge.Book[str(chat_id)].file_id = Str(update.message.document.file_id)
            badge.Book[str(chat_id)].full_file_name = update.message.document.file_name
            DetectFormat(update, context)
            result = DB.DataBase.BookSystem(badge.DB, badge.Book[str(chat_id)])
            if result and  badge.Book[str(chat_id)].format in update.message.document.file_name:
                context.bot.send_message(chat_id, text=answer["45"])
            else:
                context.bot.send_message(chat_id, text=answer["46"])
            badge.UseCommand.pop(str(chat_id))
            badge.Book.pop(str(chat_id))
    else:
        context.bot.edit_message_text(chat_id=chat_id, text=answer["41"], message_id=update.callback_query.message.message_id)
        badge.UseCommand[str(chat_id)] = "Check"

def Str(string):
    x = '"'+string+'"'
    return str(x)

def Cancel(update, context):
    chat_id = badge.GetChatID(update)
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    badge.UseCommand.pop(str(chat_id))
    badge.Book.pop(str(chat_id))
    context.bot.edit_message_text(chat_id=chat_id, text=answer["51"],
                                  message_id=update.callback_query.message.message_id)
def MenuBook(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    context.bot.send_message(update.message.chat_id, answer["39"], reply_markup=Keyboard.InlineKeyboard(badge.MenuBookKeyboard, False))

def MonitorDoc(update, context):
    print(update)
    if str(update.message.chat_id) in badge.UseCommand.keys():
        res = badge.UseCommand[str(update.message.chat_id)]
        if res == "UploadFile": Thread.Thread(UploadBook, (update, context))

def DetectFormat(update, context):
    chat_id = badge.GetChatID(update)
    if ".epub" in badge.Book[str(chat_id)].full_file_name.lower():
        badge.Book[str(chat_id)].format = ".epub"
    elif ".pdf"in badge.Book[str(chat_id)].full_file_name.lower():
        badge.Book[str(chat_id)].format = ".pdf"
    elif ".fb2"in badge.Book[str(chat_id)].full_file_name.lower():
        badge.Book[str(chat_id)].format = ".fb2"