import Quotes, start, help, weather, Evtuh, text,  CreateVoice, DogAndCat, InlineQuery, os, Meme
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from threading import Thread

def main():
    PORT = int(os.environ.get('PORT', '8443'))
    updater = Updater(os.getenv("TOKEN"), use_context=True)
    #updater.start_webhook(listen='127.0.0.1', port=5000, url_path='TOKEN')
    #dispatcher = Dispatcher(bot, update_queue)
    #thread = Thread(target=dispatcher.start, name='dispatcher')
    #thread.start()
    dispatcher = updater.dispatcher
    start_command_handler = CommandHandler('start', start.start)
    help_command_handler = CommandHandler('Help', help.help)
    weather_command_handler = CommandHandler('Weather', weather.weather)
    evtuh_command_handler = CommandHandler('Evtuh', Evtuh.Evtuh)
    voice_command_handler = CommandHandler("Voice", CreateVoice.voice)
    cat_command_handler = CommandHandler('Cat', DogAndCat.Cat_photo)
    dog_command_handler = CommandHandler('Dog', DogAndCat.Dog_photo)
    sheva_command_handler = CommandHandler('ShevchenkoStyle', Quotes.ShevchenkoStyle)
    meme_command_handler = CommandHandler('Meme', Meme.Get_meme)
    text_message_handler = MessageHandler(Filters.text, text.text)

    dispatcher.add_handler(evtuh_command_handler)
    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(help_command_handler)
    dispatcher.add_handler(weather_command_handler)
    dispatcher.add_handler(voice_command_handler)
    dispatcher.add_handler(meme_command_handler)
    dispatcher.add_handler(cat_command_handler)
    dispatcher.add_handler(dog_command_handler)
    dispatcher.add_handler(sheva_command_handler)
    dispatcher.add_handler(text_message_handler)

    dispatcher.add_handler(InlineQueryHandler(InlineQuery.inlinequery))

    updater.start_polling(timeout=100, poll_interval=3)
    updater.idle()
if __name__ == '__main__':
    main()