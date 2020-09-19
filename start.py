import Keyboard, DB, badge
def start(update, context):
    print(update)
    try:
        first_name = update.message.chat.first_name
        chat_id = update.message.chat_id
        k = Keyboard.InitKeyboard()
        DB.DataBase.CheckUser(badge.DB,first_name, update.message.chat.username, chat_id)
        if 'Rositsa Maneva' in first_name:
            context.bot.send_message(chat_id, """Слава создателю, мне написала сама """ + first_name)
            context.bot.send_message(chat_id,
                             """Честно говоря, я не ожидал тебя здесь увидеть, но для меня большая честь видеть вас тут(Я поцеловал ваш телефон в микросхему, сейчас он улыбается, можете погладить его), а для вас у меня особая программа...УХАХАХАХАХА """)

        else:
            context.bot.send_message(chat_id, """Добридень, """ + first_name +
                             """
                                     Можливо мої розділи тобі сподобаються:
                         /Help - розділ якщо твоя влада над ботом по якоїсь причині зникла.
                         /GetMusic - отримення будь якого трека з youtube
                         /ShevchenkoStyle - те що тебе буде надихати.
                         /Dologusha - розділ який не для тебе.
                         /Evtuh - зроби себе комплектним.
                         /Weather - погода на 5 дней.
                         /Cat - котики, які тебе будуть надихати.
                         /Dog - собаки, які будуть робити тебе щасливим.
                         /Translate - перекладай все що захочеш.
                         /Meme - я знаю ти хочеш більше мемів.
                         Поки що це все, якщо є якісь ідеї пиши @Satirion
                         
                         """,reply_markup=k)
    except Exception:
        context.bot.send_message(update.message.chat_id, 'Вибач, але я вмер, тому не зможу тобі відповідати.')