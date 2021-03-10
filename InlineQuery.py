from uuid import uuid4
from telegram import InlineQueryResultArticle, InlineQueryResultAudio, InlineQueryResultCachedAudio, InputMediaPhoto, ParseMode, InputTextMessageContent, \
    InlineQueryResultCachedVoice, \
    InlineQueryResultPhoto, InputMessageContent, InlineQueryResultCachedPhoto
from telegram.utils.helpers import escape_markdown

class Inline:
    _mafina = None
    def __init__(self, M):
        Inline._mafina = M

    @classmethod
    def inlinequery(self, update, context):
        print(update)
        query = update.inline_query.query
        result = []
        print(update.inline_query)
        chat_id = update.inline_query.from_user.id
        if "https://www.youtube"in query:
            self._mafina.UseCommand[chat_id] = "Audio"
            file_id = self._mafina._youtube.Get_Audio(update, context, "", chat_id, True)
            print(file_id)
            self._mafina.UseCommand.pop(chat_id)
            result.append(InlineQueryResultCachedAudio(
                id=0,
                audio_file_id = file_id,
                parse_mode=ParseMode.MARKDOWN))
        else:
            if len(str(query))> 0:
                res = self._mafina._youtube.YoutubeSearch(query)
                for x in range(len(res)):
                    title = res[x]['title']
                    print(title)
                    description = res[x]['channel']
                    url = res[x]['url_suffix']
                    print(description)
                    result.append(InlineQueryResultArticle(
                        id=x,
                        title=str(title),
                        description=str(description),
                        input_message_content=InputTextMessageContent("https://www.youtube.com/watch?v="+str(url)),
                        parse_mode=ParseMode.MARKDOWN))
            print(result[0])
        """

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
        """
        #self._mafina.ResulInline[update.inline_query.chat_id] = result
        update.inline_query.answer(result)

