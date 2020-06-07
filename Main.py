from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import badge, start, help, weather, Evtuh, text,  CreateVoice, DogAndCat, InlineQuery, os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler

def main():
    updater = Updater(badge.token)
    updater.start_webhook(listen="0.0.0.0",url_path=badge.token)
    updater.bot.set_webhook("https://mafina.herokuapp.com")
    updater.idle()
    dispatcher = updater.dispatcher
    start_command_handler = CommandHandler('start', start.start)
    help_command_handler = CommandHandler('help', help.help)
    weather_command_handler = CommandHandler('weather', weather.weather)
    evtuh_command_handler = CommandHandler('evtuh', Evtuh.Evtuh)
    voice_command_handler = CommandHandler("voice", CreateVoice.voice)
    cat_command_handler = CommandHandler('cat', DogAndCat.Cat_photo)
    dog_command_handler = CommandHandler('dog', DogAndCat.Dog_photo)
    text_message_handler = MessageHandler(Filters.text, text.text)

    dispatcher.add_handler(evtuh_command_handler)
    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(help_command_handler)
    #dispatcher.add_handler(weather_command_handler)
    #dispatcher.add_handler(voice_command_handler)
    dispatcher.add_handler(cat_command_handler)
    dispatcher.add_handler(dog_command_handler)
    #dispatcher.add_handler(text_message_handler)
    dispatcher.add_handler(InlineQueryHandler(InlineQuery.inlinequery))

    updater.start_polling(timeout=5000, poll_interval=5)

if __name__ == '__main__':
    main()