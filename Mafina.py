import Thread, Quotes, StandartCommand, weather, Evtuh,  CreateVoice, DogAndCat, InlineQuery, os, Meme, Youtube, Translate, DB, Keyboard, Setting, Rest, Cut, File, Book, Convert, DispatcherMafina
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, CallbackQueryHandler

class Mafina(object):
    _instance, _DB, job, _translator, _keyboard, _weather, _voice, _std = None, None, None, None, None, None, None, None
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
        Mafina._voice, Mafina._std = CreateVoice.Voice(self), StandartCommand.StandartCommand(self)
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
        self.dispatcher.add_handler(InlineQueryHandler(InlineQuery.inlinequery))

    def run(self):
        #Meme.StartSystemMeme()
        self._weather.StartSysWeather()
        #DogAndCat.StartSysAnimal()
        self.updater.start_polling(timeout=99000, poll_interval=3)
        self.updater.idle()

    @classmethod
    def Dispatcher(self, update, context):
        chat_id =self._instance.GetChatID(update)
        if str(chat_id) in self._instance.Users.keys():
            answer, lang =self._instance.Users[chat_id].answer, self._instance.Users[chat_id].lang
            text = str(update.message.text).lower()
            if text == "/start": Thread.Thread(self._std.start(update, context, answer, chat_id))
            elif text == "/help": Thread.Thread(self._std.help, (update, context, answer))
            elif text == "/weather": Thread.Thread(self._weather.weather, (update, context, answer))
            elif text == "/evtuh": Thread.Thread(Evtuh.Evtuh,(update, context))
            elif text == "/voice": self._voice.voice(update, context)

                   #"/Cat": DogAndCat.Cat_photo(update, context), "/Dog": DogAndCat.Dog_photo(update, context), "/Sheva": Quotes.ShevchenkoStyle(update, context),
                   #"/Meme": Meme.Get_meme(update, context), "/Youtube": Youtube.Start(update, context, answer, lang), "/SettingBot": Setting.ShowSetting(update, context, answer, lang),
                   #"/Translate": Translate.translate(update, context, answer, chat_id), "/Rest": Rest.Rest(update, context, answer, lang, chat_id),
                   #"/Cut": Cut.CutStart(update, context, answer, lang), "/Book": Book.MenuBook(update, context, answer, lang),
                   #"/Convert": Convert.convert(update, context, answer, chat_id)}
        else:
            self._instance.Users[chat_id] = User(chat_id)
            self._instance.Dispatcher(update, context)
    def GetChatID(self, update):
        try:
            return str(update.callback_query.message.chat_id)
        except Exception:
            return str(update.message.chat_id)

class User():
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.answer, self.lang = DB.DataBase.GetJsonLanguageBot(Mafina._DB, chat_id)

Mafina()