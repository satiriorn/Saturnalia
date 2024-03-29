from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

class Keyboard:

    @staticmethod
    def InitKeyboard(NameButton):
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
    @staticmethod
    def InlineKeyboard(NameButton, Status=True):
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

    d = {"af":"Afrikaans", "ak":"Akan", "sq":"Albanian", "am":"Amharic", "ar":"Arabic","hy":"Armenian","az":"Azerbaijani","eu":"Basque",
         "be":"Belarusian","bem":"Bemba","bn":"Bengali","bh":"Bihari","bs":"Bosnian","br":"Breton","bg":"Bulgarian","km":"Cambodian","ca":"Catalan",
         "hr":"Croatian","cs":"Czech","da":"Danish","nl":"Dutch","en":"English","et":"Estonian","fr":"French","fi":"Finnish","ka":"Georgian",
         "de":"German","el":"Greek","hu":"Hungarian","is":"Icelandic","id":"Indonesian","it":"Italian","ja":"Japanese","jw":"Javanese",
         "kn":"Kannada","kk":"Kazakh","kg":"Kongo","ko":"Korean","la":"Latin","lv":"Latvian","mo":"Moldavian","mn":"Mongolian","pl":"Polish","pt-BR":"Portuguese (Brazil)",
         "pt-PT":"Portuguese (Portugal)","ro":"Ukrainen","ru":"Russian","sr":"Serbian","sk":"Slovak","sl":"Slovenian","es":"Spanish","sw":"Swahili",
         "sv":"Swedish","tt":"Tatar","tr":"Turkish","tk":"Turkmen","uk":"Ukrainian"}

    b = {"Afrikaans":"af", "Akan":"ak", "Albanian":"sq", "Amharic":"am", "Arabic":"ar", "Armenian":"hy","Azerbaijani":"az","Basque":"eu",
         "Belarusian":"be","Bemba":"bem","Bengali":"bn","Bihari":"bh","Bosnian":"bs","Breton":"br","Bulgarian":"bg","Cambodian":"km","Catalan":"ca",
         "Croatian":"hr","Czech":"cs","Danish":"da","Dutch":"nl","English":"en","Estonian":"et","French":"fr","Finnish":"fi","Georgian":"ka",
         "German":"de","Greek":"el","Hungarian":"hu","Icelandic":"is","Indonesian":"id","Italian":"it","Japanese":"ja","Javanese":"jw",
         "Kannada":"kn","Kazakh":"kk","Kongo":"kg","Korean":"ko","Latin":"la","Latvian":"lv","Moldavian":"mo","Mongolian":"mn","Polish":"pl","Portuguese (Brazil)":"pt-BR",
         "Portuguese (Portugal)":"pt-PT","Russian":"ru","Serbian":"sr","Slovak":"sk","Slovenian":"sl","Spanish":"es","Swahili":"sw",
         "Swedish":"sv","Tatar":"tt","Turkish":"tr","Turkmen":"tk","Ukrainian":"uk"}

    MainKeyboard = ["/Cut", "/Rest", "/Voice", "/Book", "/Evtuh", "/Sheva", "/Meme", "/Weather", "/Convert", "/Youtube", "/Binance", "/SettingBot","/Dog","/Cat", "/Cancel"]
    TranslateKeyboard = ["Azerbaijani", "Belarusian", "Bulgarian", "Croatian", "Czech", "English","Estonian", "French", "Finnish", "Georgian", "German", "Italian", "Latvian", "Polish", "Russian","Serbian","Slovak","Slovenian", "Spanish", "Ukrainian" ]
    LanguageBot = ["Belarusian", "Ukrainian", "English", "Czech"]
    FormatBookKeyboard = [".epub", ".fb2", ".pdf"]
    QualityAudio = ["48", "128", "160", "256", "320"]
    CountMeme = {
        "uk": ["Вимкнення", "1 мем у 15 хвилин", "1 мем у 30 хвилин", "1 мем у 60 хвилин", "1 мем у 120 хвилин"],
        "be": ["Адключэнне", "1 мем за 15 хвілін", "1 мем за 30 хвілін", "1 мем за 60 хвілін", "1 мем за 120 хвілін"],
        "en": ["Off meme", "1 meme in 15 minutes", "1 meme in 30 minutes", "1 meme in 60 minutes", "1 meme in 120 minutes"],
        "fr": ["Fermer", "1 mème en 15 minutes", "1 mème en 30 minutes", "1 mème en 60 minutes", "1 mème en 120 minutes"],
        "cs":  ["Vypnout", "1 mem za 15 minut", "1 mem za 30 minut", "1 mem za 60 minut", "1 mem za 120 minut"]
        }
    Setting = {
        "uk": ["Мова перекладу", "Мова бота", "Увм/Вимк погоду", "Налаштування котиків", "Кількість мемів",
                      "Увм/Вимк відповіді", "Нічний режим мемів", "Не треба нічого змінювати"],
        "be": ["Мова перакладу", "Мова бота", "Укл/вык надвор'я",
                    "Налады като́ў", "Колькасць мемаў", "Укл/вык адказа́ў", "Начны рэжым мемаў", "Нічога мяняць не трэба"],
        "en": ["Translation language", "Bot language", "On/Off weather", "Settings cats", "Quantity of memes",
                       "On/Off response", "Night mode memes", "No need to change anything"],
        "fr": ["Langue de translation", "Langue du bot", "Allumer/éteindre le temps", "Réglages les chats", "Quantité de mèmes",
                       "On/Off response","Mode nuit mèmes", "No need to change anything"],
        "cs": ["Překladový jazyk", "Bot jazyk", "Počasí zapnuto/vypnuto", "Nastavení koček", "Počet memů",
                       "Odezva zapnutí/vypnutí", "Memy v nočním režimu", "Není třeba nic měnit"]
        }
    YoutubeKeyboard = {
        "uk": ["Скачати Відео", "Скачати Аудіо", "Скачати та Обрізати"],
        "be": ["Загрузка відэа", "Загрузка аўдыя", "Загрузка і абрэзка"],
        "en": ["Download Video", "Download Audio", "Download and Cut"],
        "fr": ["Télécharger la Video", "Télécharger l'Audio", "Télécharger et Сouper"],
        "cs": ["Stáhnout video", "Stáhnout Audio", "Stáhnout a vyjmout"],
        }
    CutKeyboard ={
        "uk": ["Обрізати Відео", "Обрізати Аудіо", "Скачати та Обрізати"],
        "be": ["Абрэзка відэа", "Абрэзка аўдыя", "Загрузка і абрэзка"],
        "en": ["Cut Video", "Cut Audio", "Download and Cut"],
        "fr": ["Couper le Video", "Couper l'Audio", "Télécharger et Сouper"],
        "cs": ["Vystřihnout video", "Vystřihnout audio", "Stáhnout a vyjmout"]
        }
    MenuBookKeyboard = {
        "uk": ["Додати книгу", "Пошук по автору", "Пошук по назві", "Кількість книг", "Cписок прочитаних книг"],
        "be": ["Дадаць кнігу", "Пошук па аўтару", "Пошук па назве", "Колькасць кніг", "Спіс прачытаных кніг"],
        "en": ["Add a book", "Search by author", "Search by title", "Number of books", "List of books read"],
        "fr": ["Ajouter le livre", "Recherche par auteur", "Rechercher par title", "Nombre des livres", "Liste des livres lus"],
        "cs": ["Přidejte knihu", "Hledání podle autora", "Hledat podle názvu", "Počet knih", "Seznam přečtených knih"],
    }
    MenuBinanceKeyboard ={
        "uk": ["Додати пару крипти", "Видалити пару", "Показати стан обраних криптовалют"],
        "be": ["Дадаць крыптапару", "Выдаліць пару", "Паказаць стан выбраных криптовалют"],
        "en": ["Add pair cryptocurrency", "Delete pair", "Show the status of selected cryptocurrencies"],
        "cs": ["Přidat kryptoměny pár", "Odstranit pár"," Zobrazit stav vybraných kryptoměn"],
        "fr": ["Ajouter une paire crypto-monnaie", "Supprimer la paire", "Afficher l'état des crypto-monnaies sélectionnées"]
    }
    ConfirmKeyboard = {
        "uk": ["Так", "Ні"],
        "be": ["Так", "Не"],
        "en": ["Yes", "No"],
        "fr": ["Oui", "Non"],
        "cs": ["Ano", "Ne"]
        }
    BookStateKeyboard = {
        "uk": ["Додати до списку", "Отримати файл", "Нічого не треба"],
        "be": ["Дадаць у спіс", "Атрымаць файл", "Нічога не трэба"],
        "en": ["Add to list", "Get the file", "Nothing needed"],
        "fr": ["Ajouter a la liste", "Obtenir le fichier", "Rien nécessaire"],
        "cs": ["Přidat do seznamu", "Získejte soubor", "Nic nepotřebuješ"],
        }
    BookStateKeyboardDelete = {
        "uk": ["Видалити зі списку", BookStateKeyboard["uk"][1], BookStateKeyboard["uk"][2]],
        "be": ["Выдаліць са спісу", BookStateKeyboard["be"][1], BookStateKeyboard["be"][2]],
        "en": ["Remove from list", BookStateKeyboard["en"][1], BookStateKeyboard["en"][2]],
        "fr": ["Retirer de la liste", BookStateKeyboard["fr"][1], BookStateKeyboard["fr"][2]],
        "cs": ["Odstranit ze seznamu", BookStateKeyboard["cs"][1], BookStateKeyboard["cs"][2]]
    }
    CancelButton = {
        "uk": ["Закінчити процес"],
        "be": ["Завяршыць працэс"],
        "en": ["Finish the process"],
        "fr": ["Terminez le processus"],
        "cs": ["Dokončete proces"],
    }
    RestButton = {
        "uk": ["Занурюємося"],
        "be": ["Пачнем"],
        "en": ["Start"],
        "fr": ["Commencer"],
        "cs": ["Začneme?"]
    }

    AnimalButton = {
        "uk": ["Вимкнути", "12:00", "09:00, 12:00", "09:00, 12:00, 22:00", "09:00, 12:00, 18:00, 22:00", "Кількість котиків"],
        "be": ["Выключыць", "12:00", "09:00, 12:00", "09:00, 12:00, 22:00", "09:00, 12:00, 18:00, 22:00", "Колькасць катоў"],
        "en": ["Disable", "12:00", "09:00, 12:00", "09:00, 12:00, 22:00", "09:00, 12:00, 18:00, 22:00", "Number of cats"],
        "fr": ["Éteindre", "12:00", "09:00, 12:00", "09:00, 12:00, 22:00", "09:00, 12:00, 18:00, 22:00", "Nombre de chats"],
        "cs": ["Vypnout", "12:00", "09:00, 12:00", "09:00, 12:00, 22:00", "09:00, 12:00, 18:00, 22:00", "Počet koček"],
    }
