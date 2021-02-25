import Thread, Quotes, StandartCommand, weather, Evtuh,  CreateVoice, DogAndCat, InlineQuery, os, Meme, Youtube, Translate, DB, Keyboard, Setting, Rest, Cut, File, Book, Convert, DispatcherMafina
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, CallbackQueryHandler

class Mafina(object):
    _instance, _DB, job, _translator, _keyboard, _weather, _voice, _std, _animal, _meme, = None, None, None, None, None, None, None, None, None, None
    _youtube = None
    UseCommand, CutFile, jobchat, Book, ResultSearch, KeyboardFormat, Users = {}, {}, {}, {}, {}, {}, {}
    NameFormat = [".epub", ".fb2", ".pdf"]
    fileformat = {".epub": "file_id_epub", ".fb2": "file_id_fb2", ".pdf": "file_id_pdf"}

    def __new__(cls):
        if not hasattr(cls, '_inst'):
            Mafina._instance = super(Mafina, cls).__new__(cls)
            return Mafina._instance

    def __init__(self):
        self.updater = Updater(os.getenv("TOKEN"), use_context=True)
        Mafina.job, Mafina._DB, Mafina._keyboard, Mafina._weather = self.updater.job_queue, DB.DataBase(), Keyboard.Keyboard(), weather.Weather(self)
        Mafina._voice, Mafina._std, Mafina._animal = CreateVoice.Voice(self), StandartCommand.StandartCommand(self), DogAndCat.Animal(self)
        Mafina._meme, Mafina._youtube = Meme.Meme(self), Youtube.Youtube(self)
        self.dispatcher = self.updater.dispatcher
        self.CreateHandler()
        self.run()

    def CreateHandler(self):
        dispatchermafina_handler = MessageHandler(Filters.command|Filters.text, Mafina.Dispatcher)
        #callback_query_handler = CallbackQueryHandler(Keyboard.button)
        file_message_handler = MessageHandler(Filters.audio | Filters.video | Filters.animation, File.file)
        document_message_handler = MessageHandler(Filters.document, Book.FileStream)
        self.dispatcher.add_handler(dispatchermafina_handler)
        #self.dispatcher.add_handler(callback_query_handler)
        self.dispatcher.add_handler(file_message_handler)
        self.dispatcher.add_handler(document_message_handler)
        #self.dispatcher.add_handler(InlineQueryHandler(InlineQuery.inlinequery))

    def run(self):
        self._meme.StartSystemMeme()
        self._weather.StartSysWeather()
        self._animal.StartSysAnimal()
        self.updater.start_polling(timeout=99000, poll_interval=3)
        self.updater.idle()

    @classmethod
    def Dispatcher(self, update, context):
        print(update)
        chat_id =self._instance.GetChatID(update)
        if chat_id in self._instance.Users.keys():
            answer, lang = self._instance.Users[chat_id].answer, self._instance.Users[chat_id].lang
            text = str(update.message.text).lower()
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
            print(self._instance.UseCommand.keys())
            if chat_id in self._instance.UseCommand.keys():
                res = self._instance.UseCommand[chat_id]
                print(res)
                if res == "Audio":Thread.Thread(Youtube.Get_Audio, (update, context))
                elif res == "Video":Thread.Thread(Youtube.Get_Video, (update, context))
                elif res == "CutAudio":Thread.Thread(Cut.CutAudio, (update, context))
                elif res == "CutVideo":Thread.Thread(Cut.CutVideo, (update, context))
                elif res == "CreateVoice":Thread.Thread(self._voice.voice, (update, context, answer, chat_id))
                elif res == "Translate":Thread.Thread(Translate.translate, (update, context))
                elif res == "GetCutVideo":Thread.Thread(Cut.GetCutStart, (update, context))
                elif res == "CutEnd":Thread.Thread(Cut.Cut, (update, context))
                elif res == "Check":Thread.Thread(Book.UploadBook, (update, context))
                elif res == "SearchViaName":Thread.Thread(Book.SearchBook, (update, context))
                elif res == "SearchViaAuthor":Thread.Thread(Book.SearchAuthor, (update, context))

                   #" ,
                   # , "/SettingBot": Setting.ShowSetting(update, context, answer, lang),
                   #"/Translate": Translate.translate(update, context, answer, chat_id), "/Rest": Rest.Rest(update, context, answer, lang, chat_id),
                   #"/Cut": Cut.CutStart(update, context, answer, lang), "/Book": Book.MenuBook(update, context, answer, lang),
                   #"/Convert": Convert.convert(update, context, answer, chat_id)}
        else:
            self._instance.Users[chat_id] = User(chat_id, self._instance)
            self._instance.Dispatcher(update, context)
    def GetChatID(self, update):
        try:
            return str(update.callback_query.message.chat_id)
        except Exception:
            return str(update.message.chat_id)

class User():
    def __init__(self, chat_id, mafina):
        self.chat_id = chat_id
        self.answer, self.lang = mafina._DB.GetJsonLanguageBot(chat_id)

Mafina()