import os, pytube, subprocess
from mutagen.easyid3 import EasyID3
from youtube_search import YoutubeSearch
class Youtube:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            Youtube._instance = super(Youtube, cls).__new__(cls)
            Youtube._mafina = M
            return Youtube._instance

    @classmethod
    def Start(self, update, context, answer, lang):
        context.bot.send_message(update.message.chat_id, answer["34"],
                                 reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.YoutubeKeyboard[lang], False))

    @classmethod
    def Get_Audio(self, update, context, answer, chat_id, inline = False):
        file, NameMusic = "", ""
        try:
            if chat_id in self._mafina.UseCommand.keys():
                if self._mafina.UseCommand[chat_id] == "Audio":
                    url= (lambda x: update.inline_query.query if x == True else update.message.text)(inline)
                    print(url)
                    try:
                        youtube = pytube.YouTube(url).streams.filter(only_audio=True).first()
                        file = youtube.download()
                    except Exception:
                         youtube = pytube.YouTube(url).streams.filter(only_audio=True).all()
                         file = youtube[0].download()
                    details = pytube.YouTube(url).player_response['videoDetails']
                    print(details)
                    NameMusic = file.replace('.mp4','.mp3')
                    subprocess.call([
                        'ffmpeg',
                        '-i', os.path.join(file),
                        os.path.join(NameMusic)
                    ])
                    audio = EasyID3(NameMusic)
                    audio['title'] = details['title'].replace(details['author'], "").replace('- ','')
                    audio['artist'] = details['author']
                    audio.save()
                    if inline:
                        infom = context.bot.send_audio("1243553196", open(NameMusic, 'rb'))
                        self._mafina._youtube.DeletePath(NameMusic)
                        self._mafina._youtube.DeletePath(file)
                        return infom.audio.file_id
                    else:
                        context.bot.send_audio(chat_id, open(NameMusic, 'rb'))
                        self._mafina.UseCommand.pop(chat_id)
                        self.DeletePath(NameMusic)
                        self.DeletePath(file)
            else:
                context.bot.edit_message_text(chat_id=chat_id, text=answer["1"], message_id=update.callback_query.message.message_id)
                self._mafina.UseCommand[str(chat_id)] = "Audio"
        except Exception:
            self._mafina.UseCommand.pop(str(chat_id))
            context.bot.send_message(chat_id, answer["2"])
            self.DeletePath(NameMusic)
            self.DeletePath(file)

    @classmethod
    def Get_Video(self, update, context, answer, chat_id):
        file = ""
        try:
            if chat_id in self._mafina.UseCommand.keys():
                if self._mafina.UseCommand[chat_id] == "Video":
                    video_url = update.message.text
                    youtube = pytube.YouTube(video_url).streams.first()
                    file = youtube.download()
                    context.bot.send_video(update.message.chat_id, open(file, 'rb'))
                    self._mafina.UseCommand.pop(str(chat_id))
                    self.DeletePath(file)
            else:
                context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["1"],
                                              message_id=update.callback_query.message.message_id)
                self._mafina.UseCommand[str(chat_id)] = "Video"
        except Exception:
            self._mafina.UseCommand.pop(str(chat_id))
            context.bot.send_message(chat_id, answer["2"])
            self.DeletePath(file)

    @staticmethod
    def GetFormat(format = '.mp3'):
        NameMusic = [f for f in os.listdir(os.getcwd()) if f.endswith(format)]
        if format == '.mp3':NameMusic.remove("voice.mp3")
        return NameMusic

    @staticmethod
    def DeletePath(NameMusic):
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), NameMusic))
        #results = YoutubeSearch('Знову подивився тренди YouTube: шок', max_results=10).to_dict()