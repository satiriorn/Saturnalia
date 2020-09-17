from googletrans import Translator
import badge

def translate(update, context):
    try:
        if badge.CommandTranslate != True:
            context.bot.send_message(update.message.chat_id, "Чекаю на текст:")
            badge.CommandTranslate = True
            return
        translator = Translator()
        result = ''
        translations = translator.translate([update.message.text], dest='en')
        for translation in translations:
            result = translation.text
        context.bot.send_message(update.message.chat_id, result)
        badge.CommandTranslate = False
    except Exception:
        context.bot.send_message(update.message.chat.id, 'Щось пішло не так спробуй ще раз.')