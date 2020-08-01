import Keyboard
def start(bot, update):
    print(update)
    try:

        first_name = update.message.chat.first_name
        chat_id = update.message.chat_id
        k = Keyboard.InitKeyboard()
        """
        conn=sqll
        print(conn)
        cursor = conn.cursor()
        sql="SELECT Name FROM user WHEN Name=" + first_name
        cursor.execute("sql")
        results = cursor.fetchall()
        conn.close()
        print(results)"""
        if 'Rositsa Maneva' in first_name:
            bot.send_message(chat_id, """Слава создателю, мне написала сама """ + first_name)
            bot.send_message(chat_id,
                             """Честно говоря, я не ожидал тебя здесь увидеть, но для меня большая честь видеть вас тут(Я поцеловал ваш телефон в микросхему, сейчас он улыбается, можете погладить его), а для вас у меня особая программа...УХАХАХАХАХА """)

        else:
            bot.send_message(chat_id, """Добридень, """ + first_name +
                             """
                                     Можливо мої розділи тобі сподобаються:
                         /Help - розділ якщо твоя влада над ботом по якоїсь причині зникла.
                         /ShevchenkoStyle - те що тебе буде надихати.
                         /Dologusha - розділ який не для тебе.
                         /Evtuh - зроби себе комплектним.
                         /Weather - погода на 5 дней.
                         /translate - переклад який ще в розробці .
                         /Cat - котики, які тебе будуть надихати.
                         /Dog - собаки, які будуть робити тебе щасливим.
                         Поки що це все, якщо є якісь ідеї пиши @Satirion
                         
                         """,reply_markup=k)
    except Exception:
        bot.send_message(update.message.chat_id, 'Вибач, але я вмер, тому не зможу тобі відповідати.')