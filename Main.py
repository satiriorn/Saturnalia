from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import badge, start, help, weather, Evtuh, text


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