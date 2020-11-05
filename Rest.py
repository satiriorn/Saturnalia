import Keyboard, time, badge

def Rest(update, context, status = True):
    try:
        chat_id = update.callback_query.message.chat_id
    except Exception:
        chat_id = update.message.chat_id
        badge.RestMode = True
    if status:
        context.bot.send_message(chat_id=chat_id,
                                 text="""Запоскійливе у 6 циклів на 1 хвилину. Знайдіть місце де вас не буде ніхто торбувати цілу хвилину, або абстрагуйте свої думки. Відчуйте темп. Також ви можете використовувати вібро задля того, щоб відчувати темп дихання(не забудьте увімкнути вібро на телефоні))""",
                                 reply_markup=Keyboard.InlineKeyboard(["Занурюємося"], False))
    else:
        context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text="Починаємо", message_id=update.callback_query.message.message_id)
        for i in range(6):
            if i == 0:
                time.sleep(5)
            context.bot.send_message(chat_id=chat_id,text="""Вдих""")
            time.sleep(5)
            context.bot.send_message(chat_id=chat_id,text="""Видих""")
            time.sleep(5)
        context.bot.send_message(chat_id=update.callback_query.message.chat_id, text="Втягніть в себе максимум спокію")
        badge.RestMode = False

