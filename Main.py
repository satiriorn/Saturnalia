import Quotes, start, help, weather, Evtuh, text,  CreateVoice, DogAndCat, InlineQuery, os, Meme, AddMusic, Translate
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler

def main():
    updater = Updater(os.getenv("TOKEN"), use_context=True)
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
    addmusic_command_handler = CommandHandler("GetMusic", AddMusic.single_download)
    translate_command_handler = CommandHandler("Translate", Translate.translate)
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
    dispatcher.add_handler(addmusic_command_handler)
    dispatcher.add_handler(translate_command_handler)
    dispatcher.add_handler(text_message_handler)

    dispatcher.add_handler(InlineQueryHandler(InlineQuery.inlinequery))

    updater.start_polling(timeout=5000, poll_interval=5)
    updater.idle()
if __name__ == '__main__':
    main()