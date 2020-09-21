from uuid import uuid4
import DogAndCat,Evtuh, weather, CreateVoice, Meme
from telegram import InlineQueryResultArticle, InputMediaPhoto, ParseMode, InputTextMessageContent, \
    InlineQueryResultCachedVoice, \
    InlineQueryResultPhoto, InputMessageContent, InlineQueryResultCachedPhoto
from telegram.utils.helpers import escape_markdown

def inlinequery(update, context):
    try:
        query = update.inline_query.query
        photo = DogAndCat.get_url_dog()
        result = []
        if len(str(query))!= 0:
            result.append(InlineQueryResultArticle(
                id=uuid4(),
                title="Word of God",
                description='Цитати Євтушенка',
                thumb_url=photo,
                input_message_content=InputTextMessageContent(
                    Evtuh.Evtuh(context, query, False)),
                parse_mode=ParseMode.MARKDOWN))

            result.append(InlineQueryResultArticle(
                id=uuid4(),
                title="Current Weather",
                thumb_url=photo,
                description='Погода',
                input_message_content=InputTextMessageContent(
                    weather.CurrentWeather(context, update, False)),
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
                description='Не хочеш котика?',
                photo_url=DogAndCat.get_url_cat(),
                thumb_url=photo,
                parse_mode=ParseMode.MARKDOWN))

            result.append(InlineQueryResultPhoto(
                id=uuid4(),
                title="Dog",
                description='Не хочеш собаку?',
                photo_url=DogAndCat.get_url_dog(),
                thumb_url=photo,
                parse_mode=ParseMode.MARKDOWN))

            result.append(InlineQueryResultPhoto(
                id=uuid4(),
                title="MEME",
                description='MORE MEME',
                photo_url=Meme.Link(),
                thumb_url=photo,
                parse_mode=ParseMode.MARKDOWN))

        update.inline_query.answer(result)
    except:
        u = 'update.inline_query.from.id'
        bot.send_message(u, 'Вибач, мої мікросхеми згоріли, пиши пізніше...')

