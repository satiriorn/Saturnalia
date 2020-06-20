import Keyboard
def start(bot, update):
    print(update)
    try:

        first_name = update.message.chat.first_name
        chat_id = update.message.chat_id
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
            bot.send_message(chat_i d,
                             """Честно говоря, я не ожидал тебя здесь увидеть, но для меня большая честь видеть вас тут(Я поцеловал ваш телефон в микросхему, сейчас он улыбается, можете погладить его), а для вас у меня особая программа...УХАХАХАХАХА """)

        else:
            bot.send_message(chat_id, """Кукусики, """ + first_name +
                             """
                                     Ладно чмо, я тебя пожалею, хотя бы назову свои интеллектуальные разделы:
                         /Help этот раздел для лохов, которые ничего не понимают..
                         /ShevchenkoStyle 
                         /Dologusha этот раздел для одной единственной девушки этой вселенной. 
                         /Evtuh если ты не знаешь кто это, ты некомплектное создание
                         /Weather погода на 5 дней
                         /translate перевод
                         /Cat рандомные котики для интровертов
                         /Dog рандомные собакены для экстравертов
                         Пока что это всё, а то твои некомплектные мозги отстали от жизни и ты сдохнешь от этого
                         
                         """,reply_markup=Keyboard.InitKeyboard())
    except Exception:
        bot.send_message(update.message.chat_id, 'Прости, но я мертв для тебя')