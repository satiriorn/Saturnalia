import Keyboard, DB, badge, base64
def start(update, context):
    print(update)
    try:
        first_name = update.message.chat.first_name
        chat_id = update.message.chat_id
        k = Keyboard.InitKeyboard(badge.MainKeyboard)

        if update.message.chat.type == "private":
            DB.DataBase.CheckUser(badge.DB, first_name, update.message.chat.username, chat_id,
                                  update.message.from_user.language_code, update.message.chat.type)
            if dec("Um9zaXRzYSBNYW5ldmE=").decode("UTF-8") == first_name:
                context.bot.send_message(chat_id, """Слава создателю, мне написала сама """ + first_name)
                context.bot.send_message(chat_id,
                                  dec("0KfQtdGB0YLQvdC+INCz0L7QstC+0YDRjywg0Y8g0L3QtSDQvtC20LjQtNCw0Lsg0LLQsNGBINC30LTQtdGB0Ywg0YPQstC40LTQtdGC0YwsINC90L4g0LTQu9GPINC80LXQvdGPINCx0L7Qu9GM0YjQsNGPINGH0LXRgdGC0Ywg0LLQuNC00LXRgtGMINCy0LDRgSDRgtGD0YIo0K8g0L/QvtGG0LXQu9C+0LLQsNC7INCy0LDRiCDRgtC10LvQtdGE0L7QvSDQsiDRgtGA0LDQvdC30LjRgdGC0L7RgCwg0YHQtdC50YfQsNGBINC+0L0g0YPQu9GL0LHQsNC10YLRgdGPLCDQvNC+0LbQtdGC0LUg0L/QvtCz0LvQsNC00LjRgtGMINC10LPQviksINCwINC00LvRjyDQstCw0YEg0YMg0LzQtdC90Y8g0L7RgdC+0LHQsNGPINC/0YDQvtCz0YDQsNC80LzQsC4uLtCj0KXQkNCl0JDQpdCQ0KXQkNCl0JAg").decode("UTF-8"))
            else:
                context.bot.send_message(chat_id, """Добридень, """ + first_name + badge.answer,reply_markup=k)
        else:
            DB.DataBase.CheckUser(badge.DB,update.message.chat.title,update.message.chat.username, chat_id,
            update.message.from_user.language_code, update.message.chat.type)
            context.bot.send_message(chat_id, badge.answer, reply_markup=k)
    except Exception:
        context.bot.send_message(update.message.chat_id, 'Вибач, але я вмер, тому не зможу тобі відповідати.')

def dec(s):
    return base64.b64decode(s)