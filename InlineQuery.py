from uuid import uuid4
import DogAndCat,Evtuh, weather, CreateVoice
from telegram import InlineQueryResultArticle, InputMediaPhoto, ParseMode, InputTextMessageContent, \
    InlineQueryResultCachedVoice, \
    InlineQueryResultPhoto, InputMessageContent, InlineQueryResultCachedPhoto
from telegram.utils.helpers import escape_markdown

def inlinequery(bot, update):
    try:
        query = update.inline_query.query
        photo = DogAndCat.get_url_dog()
        print(update)
        result = []
        results = []
        if len(str(query))!= 0:
            print("1")
            result.append(InlineQueryResultArticle(
                id=uuid4(),
                title="Word of God",
                description='Добавь слово божье в свой диалог',
                thumb_url=photo,
                input_message_content=InputTextMessageContent(
                    Evtuh.Evtuh(bot, query, False)),
                parse_mode=ParseMode.MARKDOWN))

            result.append(InlineQueryResultArticle(
                id=uuid4(),
                title="Current Weather",
                thumb_url=photo,
                description='Текуущая погодка',
                input_message_content=InputTextMessageContent(
                    weather.CurrentWeather(bot, update, False)),
                parse_mode=ParseMode.MARKDOWN))

            result.append(InlineQueryResultArticle(
                id=uuid4(),
                title="Bold",
                description='Курсивчіку мені',
                thumb_url=photo,
                input_message_content=InputTextMessageContent(
                    "_{}_".format(escape_markdown(query)),
                    parse_mode=ParseMode.MARKDOWN)))

            result.append(InlineQueryResultArticle(
                id=uuid4(),
                title="Caps",
                thumb_url=photo,
                description='Увеличу твой тексток',
                input_message_content=InputTextMessageContent(
                    query.upper()),
                parse_mode=ParseMode.MARKDOWN))
        else:
            result.append(InlineQueryResultPhoto(
                id=uuid4(),
                title="Cat",
                description='Получить дозу котика прямо сейчас',
                photo_url=DogAndCat.get_url_cat(),
                thumb_url=photo,
                parse_mode=ParseMode.MARKDOWN))

            result.append(InlineQueryResultPhoto(
                id=uuid4(),
                title="Dog",
                description='Получить дозу собак прямо сейчас',
                photo_url=DogAndCat.get_url_dog(),
                thumb_url=photo,
                parse_mode=ParseMode.MARKDOWN))

        update.inline_query.answer(result)
    except:
        u = 'update.inline_query.from.id'
        bot.send_message(u, 'Чуть позже, мнээ плохо...')

