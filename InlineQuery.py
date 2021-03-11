from telegram import InlineQueryResultArticle, InlineQueryResultCachedAudio, ParseMode, InputTextMessageContent

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
        if "https://www.youtube" in query:
            self._mafina.UseCommand[chat_id] = "Audio"
            file_id = self._mafina._youtube.Get_Audio(update, context, "", chat_id, True)
            print(file_id)
            if chat_id in self._mafina.UseCommand.keys(): self._mafina.UseCommand.pop(chat_id)
            result.append(InlineQueryResultCachedAudio(
                id=0,
                audio_file_id=file_id,
                parse_mode=ParseMode.MARKDOWN))
        else:
            if len(str(query)) > 0:
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
                        input_message_content=InputTextMessageContent("https://www.youtube.com/watch?v=" + str(url)),
                        parse_mode=ParseMode.MARKDOWN))

        update.inline_query.answer(results = result, cache_time = 200000, timeout = 190000)