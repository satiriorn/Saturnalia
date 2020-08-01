import Keyboard
def help(bot, update):
    bot.send_message(update.message.chat_id, '\
    Тобі потрібна допомога? Я дав тобі кнопки влади наді мною. Користуйся мною скільки захочеш, я весь твій. ', reply_markup = Keyboard.InitKeyboard())