from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import Setting, Mafina, Dologusha, Meme, Rest, Youtube, Cut, Thread, weather, DogAndCat, Book, DB

class Keyboard:
    def InitKeyboard(self, NameButton):
        LevelOne, LevelTwo, LevelThree, LevelFour, Button = [], [], [], [], []
        for i in range(len(NameButton)):
            if i<5:
                LevelOne.append(KeyboardButton(NameButton[i]))
            elif (i>=5) and (i<8):
                LevelTwo.append(KeyboardButton(NameButton[i]))
            elif (i >= 8) and (i < 12):
                LevelThree.append(KeyboardButton(NameButton[i]))
            else:
                LevelFour.append(KeyboardButton(NameButton[i]))
        Button.append(LevelOne)
        Button.append(LevelTwo)
        Button.append(LevelThree)
        Button.append(LevelFour)
        return ReplyKeyboardMarkup(Button, resize_keyboard=True)

    def InlineKeyboard(self, NameButton, Status=True):
        keyboard = []
        i = 0
        data = lambda NameButton, Status, i: i if Status == True else NameButton[i]
        while i < len(NameButton):
            if ((i+1)<len(NameButton)):
                keyboard.append([InlineKeyboardButton(NameButton[i], callback_data= data(NameButton,Status,i)),
                             InlineKeyboardButton(NameButton[i+1], callback_data= data(NameButton,Status,i+1))])
                i+=2
            else:
                keyboard.append([InlineKeyboardButton(NameButton[i], callback_data= data(NameButton,Status,i))])
                i += 1
        return InlineKeyboardMarkup(keyboard)

    def button(update, context):
        print(update)
        query = update.callback_query
        answer, lang = DB.DataBase.GetJsonLanguageBot(Mafina.Mafina.DB, update.callback_query.message.chat_id)
        if str(update.callback_query.message.chat_id) in Mafina.Mafina.UseCommand.keys():
            res = Mafina.Mafina.UseCommand[str(update.callback_query.message.chat_id)]
            if res == "Rest": Thread.Thread(Rest.Rest, (update, context, answer, lang, False))
            elif res == "MemeChange": Thread.Thread(Meme.MoreMeme, (update, context))
            elif res == "SettingTranslate": Thread.Thread(Setting.SettingTranslate, (update, context, answer))
            elif res == "Dologusha": Thread.Thread(Dologusha.start, (update, context))
            elif res == "LangBot": Thread.Thread(Setting.LanguageBot, (update, context, answer))
            elif res == "Confirm" or res == "Check"or res == "BookLang"or res == "FormatBook": Thread.Thread(Book.UploadBook, (update, context))
            elif res == "SeveralResult":Thread.Thread(Book.SearchBook, (update, context, answer, lang))
            elif res == "ConfirmTypeFile":Thread.Thread(Book.GetFile, (update, context, answer))
            elif res == "GetBookViaAuthor"or res == "SelectBookByAuthor": Thread.Thread(Book.SearchAuthor, (update, context, answer, lang))
            elif res == "GetBook":Thread.Thread(Book.SendListReadBooks, (update, context, answer, lang))
            elif query.data == Mafina.Mafina.CancelButton[lang][0]: Thread.Thread(Book.Cancel, (update, context, answer))
        elif query.data == "0":
            Thread.Thread(Setting.SettingTranslate, (update, context, answer))
        elif query.data =="1":
            Thread.Thread(Setting.LanguageBot, (update, context, answer))
        elif query.data == "2":
            Thread.Thread(weather.StateWeather, (update, context, answer))
        elif query.data == "3":
            Thread.Thread(DogAndCat.SysAnimal, (update, context))
        elif query.data == "4":
            Thread.Thread(Meme.CountMem,(update, context))
        elif query.data == "5":
            Thread.Thread(Setting.SettingAnswer, (update, context))
        elif query.data == Mafina.Mafina.YoutubeKeyboard[lang][0]:
            Thread.Thread(Youtube.Get_Video, (update, context))
        elif query.data == Mafina.Mafina.YoutubeKeyboard[lang][1]:
            Thread.Thread(Youtube.Get_Audio, (update, context))
        elif query.data == Mafina.Mafina.CutKeyboard[lang][0]:
            Thread.Thread(Cut.CutVideo, (update, context))
        elif query.data == Mafina.Mafina.CutKeyboard[lang][1] :
            Thread.Thread(Cut.CutAudio, (update, context))
        elif query.data == Mafina.Mafina.YoutubeKeyboard[lang][2]:
            Thread.Thread(Cut.GetCutStart, (update, context))
        elif query.data == Mafina.Mafina.CancelButton[lang][0]:
            Thread.Thread(Book.Cancel, (update, context))
        elif query.data == Mafina.Mafina.MenuBookKeyboard[lang][2]:
            Thread.Thread(Book.SearchBook, (update, context))
        elif query.data == Mafina.Mafina.MenuBookKeyboard[lang][0]:
            Thread.Thread(Book.UploadBook, (update, context))
        elif query.data == Mafina.Mafina.BookStateKeyboard[lang][1]:
            Thread.Thread(Book.GetFile, (update, context))
        elif query.data == Mafina.Mafina.MenuBookKeyboard[lang][1]:
            Thread.Thread(Book.SearchAuthor, (update, context))
        elif query.data == Mafina.Mafina.MenuBookKeyboard[lang][3]:
            Thread.Thread(Book.CountBookInDB, (update, context))
        elif query.data == Mafina.Mafina.BookStateKeyboard[lang][0]:
            Thread.Thread(Book.AddBookInReadList, (update, context))
        elif query.data == Mafina.Mafina.MenuBookKeyboard[lang][4]:
            Thread.Thread(Book.SendListReadBooks, (update, context))
        elif query.data == Mafina.Mafina.BookStateKeyboardDelete[lang][0]:
            Thread.Thread(Book.DeleteInReadList, (update, context))
        else:
            Thread.Thread(Setting.ExistentialResponse, (update, context))
        return query

    d = {"af":"Afrikaans", "ak":"Akan", "sq":"Albanian", "am":"Amharic", "ar":"Arabic","hy":"Armenian","az":"Azerbaijani","eu":"Basque",
         "be":"Belarusian","bem":"Bemba","bn":"Bengali","bh":"Bihari","bs":"Bosnian","br":"Breton","bg":"Bulgarian","km":"Cambodian","ca":"Catalan",
         "hr":"Croatian","cs":"Czech","da":"Danish","nl":"Dutch","en":"English","et":"Estonian","fr":"French","fi":"Finnish","ka":"Georgian",
         "de":"German","el":"Greek","hu":"Hungarian","is":"Icelandic","id":"Indonesian","it":"Italian","ja":"Japanese","jw":"Javanese",
         "kn":"Kannada","kk":"Kazakh","kg":"Kongo","ko":"Korean","la":"Latin","lv":"Latvian","mo":"Moldavian","mn":"Mongolian","pl":"Polish","pt-BR":"Portuguese (Brazil)",
         "pt-PT":"Portuguese (Portugal)","ro":"Romanian","ru":"Russian","sr":"Serbian","sk":"Slovak","sl":"Slovenian","es":"Spanish","sw":"Swahili",
         "sv":"Swedish","tt":"Tatar","tr":"Turkish","tk":"Turkmen","uk":"Ukrainian"}

    b = {"Afrikaans":"af", "Akan":"ak", "Albanian":"sq", "Amharic":"am", "Arabic":"ar", "Armenian":"hy","Azerbaijani":"az","Basque":"eu",
         "Belarusian":"be","Bemba":"bem","Bengali":"bn","Bihari":"bh","Bosnian":"bs","Breton":"br","Bulgarian":"bg","Cambodian":"km","Catalan":"ca",
         "Croatian":"hr","Czech":"cs","Danish":"da","Dutch":"nl","English":"en","Estonian":"et","French":"fr","Finnish":"fi","Georgian":"ka",
         "German":"de","Greek":"el","Hungarian":"hu","Icelandic":"is","Indonesian":"id","Italian":"it","Japanese":"ja","Javanese":"jw",
         "Kannada":"kn","Kazakh":"kk","Kongo":"kg","Korean":"ko","Latin":"la","Latvian":"lv","Moldavian":"mo","Mongolian":"mn","Polish":"pl","Portuguese (Brazil)":"pt-BR",
         "Portuguese (Portugal)":"pt-PT","Romanian":"ro","Russian":"ru","Serbian":"sr","Slovak":"sk","Slovenian":"sl","Spanish":"es","Swahili":"sw",
         "Swedish":"sv","Tatar":"tt","Turkish":"tr","Turkmen":"tk","Ukrainian":"uk"}

    MainKeyboard = ["/Help", "/Cut", "/Rest", "/Voice", "/Book", "/Evtuh", "/Sheva", "/Meme", "/Weather", "/Convert", "/Youtube", "/SettingBot","/Dog","/Cat"]
    TranslateKeyboard = ["Azerbaijani", "Belarusian", "Bulgarian", "Croatian", "Czech", "English","Estonian", "French", "Finnish", "Georgian", "German", "Italian", "Latvian", "Polish","Romanian", "Russian","Serbian","Slovak","Slovenian", "Spanish", "Ukrainian" ]
    LanguageBot = ["Belarusian", "Ukrainian", "English"]
    FormatBookKeyboard = [".epub", ".fb2", ".pdf"]
    CountMeme = {
        "uk": ["Вимкнення", "1 мем у 15 хвилин", "1 мем у 30 хвилин", "1 мем у 60 хвилин", "1 мем у 120 хвилин"],
        "be": ["Адключэнне", "1 мем за 15 хвілін", "1 мем за 30 хвілін", "1 мем за 60 хвілін", "1 мем за 120 хвілін"],
        "en": ["Off meme", "1 meme in 15 minutes", "1 meme in 30 minutes", "1 meme in 60 minutes", "1 meme in 120 minutes"],
        "fr": ["Fermer", "1 mème en 15 minutes", "1 mème en 30 minutes", "1 mème en 60 minutes", "1 mème en 120 minutes"]
        }
    Setting = {
        "uk": ["Мова перекладу", "Мова бота", "Увм/Вимк погоду", "Увм/Вимк котиків", "Кількість мемів",
                      "Увм/Вимк відповіді", "Не треба нічого змінювати"],
        "be": ["Мова перакладу", "Мова бота", "Укл/вык надвор'я",
                    "Укл/вык като́ў", "Колькасць мемаў", "Укл/вык адказа́ў", "Нічога мяняць не трэба"],
        "en": ["Translation language", "Bot language", "On/Off weather", "On/Off cats", "Quantity of memes",
                       "On/Off response", "No need to change anything"],
        "fr": ["Langue de translation", "Langue du bot", "Allumer/éteindre le temps", "Allumer/éteindre les chats", "Quantité de mèmes",
                       "On/Off response", "No need to change anything"]
        }
    YoutubeKeyboard = {
        "uk": ["Скачати Відео", "Скачати Аудіо", "Скачати та Обрізати"],
        "be": ["Загрузка відэа", "Загрузка аўдыя", "Загрузка і абрэзка"],
        "en":["Download Video", "Download Audio", "Download and Cut"],
        "fr":["Télécharger la Video", "Télécharger l'Audio", "Télécharger et Сouper"]
        }
    CutKeyboard ={
        "uk": ["Обрізати Відео", "Обрізати Аудіо", "Скачати та Обрізати"],
        "be": ["Абрэзка відэа", "Загрузка аўдыя", "Загрузка і абрэзка"],
        "en": ["Cut Video", "Cut Audio", "Download and Cut"],
        "fr": ["Couper le Video", "Couper l'Audio", "Télécharger et Сouper"]
        }
    MenuBookKeyboard = {
        "uk": ["Додати книгу", "Пошук по автору", "Пошук по назві", "Кількість книг", "Cписок прочитаних книг"],
        "be": ["Дадаць кнігу", "Пошук па аўтару", "Пошук па назве", "Колькасць кніг", "Спіс прачытаных кніг"],
        "en": ["Add a book", "Search by author", "Search by title", "Number of books", "List of books read"],
        "fr": ["Ajouter le livre", "Recherche par auteur", "Rechercher par title", "Nombre des livres", "Liste des livres lus"]
    }
    ConfirmKeyboard = {
        "uk": ["Так", "Ні"],
        "be": ["Так", "Не"],
        "en": ["Yes", "No"],
        "fr": ["Oui", "Non"]
        }
    BookStateKeyboard = {
        "uk": ["Додати до списку", "Отримати файл", "Нічого не треба"],
        "be": ["Дадаць у спіс", "Атрымаць файл", "Нічога не трэба"],
        "en": ["Add to list", "Get file", "Nothing needed"],
        "fr": ["Ajouter a la liste", "Obtenir le fichier", "Rien nécessaire"]
        }
    BookStateKeyboardDelete = {
        "uk": ["Видалити зі списку", BookStateKeyboard["uk"][1], BookStateKeyboard["uk"][2]],
        "be": ["Выдаліць са спісу", BookStateKeyboard["be"][1], BookStateKeyboard["be"][2]],
        "en": ["Remove from list", BookStateKeyboard["en"][1], BookStateKeyboard["en"][2]],
        "fr": ["Retirer de la liste", BookStateKeyboard["fr"][1], BookStateKeyboard["fr"][2]]
    }
    CancelButton = {
        "uk": ["Закінчити процес"],
        "be": ["Завяршыць працэс"],
        "en": ["Finish the process"],
        "fr": ["Terminez le processus"]
        }
    RestButton = {
        "uk": ["Занурюємося"],
        "be": ["Пачнем"],
        "en": ["Start"],
        "fr": ["Commencer"]
    }