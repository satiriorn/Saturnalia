import Thread, Quotes, StandartCommand, weather, Evtuh,  CreateVoice, DogAndCat, InlineQuery, os, Meme, Youtube, Translate, DB, Keyboard, Setting, Rest, Cut, File, Book, Convert, DispatcherMafina
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, CallbackQueryHandler

class Mafina(object):
    _instance, DB, job, translator, keyboard = None, None, None, None, None
    UseCommand, CutFile, jobchat, Book, ResultSearch, KeyboardFormat, Users = {}, {}, {}, {}, {}, {}, {}
    NameFormat = [".epub", ".fb2", ".pdf"]
    fileformat = {".epub": "file_id_epub", ".fb2": "file_id_fb2", ".pdf": "file_id_pdf"}

    def __new__(cls):
        if not hasattr(cls, '_inst'):
            Mafina._instance = super(Mafina, cls).__new__(cls)
            return Mafina._instance

    def __init__(self):
        Mafina.DB = DB.DataBase()
        self.updater = Updater(os.getenv("TOKEN"), use_context=True)
        Mafina.job, Mafina.DB, Mafina.keyboard = self.updater.job_queue, DB.DataBase(), Keyboard.Keyboard()
        self.dispatcher = self.updater.dispatcher
        self.command = {"start":StandartCommand.start, "Help":StandartCommand.help}#,# "Weather":weather.weather, "Evtuh":Evtuh.Evtuh, "Voice":CreateVoice.voice,
                        #"Cat": DogAndCat.Cat_photo, "Dog":DogAndCat.Dog_photo, "Sheva":Quotes.ShevchenkoStyle,"Meme":Meme.Get_meme, "Youtube":Youtube.Start,
                        #"SettingBot": Setting.ShowSetting, "Translate": Translate.translate,"Rest": Rest.Rest,"Cut": Cut.CutStart,"Book": Book.MenuBook,
                        #"Convert": Convert.convert}
        self.CreateHandler()
        self.run()

    def CreateHandler(self):
        dispatchermafina_handler = MessageHandler(Filters.command, Mafina.Dispatcher)
        #callback_query_handler = CallbackQueryHandler(Keyboard.button)
        file_message_handler = MessageHandler(Filters.audio | Filters.video | Filters.animation, File.file)
        document_message_handler = MessageHandler(Filters.document, Book.FileStream)
        self.dispatcher.add_handler(dispatchermafina_handler)
        #self.dispatcher.add_handler(callback_query_handler)
        self.dispatcher.add_handler(file_message_handler)
        self.dispatcher.add_handler(document_message_handler)
        self.dispatcher.add_handler(InlineQueryHandler(InlineQuery.inlinequery))
        for x in range(len(self.command)):
            self.dispatcher.add_handler(CommandHandler(list(self.command.keys())[x],list(self.command.values())[x]))

    def run(self):
        #Meme.StartSystemMeme()
        weather.StartSysWeather(self)
        #DogAndCat.StartSysAnimal()
        self.updater.start_polling(timeout=99000, poll_interval=3)
        self.updater.idle()

    @classmethod
    def Dispatcher(self, update, context):
        chat_id =self._instance.GetChatID(update)
        if str(chat_id) in self._instance.Users.keys():
            answer, lang =self._instance.Users[chat_id].answer, self._instance.Users[chat_id].lang
            text = str(update.message.text).lower()
            if text == "/start": Thread.Thread(StandartCommand.start(update, context, answer, Mafina, chat_id))
            elif text == "/help": Thread.Thread(StandartCommand.help, (update, context, answer, Mafina))
            elif text == "/weather": Thread.Thread(weather.weather, (update, context, answer))

                   #"/Weather": weather.weather(update, context, answer), "/Evtuh": Evtuh.Evtuh(update, context), "/Voice": CreateVoice.voice(update, context),
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
        self.answer, self.lang = DB.DataBase.GetJsonLanguageBot(Mafina.DB, chat_id)

Mafina()