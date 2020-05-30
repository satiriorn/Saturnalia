from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputMediaPhoto, ParseMode, InputTextMessageContent, \
    InlineQueryResultCachedVoice, \
    InlineQueryResultPhoto, InputMessageContent, InlineQueryResultCachedPhoto
from telegram.utils.helpers import escape_markdown
from uuid import uuid4
import badge, re, sqlite3, start, help, weather, Evtuh, text
from time import sleep
from gtts import gTTS
import pyttsx3
from googletrans import Translator


def main():
    updater = Updater(badge.token)
    dispatcher = updater.dispatcher
    start_command_handler = CommandHandler('start', start.start)
    help_command_handler = CommandHandler('help', help.help)
    weather_command_handler = CommandHandler('weather', weather.weather)
    evtuh_command_handler = CommandHandler('evtuh', Evtuh.Evtuh)
    text_message_handler = MessageHandler(Filters.text, text.text)

    dispatcher.add_handler(evtuh_command_handler)
    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(help_command_handler)
    dispatcher.add_handler(weather_command_handler)
    dispatcher.add_handler(text_message_handler)

    updater.start_polling(clean=True)
    
if __name__ == '__main__':
    main()