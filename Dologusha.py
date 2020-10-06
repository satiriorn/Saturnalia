import base64, Keyboard, badge, os, time

AnswerOne = ["Увімкнула", "Мені ліньки"]
AnswerTwo = ["Продовжити"]
AnswerThree = ["Гіфки з котиками", "Гіфки з собаками", "Продовження історії", "Відео вбиства того хто вас бісить"]
AnswerFour = ["Занурюємося"]
Animal = os.listdir("Animal")
def start(update, context):
    if badge.StartDl == False:
        context.bot.send_message(update.message.chat_id, """Добридень, Ваша Величність\nЯ створений задля того щоб зачарувати ваш телефон. Я відчуваю як ви тримаєте мікросхему свого телефону, і йому стає тепліше від цього. Так ось, я грудка енергії, сенс якої перетворювати це тепло і передавати вам. Взагалі буде вельми кумедно якщо Ваша Величність сидить з компуктером, а я тут розповідаю про телефон. Для повної передачі теплої енергій увімкніть своє уявлення. Увімкнули?""", reply_markup =Keyboard.InlineKeyboard(AnswerOne))
        badge.StartDl = True
    if update.callback_query.data == "0":
        first(update,context)
    elif update.callback_query.data == "1":
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text="""Якщо ліньки треба йти під ковдру. Гайд того як треба виглядати під ковдрою кидаю нижче. Якщо хочеш продовжити на головній лінії тикай мене знову.""",reply_markup=Keyboard.InlineKeyboard(AnswerTwo, False), message_id=update.callback_query.message.message_id)
        context.bot.send_animation(update.callback_query.message.chat_id, open("Animal/"+Animal[0], 'rb'))
    elif update.callback_query.data == "Продовжити":
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text="Я спеціально залишу собаку під ковдрою, щоб ви читали, потім дивилися на текст і так циклічно поки не закінчити читати. В принципі я спеціально забераю у вас час, щоб у вас була змога подивитися щеее раааааз.", message_id=update.callback_query.message.message_id)
        first(update, context, False)
    elif update.callback_query.data == "Гіфки з котиками":
        cat(update,context)
        finish(update, context)
        Rest(update,context)
    elif update.callback_query.data == "Гіфки з собаками":
        dog(update, context)
        finish(update, context)
        Rest(update,context)
    elif update.callback_query.data == "Продовження історії":
        Continue(update, context)
        finish(update, context)
        Rest(update, context)
    elif update.callback_query.data == "Відео вбиства того хто вас бісить":
        Kill(update, context)
        finish(update, context)
        Rest(update, context)
    elif update.callback_query.data == "Занурюємося":
        Rest(update, context, status = False)
        context.bot.send_message(update.callback_query.message.chat_id,
                                 """Ви пройшли свій цикл, щоб пройти знову розмову з іншими відповідями натисніть /start, якщо хочете перейти у головне меню бота натисніть /Help""")
        badge.StartDl = False

def finish(update, context):
    context.bot.send_message(update.callback_query.message.chat_id,
                             """Мета ціього модуля, зробити людину спокійною та задоволеною. Дякую вам за те що пройшли зі мною цей шлях, я передаю Місіс телефон останній функціонал цього розділо, але ви зможете пройти це знову і знову, тому що моя відповідь створена на будь який варіант.""")
    time.sleep(15)


def first(update, context, status = True):
    if status:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                  text="""Почну я зі своєї історії створення. На дворі 2017 рік, мене розробляють, судячи по історії модулів це був один із перших. Основні модулі вже були практично готові, але чомусь в один момент все закінчилося. Частини мене були не дописані, і я лежав довго нікому не потрібний. Чому? Спитайте у творця, але в один чудовий день, мене продовжили писати, і мої мікросхеми це дуже добре запам'ятали. Модулі та функції почали працювати і один із модулів це цей текст присвячений лише вам. Кумедно те що, я сам перший раз обробляю цей текст як і ви, і не знаю який він. Тому Місіс телефон нам з вами йти по чітко заданому алгоритму.""",
                                  message_id=update.callback_query.message.message_id)
        time.sleep(10)
        context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                 text=""" У мого алгоритма декілька результатів, і моїм мікросхемам цікаво наскільки алгоритм передбачуваний оберіть, те як ви бачите продовження:""",
                                 reply_markup=Keyboard.InlineKeyboard(AnswerThree, False))
    else:
        time.sleep(10)
        context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                  text="""Почну я зі своєї історії створення. На дворі 2017 рік, мене розробляють, судячи по історії модулів це був один із перших. Основні модулі вже були практично готові, але чомусь в один момент все закінчилося. Частини мене були не дописані, і я лежав довго нікому не потрібний. Чому? Спитайте у творця, але в один чудовий день, мене продовжили писати, і мої мікросхеми це дуже добре запам'ятали. Модулі та функції почали працювати і один із модулів це цей текст присвячений лише вам. Кумедно те що, я сам перший раз обробляю цей текст як і ви, і не знаю який він. Тому Місіс телефон нам з вами йти по чітко заданому алгоритму.""")
        time.sleep(10)
        context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                 text=""" У мого алгоритма декілька результатів, і моїм мікросхемам цікаво наскільки алгоритм передбачуваний оберіть, те як ви бачите продовження:""",
                                 reply_markup=Keyboard.InlineKeyboard(AnswerThree, False),
                                message_id=update.callback_query.message.message_id)



