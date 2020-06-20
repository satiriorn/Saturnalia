from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import Quotes, start, help, weather, Evtuh, text,  CreateVoice, DogAndCat, InlineQuery, os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler

def main():
    TOKEN = os.getenv("TOKEN")
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    start_command_handler = CommandHandler('Start', start.start)
    help_command_handler = CommandHandler('Help', help.help)
    weather_command_handler = CommandHandler('Weather', weather.weather)
    evtuh_command_handler = CommandHandler('Evtuh', Evtuh.Evtuh)
    voice_command_handler = CommandHandler("Voice", CreateVoice.voice)
    cat_command_handler = CommandHandler('Cat', DogAndCat.Cat_photo)
    dog_command_handler = CommandHandler('Dog', DogAndCat.Dog_photo)
    text_message_handler = MessageHandler(Filters.text, text.text)
    Sheva_command_handler = CommandHandler('ShevchenkoStyle', Quotes.ShevchenkoStyle)

    dispatcher.add_handler(evtuh_command_handler)
    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(help_command_handler)
    dispatcher.add_handler(weather_command_handler)
    dispatcher.add_handler(voice_command_handler)
    dispatcher.add_handler(cat_command_handler)
    dispatcher.add_handler(dog_command_handler)
    dispatcher.add_handler(text_message_handler)
    dispatcher.add_handler(Sheva_command_handler)
    dispatcher.add_handler(InlineQueryHandler(InlineQuery.inlinequery))

    updater.start_polling(timeout=5000, poll_interval=5)

if __name__ == '__main__':
    main()