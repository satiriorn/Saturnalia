from googletrans import Translator
import badge, DB, CreateVoice
def translate(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat.id)
    try:
        if badge.CommandTranslate != True:
            context.bot.send_message(update.message.chat_id, answer["14"])
            badge.CommandTranslate = True
            return
        translator = Translator()
        result = ''
        lang = None
        if update.message.chat.type == "private":
            lang = DB.DataBase.GetTranslateLanguage(badge.DB, update.message.chat.id)
        else:
            lang = DB.DataBase.GetTranslateLanguage(badge.DB, update.message.chat.id)
        translations = translator.translate([update.message.text], dest=lang)
        for translation in translations:
            result = translation.text
        CreateVoice.TranslateVoice(update, context, result, lang)
        badge.CommandTranslate = False
    except Exception:
        badge.CommandTranslate = False
        context.bot.send_message(update.message.chat.id, answer["15"])