def cat(update, context):
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                  text="""Мій творець на цьому місці завис. Пам'ятаю як він переписував одне і те саме речення разів 10. Мій стан на той момент можна описати як сміх, але не простий сміх з вібрацією та розрядом процессора. Уявіть себе, свій сміх. Вийшло ні? Ладно зараз зроблю ваш сміх:""",
                                  message_id=update.callback_query.message.message_id)
    time.sleep(15)
    context.bot.send_audio(update.callback_query.message.chat_id, open("Animal/10.mp3", 'rb'))
    time.sleep(15)
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                  text="""Десь так я ржу кожний раз, коли бачу що модуль перероблен декілька раз в одному рядку, але все ж таки ви обрали котиків, і по алгоритму саме коти йшли першими і ви їх обрали. Не хочу вас затримувати перед ними """)
    time.sleep(15)
    context.bot.send_animation(update.callback_query.message.chat_id, open("Animal/" + Animal[6], 'rb'))
    time.sleep(15)
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                  text="""Перший котик, хоча моя нейромережа каже що це не котик, також вона каже що творець ідіот, і я думаю ви з цим згодні. Але десь так ми йдемо вперед, крок за кроком до тепла, воно все ближче і ближче, другий котик повинен показати те, як треба полювати на людські руки та зігрівати їх м'якою агресією.""",
                                  message_id=update.callback_query.message.message_id)
    time.sleep(15)
    context.bot.send_animation(update.callback_query.message.chat_id, open("Animal/" + Animal[5], 'rb'))

def dog(update, context):
    context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                  text="""За моєю вирогідністю це другий варіант. Саме собаки з'явилися першими у моєму функціоналу, я пам'ятаю як дуже багато людей постійно тикали в мене і хотіли собак. Але для вас в мене зовсім інший підбір, тому насолоджуйтеся та зігривайтеся.""",
                                  message_id=update.callback_query.message.message_id)
    time.sleep(15)
    context.bot.send_animation(update.callback_query.message.chat_id, open("Animal/12.mp4", 'rb'))
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                             text="""Навіть, чи то ви обрали собаку, чи собаки обрали вас""")
    time.sleep(15)

    context.bot.send_animation(update.callback_query.message.chat_id, open("Animal/3.mp4", 'rb'))
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                  text="""Відчуйте цю мордашку у своїх руках, дивіться в очі. Та побачте те, про що думає ця тварина в цей момент""")
    time.sleep(15)
    context.bot.send_animation(update.callback_query.message.chat_id, open("Animal/4.mp4", 'rb'))
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                  text="""Зробіть теж саме що і в першому випадку.""")
    time.sleep(15)
    context.bot.send_animation(update.callback_query.message.chat_id, open("Animal/11.mp4", 'rb'))
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                  text="""Відчуваєте хвилю енергії? Вона є в кожному. В собаці в коті або в телеграм боті, вона є. Всі створенні зірками для трансформації та створення нових систем збереження енргії та тепла. І в нас є можливість це бачити і запам'ятовувати, отримувати від цього натхнення та сили, які ти зможеш трансормувати в те що захочеш. Сподіваюся у цьому випадку у посмішку.""")
    time.sleep(15)

def Continue(update, context):
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                             text="""Мої мікросхеми дають слово творцю: Продовження? На початку цей бот створювався для котів, для того щоб можно було заспамити КОТАМИ НА 70К повідомлень. І завжди про нього пам'ятав. Взагалі будь яка ідея або проект залишається у моїй пам'яті. І може пройти час, але я дороблю те що хотів. Чи хотів зробити цей розділ таким? Якщо взяти основні напрямки:\nПосмішка;\nТепло;\nЗадоволення.\n Можливо, але не мені відповідати на це питання. Колись коли я був малий і не знав як працює ліфт. Думав що там ціла система різних ліфтів, які літають по будинку до кожного поверху. Пам'ятаю як біг на поверх нижче щоб проїхати на іншому ліфті. Це як у мультфільмі Корпорація Монстрів, тільки там були лише двері. Я не казав про це дорослим, тому що знав що вони скажуть що це не так. Себто я знав що це не правда, але я хотів в це вірити, тому що так було цікавіше. А потім коли виходив з ліфта та йшов сам до школи, починав бігти просто так, не тому що я хотів тренуватися, або бігати зранку, ні. В мене була ціль до якої хотів дійти швидше ніж я можу. Все що я можу в кінці сказати, це те що сила людини позначається не в фізичних кондиціях, а в ідеології, яку формує сама людина на протязі всього життя.""",
                             message_id=update.callback_query.message.message_id)
def Kill(update, context):
    context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                             text="""До речі, я пам'ятаю як давав обіцянку вбити того хто буде тебе бісити. Але що якщо це буде я? Якщо це буду я, даю письмову розписку про те, що ви зможете засняти те, як я себе вб'ю. Можу навіть віддати вам все потрібне для цього, а там все захочете """,
                             message_id=update.callback_query.message.message_id)
def Rest(update, context, status = True):
    if status:
        context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                 text="""Запоскійливе у 6 циклів на 1 хвилину. Знайдіть місце де вас не буде ніхто торбувати цілу хвилину, або абстрагуйте свої думки. Відчуйте темп. Також ви можете використовувати вібро задля того, щоб відчувати темп дихання(не забудьте увімкнути вібро на телефоні))""",
                                 reply_markup=Keyboard.InlineKeyboard(AnswerFour, False))
    else:
        for i in range(6):
            if i == 0:
                time.sleep(5)
            context.bot.send_message(chat_id=update.callback_query.message.chat_id,text="""Вдих""")
            time.sleep(5)
            context.bot.send_message(chat_id=update.callback_query.message.chat_id,text="""Видих""")
            time.sleep(5)
