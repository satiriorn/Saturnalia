from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent

class Inline:
    _mafina = None
    def __init__(self, M):
        Inline._mafina = M

    @classmethod
    def inlinequery(self, update, context):
        query = update.inline_query.query
        result = []
        chat_id = update.inline_query.from_user.id
        if len(str(query)) > 0:
            res = self._mafina._youtube.YoutubeSearch(query)
            for x in range(len(res)):
                title = res[x]['title']
                description = res[x]['channel']
                url = res[x]['url_suffix']
                result.append(InlineQueryResultArticle(
                    id=x,
                    title=str(title),
                    description=str(description),
                    input_message_content=InputTextMessageContent("https://www.youtube.com/" + str(url)),
                    parse_mode=ParseMode.MARKDOWN))
        self._mafina.ResultInline[chat_id] = result
        update.inline_query.answer(results=result, cache_time=0, timeout=190000)