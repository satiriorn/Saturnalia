import os, pytube, subprocess
from mutagen.easyid3 import EasyID3
from youtube_search import YoutubeSearch
class Youtube:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            Youtube._instance = super(Youtube, cls).__new__(cls)
            Youtube._mafina = M
            cls.user_link = {}
            return Youtube._instance

    @classmethod
    def Start(self, update, context, answer, lang):
        context.bot.send_message(update.message.chat_id, answer["34"],
                                 reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.YoutubeKeyboard[lang], False))

    @classmethod
    def Get_Audio(self, update, context, answer, chat_id, inline = False):
        file, NameMusic = "", ""
        #try:
        if chat_id in self._mafina.UseCommand.keys():
            if self._mafina.UseCommand[chat_id] == "ChooseQuality":
                print(update.message.text)
                youtube = pytube.YouTube(update.message.text)
                self.user_link[chat_id] = youtube
                quality = []
                all_stream = youtube.streams.filter(only_audio=True)
                for x in range(len(all_stream)):
                    quality.append(all_stream[x].abr)
                self._mafina.UseCommand.pop(chat_id)
                self._mafina.UseCommand[chat_id] = "Audio"
                if len(quality) > 1:
                    context.bot.send_message(update.message.chat_id, answer["77"],
                                         reply_markup=self._mafina._keyboard.InlineKeyboard(quality, False))

                #url = (lambda x: update if x == True else update.message.text)(inline)
                #print(url)
            elif self._mafina.UseCommand[chat_id] == "Audio":
                context.bot.edit_message_text(chat_id=chat_id, text=answer["53"],
                                              message_id=update.callback_query.message.message_id)
                try:
                    file = self.user_link[chat_id].streams.filter(only_audio=True, abr=update.callback_query.data).first().download()
                except Exception:
                     youtube = self.user_link[chat_id].streams.filter(only_audio=True, abr=update.callback_query.data).last().download()
                     file = youtube[0].download()
                details = self.user_link[chat_id]
                print(details)
                NameMusic = details.title.replace(details.author, "").replace("- Topic -", "")+".mp3"
                subprocess.call([
                    'ffmpeg',
                    '-i', os.path.join(file),
                    os.path.join(NameMusic)
                ])
                audio = EasyID3(NameMusic)
                audio['title'] = details.title.replace(details.author, "").replace("- Topic -", "")
                audio['artist'] = details.author
                audio.save()
                context.bot.send_audio(chat_id, open(NameMusic, 'rb'))
                self._mafina.UseCommand.pop(chat_id)
                self.DeletePath(NameMusic)
                self.DeletePath(file)
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["1"], message_id=update.callback_query.message.message_id)
            self._mafina.UseCommand[chat_id] = "ChooseQuality"
        #except Exception:
            #self._mafina.UseCommand.pop(chat_id)
            #context.bot.send_message(chat_id, answer["2"])
            #self.DeletePath(NameMusic)
            #self.DeletePath(file)

    @classmethod
    def Get_Video(self, update, context, answer, chat_id):
        file = ""
        try:
            if chat_id in self._mafina.UseCommand.keys():
                if self._mafina.UseCommand[chat_id] == "Video":
                    video_url = update.message.text
                    youtube = pytube.YouTube(video_url).streams.filter(res = "720p").first()
                    file = youtube.download()
                    context.bot.send_video(update.message.chat_id, open(file, 'rb'))
                    self._mafina.UseCommand.pop(chat_id)
                    self.DeletePath(file)
            else:
                context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["1"],
                                              message_id=update.callback_query.message.message_id)
                self._mafina.UseCommand[chat_id] = "Video"
        except Exception:
            self._mafina.UseCommand.pop(chat_id)
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

    @staticmethod
    def YoutubeSearch(Name): return YoutubeSearch(Name, max_results=5).to_dict()