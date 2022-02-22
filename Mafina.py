import Thread, Cryptocurrency, Quotes, StandartCommand, weather, Evtuh,  CreateVoice, DogAndCat, InlineQuery, os, Meme, Youtube, Translate, DB, Keyboard, Setting,  \
    Cut, File, Book, Cancel, Hunter_of_BinanceAnnouncements, TextGen
from telegram.ext import Updater, MessageHandler, Filters, InlineQueryHandler, CallbackQueryHandler, ChosenInlineResultHandler
from googletrans import Translator

class Mafina(object):
    _instance, _DB, job, _translator, _keyboard, _weather, _voice, _std, _animal, _meme = None, None, None, None, None, None, None, None, None, None
    _youtube, _setting, _cut, _book, _file, _translate, _inline, _cancel, _binance, _hunter = None, None, None, None, None, None, None, None, None, None
    _textgen = None
    UseCommand, CutFile, jobchat, Book, ResultSearch, KeyboardFormat, Users, ResultInline = {}, {}, {}, {}, {}, {}, {}, {}
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
        Mafina._book, Mafina._file, Mafina._translate, Mafina._inline = Book.Book(self), File.File(self), Translate.Translate(self), InlineQuery.Inline(self)
        Mafina._translator, Mafina._cancel, Mafina._binance, Mafina._hunter = Translator(), Cancel.Cancel(self), Cryptocurrency.Binance(self), Hunter_of_BinanceAnnouncements.Hunter(self)
        Mafina._textgen = TextGen.TextGeneration(self)
        self.dispatcher = self.updater.dispatcher
        self.CreateHandler()
        self.run()

    def CreateHandler(self):
        dispatchermafina_handler = MessageHandler(Filters.command|Filters.text, Mafina.Dispatcher)
        callback_query_handler = CallbackQueryHandler(Mafina.Dispatcher)
        file_message_handler = MessageHandler(Filters.audio | Filters.video | Filters.animation | Filters.document, Mafina.DispatcherFile)
        result_chosen_handler = ChosenInlineResultHandler(Mafina.DispatcherInline)
        self.dispatcher.add_handler(dispatchermafina_handler)
        self.dispatcher.add_handler(callback_query_handler)
        self.dispatcher.add_handler(file_message_handler)
        self.dispatcher.add_handler(result_chosen_handler)
        self.dispatcher.add_handler(InlineQueryHandler(Mafina._inline.inlinequery))

    def run(self):
        #Thread.Thread(self._hunter.HunterListing, ())
        #self._meme.StartSystemMeme()
        #self._weather.StartSysWeather()
        #self._animal.StartSysAnimal()
        #self._binance.Start_Crypto_job()
        self.updater.start_polling(timeout=1990000, poll_interval=1)
        self.updater.idle()

    @classmethod
    def DispatcherFile(self, update, context):
        chat_id = self._instance.GetChatID(update)  
        if chat_id in self._instance.Users.keys():
            answer, lang = self._instance.Users[chat_id].answer, self._instance.Users[chat_id].lang
            self._file.file(update, context, answer, lang, chat_id)
        else:
            self._instance.Users[chat_id] = User(chat_id, self._instance, update)
            self._instance.DispatcherFile(update, context)

    @classmethod
    def DispatcherInline(self, update, context):
        result = update.chosen_inline_result
        chat_id = result.from_user.id
        if chat_id in self._instance.Users.keys():
            answer, lang = self._instance.Users[chat_id].answer, self._instance.Users[chat_id].lang
            print(result.result_id)
            self._instance.UseCommand[chat_id] = "ChooseQuality"
            self._youtube.Get_Audio(self._instance.ResultInline[chat_id][int(result.result_id)]['input_message_content']['message_text'],
                                    context, answer, chat_id, inline=True)
        else:
            self._instance.Users[chat_id] = User(chat_id, self._instance, update)
            self._instance.DispatcherInline(update, context)

    @classmethod
    def Dispatcher(self, update, context):
        chat_id =self._instance.GetChatID(update)
        if chat_id in self._instance.Users.keys():
            answer, lang = self._instance.Users[chat_id].answer, self._instance.Users[chat_id].lang
            if 'reply_to_message' in str(update) and 'IMafinabot' in str(update):
                update.message.reply_text(self._textgen.generate_by_prefix(str(update.message.text)))
                return 0
            text = self._instance.data(update)
            if self._textgen.generate_by_prefix_city(update, context, text): return 0
            if "/cancel" in text: Thread.Thread(self._cancel.cancel, (update, context, answer, chat_id))
            if chat_id in self._instance.UseCommand.keys():
                res = self._instance.UseCommand[chat_id]
                Process ={
                "Audio": lambda: Thread.Thread(self._youtube.Get_Audio, (update, context, answer, chat_id)),
                "ChooseQuality": lambda: Thread.Thread(self._youtube.Get_Audio, (update, context, answer, chat_id)),
                "Video": lambda: Thread.Thread(self._youtube.Get_Video, (update, context, answer, chat_id)),
                "CutAudio": lambda: Thread.Thread(self._cut.CutAudio, (update, context, answer, chat_id)),
                "CutVideo": lambda: Thread.Thread(self._cut.CutVideo, (update, context, answer, chat_id)),
                "CreateVoice" : lambda: Thread.Thread(self._voice.voice, (update, context, answer, chat_id, text)),
                "Translate": lambda: Thread.Thread(self._translate.translate, (update, context, answer, chat_id)),
                "GetCutVideo": lambda: Thread.Thread(self._cut.GetCutStart, (update, context, answer, chat_id)),
                "CutEnd": lambda: Thread.Thread(self._cut.Cut, (update, context, chat_id)),
                "Check": lambda: Thread.Thread(self._book.UploadBook, (update, context, answer, lang, chat_id)),
                "Confirm": lambda: Thread.Thread(self._book.UploadBook, (update, context, answer, lang, chat_id)),
                "BookLang": lambda: Thread.Thread(self._book.UploadBook, (update, context, answer, lang, chat_id)),
                "FormatBook": lambda: Thread.Thread(self._book.UploadBook, (update, context, answer, lang, chat_id)),
                "SearchViaName": lambda: Thread.Thread(self._book.SearchBook, (update, context, answer, lang, chat_id)),
                "SearchViaAuthor": lambda: Thread.Thread(self._book.SearchAuthor, (update, context, answer, lang, chat_id)),
                "Rest": lambda: Thread.Thread(self._std.Rest, (update, context, answer, lang, chat_id, False)),
                "MemeChange": lambda: Thread.Thread(self._meme.MoreMeme, (update, context, lang, chat_id)),
                "SettingTranslate": lambda: Thread.Thread(self._setting.SettingTranslate, (update, context, answer, chat_id)),
                "SeveralResult": lambda: Thread.Thread(self._book.SearchBook, (update, context, answer, lang, chat_id)),
                "ConfirmTypeFile": lambda: Thread.Thread(self._book.GetFile, (update, context, answer, chat_id)),
                "GetBookViaAuthor": lambda: Thread.Thread(self._book.SearchAuthor, (update, context, answer, lang, chat_id)),
                "SelectBookByAuthor": lambda: Thread.Thread(self._book.SearchAuthor, (update, context, answer, lang, chat_id)),
                "GetBook": lambda: Thread.Thread(self._book.SendListReadBooks, (update, context, answer, lang, chat_id)),
                "ChangeSysAnimal": lambda: Thread.Thread(self._animal.SysAnimal, (update, context, answer, lang, chat_id)),
                "LangBot": lambda: Thread.Thread(self._setting.LanguageBot, (update, context, answer, chat_id)),
                "GetPair": lambda: Thread.Thread(self._binance.Add_Pair, (update, context, answer, chat_id)),
                "DeletePair": lambda: Thread.Thread(self._binance.Delete_Pair, (update, context, answer, chat_id)),
                self._keyboard.CancelButton[lang][0]: lambda: Thread.Thread(self._book.Cancel, (update, context, answer, chat_id)),
                self._keyboard.BookStateKeyboard[lang][2]: lambda: Thread.Thread(self._book.Cancel, (update, context, answer, chat_id))
                }
                if res in Process.keys():Process[res]()
                if text in Process.keys(): Process[text]()
                return
            CommandTxtButton = {
                "/help": lambda: Thread.Thread(self._std.help, (update, context, answer)),
                "/evtuh": lambda: Thread.Thread(Evtuh.Evtuh, (update, context)),
                "/start": lambda: Thread.Thread(self._std.start(update, context, answer, chat_id)),
                "/weather": lambda: Thread.Thread(self._weather.weather, (update, context, answer)),
                "/voice":lambda: Thread.Thread(self._voice.voice, (update, context, answer, chat_id)),
                "/dog": lambda: Thread.Thread(self._animal.Dog_photo, (update, context, answer)),
                "/binance": lambda: Thread.Thread(self._binance.Menu_Binance, (update, context, answer, lang)),
                ("/cat", "котик"): lambda: Thread.Thread(self._animal.Cat_photo, (update, context, answer)),
                "/sheva": lambda: Thread.Thread(Quotes.ShevchenkoStyle, (update, context)),
                ("/meme", "мем"): lambda: Thread.Thread(self._meme.Get_meme, (update, context, answer)),
                "/youtube": lambda: Thread.Thread(self._youtube.Start, (update, context, answer, lang)),
                "/settingbot": lambda: Thread.Thread(self._setting.ShowSetting, (update, context, answer, chat_id, lang)),
                "/rest": lambda: Thread.Thread(self._std.Rest, (update, context, answer, lang, chat_id)),
                "/cut": lambda: Thread.Thread(self._cut.CutStart, (update, context, answer, lang)),
                "/convert": lambda: Thread.Thread(self._std.convert, (update, context, answer, chat_id)),
                "/book": lambda: Thread.Thread(self._book.MenuBook, (update, context, answer, lang)),
                "/translate": lambda: Thread.Thread(self._translate.translate, (update, context, answer, chat_id)),
                "/gen": lambda: update.message.reply_text(self._instance._textgen.generate_random()),
                "/genvoice": lambda: Thread.Thread(self._voice.gen_voice, (update, context, answer, chat_id, self._instance._textgen.generate_random())),
                "погода": lambda: Thread.Thread(self._weather.CurrentWeather, (update, context, answer)),
                "animal": lambda: Thread.Thread(self._file.SendFile, (update, context)),
                "0": lambda: Thread.Thread(Thread.Thread(self._setting.SettingTranslate, (update, context, answer, chat_id))),
                "1": lambda: Thread.Thread(self._setting.LanguageBot, (update, context, answer, chat_id)),
                "2": lambda: Thread.Thread(self._weather.StateWeather, (update, context, answer, chat_id)),
                "3": lambda: Thread.Thread(self._animal.SysAnimal, (update, context, answer, lang, chat_id)),
                "4": lambda: Thread.Thread(self._meme.CountMem, (update, context, answer, lang)),
                "5": lambda: Thread.Thread(self._setting.SettingAnswer, (update, context, answer, chat_id)),
                "6": lambda: Thread.Thread(self._meme.NightMode, (update, context, answer, chat_id)),
                self._keyboard.MenuBinanceKeyboard[lang][0]: lambda: Thread.Thread(self._binance.Add_Pair, (update, context, answer, chat_id)),
                self._keyboard.MenuBinanceKeyboard[lang][1]: lambda: Thread.Thread(self._binance.Delete_Pair, (update, context, answer, chat_id)),
                self._keyboard.MenuBinanceKeyboard[lang][2]: lambda: Thread.Thread(self._binance.Display_selected_pairs, (update, context, answer, chat_id)),
                self._keyboard.YoutubeKeyboard[lang][0]: lambda: Thread.Thread(self._youtube.Get_Video,(update, context, answer, chat_id)),
                self._keyboard.YoutubeKeyboard[lang][1]: lambda: Thread.Thread(self._youtube.Get_Audio,(update, context, answer, chat_id)),
                self._keyboard.CutKeyboard[lang][0]: lambda: Thread.Thread(self._cut.CutVideo,(update, context, answer, chat_id)),
                self._keyboard.CutKeyboard[lang][1]: lambda: Thread.Thread(self._cut.CutAudio,(update, context, answer, chat_id)),
                self._keyboard.YoutubeKeyboard[lang][2]: lambda: Thread.Thread(self._cut.GetCutStart,(update, context, answer, chat_id)),
                (self._keyboard.CancelButton[lang][0], self._keyboard.BookStateKeyboard[lang][2]):lambda: Thread.Thread(self._book.Cancel, (update, context, answer, chat_id)),
                self._keyboard.MenuBookKeyboard[lang][2]: lambda: Thread.Thread(self._book.SearchBook, (update, context, answer, lang, chat_id)),
                self._keyboard.MenuBookKeyboard[lang][0]: lambda: Thread.Thread(self._book.UploadBook, (update, context, answer, lang, chat_id)),
                self._keyboard.BookStateKeyboard[lang][1]: lambda: Thread.Thread(self._book.GetFile,(update, context, answer, chat_id)),
                self._keyboard.MenuBookKeyboard[lang][1]: lambda: Thread.Thread(self._book.SearchAuthor, (update, context, answer, lang, chat_id)),
                self._keyboard.MenuBookKeyboard[lang][3]: lambda: Thread.Thread(self._book.CountBookInDB, (update, context, chat_id)),
                self._keyboard.BookStateKeyboard[lang][0]: lambda: Thread.Thread(self._book.AddBookInReadList, (update, context, answer, chat_id)),
                self._keyboard.MenuBookKeyboard[lang][4]: lambda: Thread.Thread(self._book.SendListReadBooks, (update, context, answer, lang, chat_id)),
                self._keyboard.BookStateKeyboardDelete[lang][0]: lambda: Thread.Thread(self._book.DeleteInReadList, (update, context, answer, chat_id)),
                self._keyboard.Setting[lang][6]: lambda: Thread.Thread(self._setting.ExistentialResponse, (update, context, answer, chat_id))
                }
            if text.replace("@imafinabot", "") in CommandTxtButton.keys():
                if len(text) > 1 or text.isnumeric():
                    if CommandTxtButton[text.replace("@imafinabot", "")]() and '?' in text: Thread.Thread(self._std.question, (update, context, answer))
        else:
            self._instance.Users[chat_id] = User(chat_id, self._instance, update)
            self._instance.Dispatcher(update, context)

    def data(self, update):
        try: return str(update.message.text).lower()
        except Exception: return str(update.callback_query.data)

    def GetChatID(self, update):
        try: return str(update.callback_query.message.chat_id)
        except Exception: return str(update.message.chat_id)

class User():
    def __init__(self, chat_id, mafina, update):
        mafina._DB.CheckUser(update.message.chat.title, update.message.chat.username, chat_id,
                update.message.from_user.language_code, update.message.chat.type)
        self.chat_id = chat_id
        self.answer, self.lang = mafina._DB.GetJsonLanguageBot(chat_id)

Mafina()