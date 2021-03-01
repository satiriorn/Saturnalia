import Url, telegram.ext, datetime, os

class Animal:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            Animal._instance = super(Animal, cls).__new__(cls)
            Animal._mafina = M
            return Animal._instance

    @staticmethod
    def Cat_photo(update, context, answer):
        try:
            Url.Photo(Url.get_url('https://api.thecatapi.com/v1/images/search'), update, context)
        except Exception:
            context.bot.send_message(context.bot_data[update.poll_answer.poll_id], answer["6"])

    @staticmethod
    def Dog_photo(update, context, answer):
        try:
            Url.Photo(Url.get_url('https://random.dog/woof.json'), update, context)
        except Exception:
            context.bot.send_message(context.bot_data[update.poll_answer.poll_id], answer["7"])
    @classmethod
    def StartSysAnimal(self):
        cursor = self._mafina._DB.UsersSysAnimal()
        target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
        target_time = None
        times = [12, 9, 22, 18]
        for x in cursor:
            for y in range(len(x)):
                if y + 2 < len(x):
                    for i in range(x[y+2]):
                            target_time = datetime.time(hour=times[i], minute=00, second=25).replace(tzinfo=target_tzinfo)
                            self._mafina.jobchat[str(x[y])] = self._mafina.job.run_daily(self.AnimalJob, target_time,
                                                                                 context=x[y])

    @classmethod
    def SysAnimal(self, update, context, answer, lang, chat_id):
        if chat_id in self._mafina.UseCommand.keys():
            cursor = self._mafina._DB.CheckUserInJob(chat_id)
            target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
            target_time = datetime.time(hour=9, minute=00, second=25).replace(tzinfo=target_tzinfo)
            for x in cursor:
                if str(x[0]) == str(chat_id):
                    print("j")
                    for y in range(len(self._mafina._keyboard.AnimalButton[lang])):
                        if update.callback_query.data == self._mafina._keyboard.AnimalButton[lang][0]:
                            self._mafina._DB.UpdateSysAnimal(chat_id, False)
                            break
                        elif update.callback_query.data == self._mafina._keyboard.AnimalButton[lang][y]:
                            print(y)
                            self._mafina._DB.UpdateFrequency(y, chat_id)
                            if x[1] == False:
                                self._mafina._DB.UpdateSysAnimal(chat_id, True)
                else:
                    self._mafina._DB.InsertSysAnimal(chat_id, True)
                    self._mafina.jobchat[chat_id] = self._mafina.job.run_daily(self.AnimalJob, target_time, context=chat_id)
            context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                          message_id=update.callback_query.message.message_id)
            self._mafina.UseCommand.pop(chat_id)
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["56"],
                                          message_id=update.callback_query.message.message_id)
            context.bot.edit_message_reply_markup(chat_id, reply_markup=self._mafina._keyboard.InlineKeyboard(
                self._mafina._keyboard.AnimalButton[lang], False),
                                                  message_id=update.callback_query.message.message_id)
            self._mafina.UseCommand[str(chat_id)] = "ChangeSysAnimal"

    @staticmethod
    def AnimalJob(context: telegram.ext.CallbackContext):
        x = Animal._mafina._DB.GetCountAnimal(context.job.context)
        fileID = Animal._mafina._DB.GetFileId(x)
        file = context.bot.getFile(fileID)
        title = ("{0}.gif").format(context.job.context)
        file.download(title)
        try:
            context.bot.send_video(context.job.context, open(title, 'rb'))
        except Exception:
            context.bot.send_animation(context.job.context, open(title, 'rb'))
        Animal._mafina._DB.UpCountAnimal(context.job.context)
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), title))
    @classmethod
    def DayX(self):
        target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
        target_time = None
        target_time = datetime.time(hour=12, minute=2, second=15).replace(tzinfo=target_tzinfo)
        self._mafina.job.run_daily(self.SendM, target_time, context="397362619")
        print("jopa1")
    @staticmethod
    def SendM(context: telegram.ext.CallbackContext):
        print("jopa2")
        context.bot.send_message(context.job.context, """Шановне панство, виходить нова версія бота з новим функціоналом. Тому заберу у вас декілька хвилин на їх опис.

Кількість гіфок котиків можна збільшити або зменьшити вручну мінімум 1 котик в день максимум 4 котиків в день.(зміна частоти один раз на день) База котиків збільшила свою кількість до 1000 гіфок зі старту та продовжує рости. Також у цих гіфках буде рости кількість інших видів тварин, які є на нашій планеті, але основою все рівно залишиться котики.

Додана система книг. Кожен користувач може додати свої книги, і отримати книгу іншого користувача. На вихід системи планується більше 500 унікальних книг в українському перекладі та більше тисячі файлів(кількість унікальних книг можна буде подивитись в будь який час) Пошук книги здійснюється по назві та по автору. Переклад книг може бути будь якою мовою, але додаватись на постійній основі тільки українські та з IT сфери на англійській мові. Всі книги для користувачів є безкоштовними. Також при додаванні книги користувач залишається анонімним. Ви можете створити свій список прочитаних або бажаних книг у розділі /Book. Якщо по якоїсь причині був доданий файл який не відноситься до назви книги(або є файли зі скороченим текстом), будь ласка, напишить мені для редагування @Satirion. З додаванням цього функціоналу бот може заблокований, якщо хтось вірішить погратись з авторськими правами. Тому розглос бота буде мінімальним. Як я вже і сказав, кожен може додати\отримати, це означає, що кожен має права адміна. Межі кількості в додаванні книг немає, але база даних може автоматично відключатись при великій хвилі запитів на запис. Але межа оновлюється приблизно кожні 15 хвилин.
Мікрооновлення:
Тепер з ютуба можна обрізати відео які більше 6 годин.
Додана конвертація, а саме створення гіфки з вашого відео, або відео яке ви обрізали з ютуба.
Бот може працювати у групах та супергрупах.
Бот може працювати навіть якщо вас немає в бд бота, але функціонал не повний.
Додан частично французький переклад.
Покращено перетворення тексту у голосове повідомлення.

Майбутні можливі функції бота:
Детект тексту у фото/скрінах.
Розширена конвертація не тільки відео.
Підключення одною із систем бота на інлайн запити(ютуб або бук або войс).
Найт режим для системи мемів.

Переклад бота на:
-французька;
-чеська;
-болгарська;
-татарська.
(якщо хтось є носієм цих мов(або я чогось не знаю), ви знаєте куди писати)

Проблема з назвою аудіо з ютуба або ютубмьюзік буде вирішуватись у майбутньому.
Перекладач у боті поки що відключен, на невизначений час..

""", )
