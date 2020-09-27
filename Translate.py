from googletrans import Translator
import badge, DB, CreateVoice
def translate(update, context):
    try:
        if badge.CommandTranslate != True:
            context.bot.send_message(update.message.chat_id, "Чекаю на текст:")
            badge.CommandTranslate = True
            return
        translator = Translator()
        result = ''
        lang = None
        if update.message.chat.type == "private":
            lang = DB.DataBase.GetTranlateLanguage(badge.DB, update.message.chat.first_name)
        else:
            lang = DB.DataBase.GetTranlateLanguage(badge.DB, update.message.chat.title)
        translations = translator.translate([update.message.text], dest=lang)
        for translation in translations:
            result = translation.text
        CreateVoice.TranslateVoice(update, context, result, lang)
        badge.CommandTranslate = False
    except Exception:
        badge.CommandTranslate = False
        context.bot.send_message(update.message.chat.id, 'Щось пішло не так спробуй ще раз.')

