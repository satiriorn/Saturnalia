import os

class NewBook:
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        self.book_lang, self.file_id, self.format = None, None, None
        self.full_file_name = ""

class Book:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            Book._instance = super(Book, cls).__new__(cls)
            Book._mafina = M
            return Book._instance
    @classmethod
    def GetFile(self, update, context, answer, chat_id):
        print("GETFILE")
        if chat_id in self._mafina.UseCommand.keys():
            if self._mafina.UseCommand[chat_id] == "ConfirmTypeFile":
                context.bot.edit_message_text(chat_id=chat_id, text=answer["53"],
                                              message_id=update.callback_query.message.message_id)
                self.DownloadBook(update, context, self._mafina.KeyboardFormat[chat_id][update.callback_query.data], update.callback_query.data)
                self._mafina.UseCommand.pop(chat_id)
                self._mafina.KeyboardFormat.pop(chat_id)
        else:
            fileID = self._mafina._DB.GetFile(self._mafina.ResultSearch[chat_id])
            self._mafina.KeyboardFormat[chat_id] = {}
            for x in fileID:
                for y in range(len(x)):
                    if str(x[y]) != "":
                        self._mafina.KeyboardFormat[chat_id][self._mafina.NameFormat[y]] = x[y]
            keys = list(self._mafina.KeyboardFormat[chat_id].keys())
            if len(keys) == 1:
                context.bot.edit_message_text(chat_id=chat_id, text=answer["53"],
                                              message_id=update.callback_query.message.message_id)
                self.DownloadBook(update, context,self._mafina.KeyboardFormat[chat_id][keys[0]], keys[0])
                self._mafina.KeyboardFormat.pop(chat_id)
            else:
                context.bot.edit_message_text(chat_id=chat_id, text=answer["52"], message_id=update.callback_query.message.message_id)
                context.bot.edit_message_reply_markup(chat_id=chat_id,
                                                      reply_markup=self._mafina._keyboard.InlineKeyboard(keys, False),
                                                      message_id=update.callback_query.message.message_id)
                self._mafina.UseCommand[str(chat_id)] = "ConfirmTypeFile"
    @classmethod
    def DownloadBook(self, update, context, fileID, format, chat_id):
        file = context.bot.getFile(fileID)
        title = ("{0}{1}").format(str(self._mafina.ResultSearch[str(chat_id)]), format)
        file.download(title)
        context.bot.send_document(chat_id, open(title, 'rb'))
        self._mafina.ResultSearch.pop(str(chat_id))
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), title))
    @classmethod
    def AddBookInReadList(self, update, context, answer, chat_id):
        self._mafina._DB.AddBookInListRead(chat_id, self._mafina.ResultSearch[chat_id])
        context.bot.edit_message_text(chat_id=chat_id, text=answer["50"],
                                      message_id=update.callback_query.message.message_id)
        self._mafina.ResultSearch.pop(str(chat_id))
    @classmethod
    def SendListReadBooks(self, update, context, answer, lang, chat_id):
        if chat_id in self._mafina.UseCommand.keys():
            if self._mafina.UseCommand[chat_id] == "GetBook":
                if update.callback_query.data == "Відміна пошуку":
                    self.Cancel(update, context)
                val = self._mafina.ResultSearch[chat_id][int(update.callback_query.data) - 1]
                self._mafina.ResultSearch[chat_id] = str(val)[3:]
                self._mafina.UseCommand.pop(str(chat_id))
                context.bot.edit_message_text(chat_id=chat_id, text=str(answer["60"] + "\n" +val),message_id=update.callback_query.message.message_id)
                context.bot.edit_message_reply_markup(chat_id=chat_id,
                    reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.BookStateKeyboardDelete[lang], False),
                    message_id=update.callback_query.message.message_id)
        else:
            result = self._mafina._DB.GetBookInReadList(chat_id)
            value, key, val = self.RefactoringData(result)
            if len(value) == 0:
                context.bot.send_message(chat_id, answer["62"],
                                         reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.MenuBookKeyboard, False))
                self._mafina.UseCommand.pop(str(chat_id))
            else:
                context.bot.edit_message_text(chat_id=chat_id, text=str(answer["56"] + "\n" + val),
                                              message_id=update.callback_query.message.message_id)
                context.bot.edit_message_reply_markup(chat_id=chat_id, reply_markup=self._mafina._keyboard.InlineKeyboard(key, False),
                                                      message_id=update.callback_query.message.message_id)
                self._mafina.ResultSearch[chat_id] = value
                self._mafina.UseCommand[chat_id] = "GetBook"

    @classmethod
    def SearchBook(self, update, context, answer, lang, chat_id):
        if chat_id in self._mafina.UseCommand.keys():
            if self._mafina.UseCommand[chat_id] == "SearchViaName":
                result = self._mafina._DB.SearchBook(update.message.text)
                value, key, val = self.RefactoringData(result)
                if len(value) == 0:
                    context.bot.send_message(chat_id, answer["54"],
                                             reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.MenuBookKeyboard[lang], False))
                    self._mafina.UseCommand.pop(chat_id)
                elif len(value) == 1:
                    context.bot.send_message(chat_id, answer["48"] + value[0],
                                             reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.BookStateKeyboard[lang], False))
                    self._mafina.UseCommand.pop(chat_id)
                    self._mafina.ResultSearch[chat_id] = str(value[0])[3:]
                else:
                    context.bot.send_message(chat_id, str(answer["49"]+"\n"+val), reply_markup=self._mafina._keyboard.InlineKeyboard(key, False))
                    self._mafina.ResultSearch[chat_id] = value
                    self._mafina.UseCommand[chat_id] = "SeveralResult"

            elif self._mafina.UseCommand[chat_id] == "SeveralResult":
                val = self._mafina.ResultSearch[chat_id][int(update.callback_query.data)-1]
                v = val.split("—")
                self._mafina.ResultSearch[chat_id] = str(v[0])[3:]
                self._mafina.UseCommand.pop(chat_id)
                context.bot.edit_message_text(chat_id=chat_id, text=answer["44"], message_id=update.callback_query.message.message_id)
                context.bot.send_message(chat_id, answer["48"] + str(val)[3:],
                                         reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.BookStateKeyboard[lang], False))
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["47"],
                                          message_id=update.callback_query.message.message_id)
            self._mafina.UseCommand[chat_id] = "SearchViaName"
    @classmethod
    def SearchAuthor(self, update, context, answer, lang, chat_id):
        if chat_id in self._mafina.UseCommand.keys():
            if self._mafina.UseCommand[chat_id] == "SearchViaAuthor":
                result = self._mafina._DB.SearchAuthor(update.message.text)
                value, key, val = self.RefactoringData(result)
                if len(value) == 0:
                    context.bot.send_message(chat_id, answer["57"],
                                             reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.MenuBookKeyboard[lang], False))
                    self._mafina.UseCommand.pop(chat_id)
                else:
                    context.bot.send_message(chat_id, str(answer["56"]+"\n"+val), reply_markup=self._mafina._keyboard.InlineKeyboard(key, False))
                    self._mafina.ResultSearch[chat_id] = value
                    self._mafina.UseCommand[chat_id] = "GetBookViaAuthor"
            elif self._mafina.UseCommand[chat_id] == "GetBookViaAuthor":
                if update.callback_query.data == "Відміна пошуку":
                    self.Cancel(update, context)
                val = self._mafina.ResultSearch[chat_id][int(update.callback_query.data) - 1]
                result =self._mafina._DB.GetBookViaAuthor(val[3:])
                value, key, val = self.RefactoringData(result)
                self._mafina.ResultSearch[chat_id] = value
                context.bot.edit_message_text(chat_id=chat_id, text=str(answer["49"] + "\n" + val), message_id = update.callback_query.message.message_id)
                context.bot.edit_message_reply_markup(chat_id=chat_id,
                                                      reply_markup= self._mafina._keyboard.InlineKeyboard(key, False),
                                                      message_id =update.callback_query.message.message_id)
                self._mafina.UseCommand[chat_id] = "SelectBookByAuthor"
            elif self._mafina.UseCommand[chat_id] == "SelectBookByAuthor":
                if update.callback_query.data == "Відміна пошуку":
                    self.Cancel(update, context)
                val = self._mafina.ResultSearch[chat_id][int(update.callback_query.data) - 1]
                self._mafina.ResultSearch[chat_id] = str(val)[3:]
                self._mafina.UseCommand.pop(str(chat_id))
                context.bot.edit_message_text(chat_id=chat_id, text=str(answer["60"] + "\n" +val), message_id=update.callback_query.message.message_id)
                context.bot.edit_message_reply_markup(chat_id=chat_id,
                                                      reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.BookStateKeyboard[lang], False),
                                                      message_id=update.callback_query.message.message_id)
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["55"], message_id=update.callback_query.message.message_id)
            self._mafina.UseCommand[str(chat_id)] = "SearchViaAuthor"
    @classmethod
    def CountBookInDB(self, update, context, chat_id):
        val = self._mafina._DB.CountBook()
        context.bot.edit_message_text(chat_id=chat_id, text=val, message_id=update.callback_query.message.message_id)

    @classmethod
    def RefactoringData(self, result):
        count = 1
        value, key, v = [], [], []
        val = ""
        for x in result:
            v.append(x[0])
            value.append(str(count) + ". " + x[0])
            key.append(str(count))
            if len(x)>1: val += str(count) + ". " + x[0]+"\nАвтор: "+x[1]+"\nМова: "+self._mafina.d[x[2]] + "\n\n"
            else: val += str(count) + ". " + x[0]+"\n"
            count += 1
        key.append("Відміна пошуку")
        return value, key, val
    @classmethod
    def UploadBook(self, update, context, answer, lang, chat_id):
        if chat_id in self._mafina.Mafina.UseCommand.keys():
            if self._mafina.UseCommand[chat_id] == "Check":
                context.bot.send_message(chat_id, answer["43"],
                                         reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.ConfirmKeyboard[lang], False))
                data = (update.message.text).split('\n')
                self._mafina.Book[chat_id] = NewBook(Name=data[0], Author=data[1])
                self._mafina.UseCommand.pop(chat_id)
                self._mafina.UseCommand[chat_id] = "Confirm"
            elif self._mafina.UseCommand[chat_id] == "Confirm":
                if(str(update.callback_query.data) == "Так" or str(update.callback_query.data) == "Yes"):
                    self._mafina.UseCommand.pop(chat_id)
                    context.bot.edit_message_text(chat_id=chat_id,text=answer["40"],
                                                  message_id=update.callback_query.message.message_id)
                    context.bot.edit_message_reply_markup(chat_id, reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.TranslateKeyboard, False),
                                                          message_id=update.callback_query.message.message_id)
                    self._mafina.UseCommand[chat_id] = "BookLang"
                else:
                    self._mafina.UseCommand.pop(chat_id)
                    self._mafina.Book.pop(chat_id)
                    self.UploadBook(update, context, answer, lang, chat_id)
            elif self._mafina.UseCommand[str(chat_id)] == "BookLang":
                self._mafina.Book[str(chat_id)].book_lang =self._mafina._keyboard.b[update.callback_query.data]
                self._mafina.UseCommand.pop(str(chat_id))
                self._mafina.UseCommand[str(chat_id)] = "UploadFile"
                context.bot.edit_message_text(chat_id=chat_id, text=answer["42"],
                                              message_id=update.callback_query.message.message_id)
                context.bot.edit_message_reply_markup(chat_id,
                                              reply_markup = self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.CancelButton[lang], False),
                                              message_id=update.callback_query.message.message_id)
            elif self._mafina.UseCommand[str(chat_id)] == "UploadFile":
                self._mafina.Book[str(chat_id)].file_id = update.message.document.file_id
                self._mafina.Book[str(chat_id)].full_file_name = update.message.document.file_name
                self.DetectFormat(update, context)
                result = self._mafina._DB.BookSystem(self._mafina.Book[str(chat_id)])
                if result and self._mafina.Book[str(chat_id)].format in update.message.document.file_name:
                    context.bot.send_message(chat_id, text=answer["45"])
                else:
                    context.bot.send_message(chat_id, text=answer["46"])
                self._mafina.UseCommand.pop(str(chat_id))
                self._mafina.Book.pop(str(chat_id))
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["41"], message_id=update.callback_query.message.message_id)
            self._mafina.UseCommand[str(chat_id)] = "Check"
    @classmethod
    def Cancel(self, update, context, answer, chat_id):
        context.bot.edit_message_text(chat_id=chat_id, text=answer["51"], message_id=update.callback_query.message.message_id)
        self._mafina.UseCommand.pop(str(chat_id))
        self._mafina.Book.pop(str(chat_id))

    @classmethod
    def MenuBook(self, update, context, answer, lang):
        context.bot.send_message(update.message.chat_id, answer["39"],
                                 reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.MenuBookKeyboard[lang], False))

    @classmethod
    def DetectFormat(self, chat_id):
        if ".epub" in self._mafina.Book[str(chat_id)].full_file_name.lower():
            self._mafina.Book[str(chat_id)].format = ".epub"
        elif ".pdf"in self._mafina.Book[str(chat_id)].full_file_name.lower():
            self._mafina.Book[str(chat_id)].format = ".pdf"
        elif ".fb2"in self._mafina.Book[str(chat_id)].full_file_name.lower():
            self._mafina.Book[str(chat_id)].format = ".fb2"

    @classmethod
    def DeleteInReadList(self, update, context, answer, chat_id):
        self._mafina._DB.DeleteBookInReadList(chat_id, self._mafina.ResultSearch[chat_id])
        context.bot.edit_message_text(chat_id=chat_id, text=answer["63"], message_id=update.callback_query.message.message_id)