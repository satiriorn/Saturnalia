from uuid import uuid4
from telegram import InlineQueryResultArticle, InlineQueryResultAudio, InputMediaPhoto, ParseMode, InputTextMessageContent, \
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
        if len(str(query))> 0:
            res = self._mafina._youtube.YoutubeSearch(query)
            for x in range(len(res)):
                title = res[x]['title']
                print(title)
                description = res[x]['channel']
                url = res[x]['url_suffix']
                print(description)
                result.append(InlineQueryResultAudio(
                    id=x,
                    title=str(title),
                    audio_url = "https://r1---sn-quxapm-3c2l.googlevideo.com/videoplayback?expire=1615124671&ei=X4REYMfPH_qkxN8PiKiiwA4&ip=94.131.198.219&id=o-ABUT4amaE9AR9z_CfbTsTM1KWq7kKVKziefX_T7SiVqG&itag=18&source=youtube&requiressl=yes&mh=Po&mm=31%2C29&mn=sn-quxapm-3c2l%2Csn-3c27sn7d&ms=au%2Crdu&mv=m&mvi=1&pl=22&initcwndbps=1557500&vprv=1&mime=video%2Fmp4&ns=IiFYnRHvlaaFkTwOz2UavAcF&gir=yes&clen=20940795&ratebypass=yes&dur=232.222&lmt=1542475001649688&mt=1615102850&fvip=14&fexp=24001374%2C24007246&c=WEB&txp=5531432&n=ZVDJeIuGjUYCG72cfU&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIga3FmnT-dmVT5NVhotAQvTtU1DSJ9YtegPpkVV08PVYwCIQDjKF04IbpiYDkmRYgdVxF2ykVVtAtXQ-WJ_NsdaYFJcQ%3D%3D&sig=AOq0QJ8wRAIgQmc6tX2AKLV783izotv3wqJ-6BUB4y-oI81NrJEPDAwCIEPe1PLToJjKAseLqR1J-aYKPkEX4AHS8v7IDEThzGYf",
                    description=str(description),
                    input_message_content=InputTextMessageContent(str(url)),
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

