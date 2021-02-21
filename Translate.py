from googletrans import Translator
import badge, DB, CreateVoice

def translate(update, context):
    chat_id = update.message.chat_id
    answer, lang = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    try:
        if str(update.message.chat_id) in badge.UseCommand.keys():
            if badge.UseCommand[str(update.message.chat_id)] == "Translate":
                result = ''
                lang = DB.DataBase.GetTranslateLanguage(badge.DB, chat_id)
                translations = badge.translator.translate([update.message.text], dest=lang)
                for translation in translations:
                    result = translation.text
                CreateVoice.TranslateVoice(update, context, result, lang)
        else:
            badge.UseCommand[str(update.message.chat_id)] = "Translate"
            context.bot.send_message(update.message.chat_id, answer["14"])
    except Exception:
        badge.translator = Translator()
        context.bot.send_message(update.message.chat.id, answer["15"])
        badge.UseCommand.pop(str(update.message.chat_id))