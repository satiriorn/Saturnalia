import Thread,UkrainianGame, File, weather, Evtuh, DogAndCat, CreateVoice, Convert, Setting, Translate, Youtube, Quotes, Rest, Cut, Book, Meme, DB, Mafina

class User():
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.answer, self.lang = DB.DataBase.GetJsonLanguageBot(Mafina.Mafina.DB, chat_id)
def Dispatcher(update, context):
    m = Mafina.mafina
    chat_id = m.GetChatID(m, update)
    if chat_id in m.Users.keys():
        if chat_id in m.UseCommand.keys():
            answer, lang =m.Users[chat_id].answer, m.Users[chat_id].lang
            res = Mafina.mafina.UseCommand[chat_id]
            Command = {
               "/start": start.start(update, context), "/Help": help.help(update, context),
               "/Weather": weather.weather(update, context, answer), "/Evtuh": Evtuh.Evtuh(update, context),
               "/Voice": CreateVoice.voice(update, context),
               "/Cat": DogAndCat.Cat_photo(update, context), "/Dog": DogAndCat.Dog_photo(update, context),
               "/Sheva": Quotes.ShevchenkoStyle(update, context),
               "/Meme": Meme.Get_meme(update, context),
               "/Youtube": Youtube.Start(update, context, answer, lang),
               "/SettingBot": Setting.ShowSetting(update, context, answer, lang),
               "/Translate": Translate.translate(update, context, answer, chat_id),
               "/Rest": Rest.Rest(update, context, answer, lang, chat_id),
               "/Cut": Cut.CutStart(update, context, answer, lang),
               "/Book": Book.MenuBook(update, context, answer, lang),
               "/Convert": Thread.Thread(Convert.convert, (update, context, answer, chat_id))
                       }
            Command[update.chat.text]
            if res == "Audio": Thread.Thread(Youtube.Get_Audio, (update, context))
            elif res == "Video":Thread.Thread(Youtube.Get_Video, (update, context))
            elif res == "CutAudio":Thread.Thread(Cut.CutAudio, (update, context))
            elif res == "CutVideo":Thread.Thread(Cut.CutVideo, (update, context))
            elif res == "CreateVoice":Thread.Thread(CreateVoice.voice, (update, context))
            elif res == "Translate":Thread.Thread(Translate.translate, (update, context))
            elif res == "GetCutVideo":Thread.Thread(Cut.GetCutStart, (update,context))
            elif res == "CutEnd":Thread.Thread(Cut.Cut, (update, context))
            elif res == "Check":Thread.Thread(Book.UploadBook, (update, context))
            elif res == "SearchViaName":Thread.Thread(Book.SearchBook, (update, context))
            elif res == "SearchViaAuthor":Thread.Thread(Book.SearchAuthor, (update, context))
        elif "погода" == update.message.text.lower():
            Thread.Thread(weather.CurrentWeather, (update, context))
        elif update.message.text.lower() == "котик":
            Thread.Thread(DogAndCat.Cat_photo,(update, context))
        elif "мем" == update.message.text.lower():
            Thread.Thread(Meme.Get_meme,(update, context))
        elif "animal" == update.message.text.lower():
            Thread.Thread(File.SendFile, (update, context))
        elif '?' in update.message.text.lower():
            Thread.Thread(UkrainianGame.question,(update, context))
    else:
         Mafina.mafina.Users[chat_id] = User(chat_id)
         Dispatcher(update, context)