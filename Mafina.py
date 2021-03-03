import Thread, Quotes, StandartCommand, weather, Evtuh,  CreateVoice, DogAndCat, InlineQuery, os, Meme, Youtube, Translate, DB, Keyboard, Setting,  Cut, File, Book
from telegram.ext import Updater, MessageHandler, Filters, InlineQueryHandler, CallbackQueryHandler

class Mafina(object):
    _instance, _DB, job, _translator, _keyboard, _weather, _voice, _std, _animal, _meme, = None, None, None, None, None, None, None, None, None, None
    _youtube, _setting, _cut, _book, _file = None, None, None, None, None
    UseCommand, CutFile, jobchat, Book, ResultSearch, KeyboardFormat, Users = {}, {}, {}, {}, {}, {}, {}
    NameFormat = [".epub", ".fb2", ".pdf"]
    fileformat = {".epub": "file_id_epub", ".fb2": "file_id_fb2", ".pdf": "file_id_pdf"}

    def __new__(cls):
        if not hasattr(cls, '_inst'):
            Mafina._instance = super(Mafina, cls).__new__(cls)
            return Mafina._instance

    def __init__(self):
        self.updater = Updater(os.getenv("TOKEN"), use_context=True)
        Mafina.job, Mafina._DB, Mafina._keyboard, Mafina._weather = self.updater.job_queue, DB.DataBase(self), Keyboard.Keyboard(), weather.Weather(self)
        Mafina._voice, Mafina._std, Mafina._animal = CreateVoice.Voice(self), StandartCommand.StandartCommand(self), DogAndCat.Animal(self)
        Mafina._meme, Mafina._youtube, Mafina._setting, Mafina._cut = Meme.Meme(self), Youtube.Youtube(self), Setting.SettingMafina(self), Cut.Cut(self)
        Mafina._book, Mafina._file = Book.Book(self), File.File(self)
        self.dispatcher = self.updater.dispatcher
        self.CreateHandler()
        self.run()

    def CreateHandler(self):
        dispatchermafina_handler = MessageHandler(Filters.command|Filters.text, Mafina.Dispatcher)
        callback_query_handler = CallbackQueryHandler(Mafina.Dispatcher)
        file_message_handler = MessageHandler(Filters.audio | Filters.video | Filters.animation | Filters.document, Mafina.DispatcherFile)
        self.dispatcher.add_handler(dispatchermafina_handler)
        self.dispatcher.add_handler(callback_query_handler)
        self.dispatcher.add_handler(file_message_handler)
        #self.dispatcher.add_handler(InlineQueryHandler(InlineQuery.inlinequery))

    def run(self):
        self._meme.StartSystemMeme()
        self._weather.StartSysWeather()
        self._animal.StartSysAnimal()
        self.updater.start_polling(timeout=99000, poll_interval=3)
        self.updater.idle()

    @classmethod
    def DispatcherFile(self, update, context):
        chat_id = self._instance.GetChatID(update)
        if chat_id in self._instance.Users.keys():
            answer, lang = self._instance.Users[chat_id].answer, self._instance.Users[chat_id].lang
            self._file.file(update, context, answer, lang, chat_id)
        else:
            self._instance.Users[chat_id] = User(chat_id, self._instance)
            self._instance.DispatcherFile(update, context)

    @classmethod
    def Dispatcher(self, update, context):
        print(update)
        chat_id =self._instance.GetChatID(update)
        if chat_id in self._instance.Users.keys():
            answer, lang = self._instance.Users[chat_id].answer, self._instance.Users[chat_id].lang
            text = self._instance.data(update)
            print(text)
            if text == "/start": Thread.Thread(self._std.start(update, context, answer, chat_id))
            elif text == "/help": Thread.Thread(self._std.help, (update, context, answer))
            elif text == "/weather": Thread.Thread(self._weather.weather, (update, context, answer))
            elif text == "/evtuh": Thread.Thread(Evtuh.Evtuh, (update, context))
            elif text == "/voice": Thread.Thread(self._voice.voice, (update, context, answer, chat_id))
            elif text == "/dog": Thread.Thread(self._animal.Dog_photo, (update, context, answer))
            elif text == "/cat": Thread.Thread(self._animal.Cat_photo, (update, context, answer))
            elif text == "/sheva": Thread.Thread(Quotes.ShevchenkoStyle, (update, context))
            elif text == "/meme": Thread.Thread(self._meme.Get_meme, (update, context,  answer))
            elif text == "/youtube": Thread.Thread(self._youtube.Start, (update, context, answer, lang))
            elif text == "/settingbot": Thread.Thread(self._setting.ShowSetting, (update, context, answer, chat_id, lang))
            elif text == "/rest": Thread.Thread(self._std.Rest, (update, context, answer, lang, chat_id))
            elif text == "/cut": Thread.Thread(self._cut.CutStart, (update, context, answer, lang))
            elif text == "/convert": Thread.Thread(self._std.convert, (update, context, answer, chat_id))
            elif text == "/book": Thread.Thread(self._book.MenuBook, (update, context, answer, lang))
            print(self._instance.UseCommand.keys())
            if chat_id in self._instance.UseCommand.keys():
                res = self._instance.UseCommand[chat_id]
                print(res)
                if res == "Audio": Thread.Thread(self._youtube.Get_Audio, (update, context, answer, chat_id))
                elif res == "Video": Thread.Thread(self._youtube.Get_Video, (update, context, answer, chat_id))
                elif res == "CutAudio": Thread.Thread(self._cut.CutAudio, (update, context, answer, chat_id))
                elif res == "CutVideo": Thread.Thread(self._cut.CutVideo, (update, context, answer, chat_id))
                elif res == "CreateVoice": Thread.Thread(self._voice.voice, (update, context, answer, chat_id))
                elif res == "Translate": Thread.Thread(Translate.translate, (update, context))
                elif res == "GetCutVideo": Thread.Thread(self._cut.GetCutStart, (update, context, answer, chat_id))
                elif res == "CutEnd": Thread.Thread(self._cut.Cut, (update, context, chat_id))
                elif res == "Check" or res == "Confirm" or res == "BookLang" or res == "FormatBook":
                    Thread.Thread(self._book.UploadBook, (update, context, answer, lang, chat_id))
                elif res == "SearchViaName": Thread.Thread(self._book.SearchBook, (update, context, answer, lang, chat_id))
                elif res == "SearchViaAuthor": Thread.Thread(self._book.SearchAuthor, (update, context, answer, lang, chat_id))
                elif res == "Rest": Thread.Thread(self._std.Rest, (update, context, answer, lang, chat_id, False))
                elif res == "MemeChange": Thread.Thread(self._meme.MoreMeme, (update, context, lang, chat_id))
                elif res == "SettingTranslate": Thread.Thread(self._setting.SettingTranslate, (update, context, answer, chat_id))
                #elif res == "Dologusha": Thread.Thread(Dologusha.start, (update, context))
                elif res == "LangBot":
                    Thread.Thread(self._setting.LanguageBot, (update, context, answer, chat_id))
                    del self._instance.Users[chat_id]
                    self._instance.Users.pop(chat_id)
                    self._instance.Dispatcher(update, context)
                elif res == "SeveralResult": Thread.Thread(self._book.SearchBook, (update, context, answer, lang, chat_id))
                elif res == "ConfirmTypeFile": Thread.Thread(self._book.GetFile, (update, context, answer, chat_id))
                elif res == "GetBookViaAuthor" or res == "SelectBookByAuthor":
                    Thread.Thread(self._book.SearchAuthor, (update, context, answer, lang, chat_id))
                elif res == "GetBook": Thread.Thread(self._book.SendListReadBooks, (update, context, answer, lang, chat_id))
                elif res == "ChangeSysAnimal": Thread.Thread(self._animal.SysAnimal, (update, context, answer, lang, chat_id))
                elif text == self._keyboard.CancelButton[lang][0]:Thread.Thread(self._book.Cancel, (update, context, answer, chat_id))
            elif text == "погода":Thread.Thread(self._weather.CurrentWeather, (update, context, answer))
            elif text == "котик": Thread.Thread(self._animal.Cat_photo, (update, context, answer))
            elif text == "мем": Thread.Thread(self._meme.Get_meme, (update, context,  answer))
            elif text == "animal": Thread.Thread(self._file.SendFile, (update, context))
            elif '?' in text: Thread.Thread(self._std.question, (update, context, answer))
            elif text == "0": Thread.Thread(Thread.Thread(self._setting.SettingTranslate, (update, context, answer, chat_id)))
            elif text == "1":Thread.Thread(self._setting.LanguageBot, (update, context, answer, chat_id))
            elif text == "2": Thread.Thread(self._weather.StateWeather, (update, context, answer, chat_id))
            elif text == "3": Thread.Thread(self._animal.SysAnimal, (update, context, answer, lang, chat_id))
            elif text == "4": Thread.Thread(self._meme.CountMem, (update, context, answer, lang))
            elif text == "5": Thread.Thread(self._setting.SettingAnswer, (update, context, answer, chat_id))
            elif text == self._keyboard.YoutubeKeyboard[lang][0]: Thread.Thread(self._youtube.Get_Video, (update, context, answer, chat_id))
            elif text == self._keyboard.YoutubeKeyboard[lang][1]: Thread.Thread(self._youtube.Get_Audio, (update, context, answer, chat_id))
            elif text == self._keyboard.CutKeyboard[lang][0]: Thread.Thread(self._cut.CutVideo, (update, context, answer, chat_id))
            elif text == self._keyboard.CutKeyboard[lang][1]: Thread.Thread(self._cut.CutAudio, (update, context, answer, chat_id))
            elif text ==self._keyboard.YoutubeKeyboard[lang][2]: Thread.Thread(self._cut.GetCutStart, ( update, context, answer, chat_id))
            elif text == self._keyboard.CancelButton[lang][0]: Thread.Thread(self._book.Book.Cancel, (update, context, answer, chat_id))
            elif text == self._keyboard.MenuBookKeyboard[lang][2]: Thread.Thread(self._book.SearchBook, (update, context, answer, lang, chat_id))
            elif text == self._keyboard.MenuBookKeyboard[lang][0]: Thread.Thread(self._book.UploadBook, (update, context, answer, lang, chat_id))
            elif text == self._keyboard.BookStateKeyboard[lang][1]: Thread.Thread(self._book.GetFile, (update, context, answer, chat_id))
            elif text == self._keyboard.MenuBookKeyboard[lang][1]: Thread.Thread(self._book.SearchAuthor, (update, context, answer, lang, chat_id))
            elif text == self._keyboard.MenuBookKeyboard[lang][3]: Thread.Thread(self._book.CountBookInDB, (update, context, chat_id))
            elif text == self._keyboard.BookStateKeyboard[lang][0]: Thread.Thread(self._book.AddBookInReadList, (update, context, answer, chat_id))
            elif text == self._keyboard.MenuBookKeyboard[lang][4]: Thread.Thread(self._book.SendListReadBooks, (update, context, answer, lang, chat_id))
            elif text == self._keyboard.BookStateKeyboardDelete[lang][0]:Thread.Thread(self._book.DeleteInReadList, (update, context, answer, chat_id))
            else: Thread.Thread(self._setting.ExistentialResponse, (update, context, answer, chat_id))
                   #"/Translate": Translate.translate(update, context, answer, chat_id), ,
        else:
            self._instance.Users[chat_id] = User(chat_id, self._instance)
            self._instance.Dispatcher(update, context)

    def data(self, update):
        try: return str(update.message.text).lower()
        except Exception: return str(update.callback_query.data)
    def GetChatID(self, update):
        try: return str(update.callback_query.message.chat_id)
        except Exception:  return str(update.message.chat_id)

class User():
    def __init__(self, chat_id, mafina):
        self.chat_id = chat_id
        self.answer, self.lang = mafina._DB.GetJsonLanguageBot(chat_id)

Mafina()