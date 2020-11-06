from googletrans import Translator
import badge, DB, CreateVoice

def translate(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat.id)
    try:
        if str(update.message.chat_id) in badge.UseCommand.keys():
            if badge.UseCommand[str(update.message.chat_id)] == "Translate":
                translator = Translator()
                result = ''
                lang = DB.DataBase.GetTranslateLanguage(badge.DB, update.message.chat.id)
                translations = translator.translate([update.message.text], dest=lang)
                for translation in translations:
                    result = translation.text
                CreateVoice.TranslateVoice(update, context, result, lang)
        else:
            badge.UseCommand[str(update.message.chat_id)] = "Translate"
            context.bot.send_message(update.message.chat_id, answer["14"])
    except Exception:
        context.bot.send_message(update.message.chat.id, answer["15"])

