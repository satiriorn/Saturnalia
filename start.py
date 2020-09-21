import Keyboard, DB, badge
def start(update, context):
    print(update)
    try:
        first_name = update.message.chat.first_name
        chat_id = update.message.chat_id
        k = Keyboard.InitKeyboard()

        if update.message.chat.type == "private":
            DB.DataBase.CheckUser(badge.DB, first_name, update.message.chat.username, chat_id,
                                  update.message.from_user.language_code, update.message.chat.type)
            if 'Rositsa Maneva' in first_name:
                context.bot.send_message(chat_id, """Слава создателю, мне написала сама """ + first_name)
                context.bot.send_message(chat_id,
                                 """Честно говоря, я не ожидал тебя здесь увидеть, но для меня большая честь видеть вас тут(Я поцеловал ваш телефон в микросхему, сейчас он улыбается, можете погладить его), а для вас у меня особая программа...УХАХАХАХАХА """)

            else:
                context.bot.send_message(chat_id, """Добридень, """ + first_name + badge.answer,reply_markup=k)
        else:
            DB.DataBase.CheckUser(badge.DB,update.message.chat.title,update.message.chat.username, chat_id,
            update.message.from_user.language_code, update.message.chat.type)
            context.bot.send_message(chat_id, badge.answer, reply_markup=k)
    except Exception:
        context.bot.send_message(update.message.chat_id, 'Вибач, але я вмер, тому не зможу тобі відповідати.')
