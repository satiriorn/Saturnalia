from pydub import AudioSegment
import os, pytube
from mutagen.easyid3 import EasyID3
from datetime import timedelta, datetime
class Cut:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            Cut._instance = super(Cut, cls).__new__(cls)
            Cut._mafina = M
            return Cut._instance
    @classmethod
    def CutStart(self, update, context, answer, lang):
        context.bot.send_message(update.message.chat_id, answer["35"],
                                 reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.CutKeyboard[lang], False))

    @classmethod
    def CutAudio(self, update, context, answer, chat_id):
        NameMusic, ExtractName = "", ""
        try:
            if chat_id in self._mafina.UseCommand.keys() and update.message.text == None:
                if self._mafina.UseCommand[chat_id] == "CutAudio":
                    file = context.bot.getFile(update.message.audio.file_id)
                    title = update.message.audio.title
                    if title!=None:
                        self._mafina.CutFile[chat_id]=file.download(title)
                    else:
                        self._mafina.CutFile[chat_id] = "ExtractTrack.mp3"
                        file.download(title)
                context.bot.send_message(update.message.chat_id, answer["33"])
            elif chat_id in self._mafina.UseCommand.keys()and update.message.text != None:
                if self._mafina.UseCommand[chat_id] == "CutAudio":
                    time = str(update.message.text).split('-')
                    start = (time[0]).split(':')
                    finish = (time[1]).split(':')
                    startMin = int(start[0])
                    startSec = int(start[1])
                    endMin = int(finish[0])
                    endSec = int(finish[1])
                    startTime = startMin * 60 * 1000 + startSec * 1000
                    endTime = endMin * 60 * 1000 + endSec * 1000
                    NameMusic = self._mafina.CutFile[str(chat_id)]
                    song = AudioSegment.from_mp3(NameMusic)
                    extract = song[startTime:endTime]
                    ExtractName = NameMusic.replace('.mp3',"")+'-extract'
                    extract.export(ExtractName, format="mp3")
                    audio = EasyID3(ExtractName)
                    audio['title'] = ExtractName
                    audio.update()
                    context.bot.send_audio(update.message.chat_id, open(ExtractName, 'rb'))
                    self._mafina.UseCommand.pop(str(chat_id))
                    self._mafina.CutFile.pop(str(chat_id))
                    self.remove(NameMusic)
                    self.remove(ExtractName)
            else:
                context.bot.edit_message_text(chat_id=chat_id, text=answer["32"], message_id=update.callback_query.message.message_id)
                self._mafina.UseCommand[str(chat_id)] = "CutAudio"
        except Exception:
            self._mafina.UseCommand.pop(str(chat_id))
            self._mafina.CutFile.pop(str(chat_id))
            self.remove(NameMusic)
            self.remove(ExtractName)
            context.bot.send_message(chat_id, answer["2"])
    @classmethod
    def CutVideo(self, update, context, answer, chat_id):
        try:
            if chat_id in self._mafina.UseCommand.keys() and update.message.text == None:
                if self._mafina.UseCommand[chat_id] == "CutVideo":
                    file = context.bot.getFile(update.message.video.file_id)
                    self._mafina.CutFile[chat_id] = file.download()
                    context.bot.send_message(update.message.chat_id, answer["33"])
            elif chat_id in self._mafina.UseCommand.keys()and update.message.text != None:
                if self._mafina.UseCommand[chat_id] == "CutVideo":
                    self.Cut(update, context, chat_id)
            else:
                context.bot.edit_message_text(chat_id=chat_id, text=answer["36"], message_id=update.callback_query.message.message_id)
                self._mafina.UseCommand[chat_id] = "CutVideo"
        except Exception:
           self.delete(update, chat_id)
    @classmethod
    def GetCutStart(self, update, context, answer, chat_id):
        file, name = "", ""
        youtube = None
        try:
            if chat_id in self._mafina.UseCommand.keys():
                if self._mafina.UseCommand[chat_id] == "GetCutVideo":
                    video_url = update.message.text
                    try:
                        youtube = pytube.YouTube(video_url).streams.first()
                        file = youtube.download()
                    except Exception:
                        youtube = pytube.YouTube(video_url).streams.all()
                        file = youtube[0].download()
                    name = str(chat_id).replace('-','')
                    print(name)
                    os.rename(file, ('{}.mp4').format(name))
                    self._mafina.CutFile[str(chat_id)]= ('{}.mp4').format(name)
                    context.bot.send_message(update.message.chat_id, answer["33"])
                    self._mafina.UseCommand.pop(str(chat_id))
                    self._mafina.UseCommand[str(chat_id)] = "CutEnd"
            else:
                context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id, text=answer["1"],
                                              message_id=update.callback_query.message.message_id)
                self._mafina.UseCommand[str(chat_id)] = "GetCutVideo"
        except Exception:
            self.delete(update, chat_id)
            context.bot.send_message(chat_id, answer["2"])
    @classmethod
    def GetCutEnd(self, update, context, answer, chat_id):
        try:
            if chat_id in self._mafina.UseCommand.keys():
                if self._mafina.UseCommand[str(chat_id)] == "CutEnd":
                    self.Cut(update, context, chat_id)
        except Exception:
            self.delete(update, chat_id)
            context.bot.send_message(chat_id, answer["2"])

    @classmethod
    def Cut(self, update, context, chat_id):
        time = str(update.message.text).split('-')
        start = self.GetDataTime(time[0])
        finish = self.GetDataTime(time[1])
        duration = finish - start
        start = datetime.strftime(start, '%H:%M:%S')
        file = str(self._mafina.CutFile[str(chat_id)])
        name = self.get_name(update)
        os.system(('ffmpeg -ss {} -i {} -to {} -c copy {}.mp4').format(str(start),
                                                                               os.path.join(file),
                                                                               str(duration),
                                                                               str(name)))
        context.bot.send_video(update.message.chat_id, open(('{}.mp4').format(str(name)), 'rb'))
        self.delete(update, chat_id)
    @classmethod
    def get_name(self, update):
        x =(lambda x: x == 'private' if update.message.chat.username else self._mafina._DB.GetIdUser(self._mafina.GetChatID(update)))(
            update.message.chat.type)
        print(x)
        return x

    @classmethod
    def delete(self, update, chat_id):
        self._mafina.UseCommand.pop(chat_id)
        file = self._mafina.CutFile[chat_id]
        self._mafina.CutFile.pop(chat_id)
        self.remove(('{}.mp4').format(str(self.get_name(update))))
        self.remove(os.path.join(file))

    @staticmethod
    def remove(name):
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), name))

    @staticmethod
    def GetDataTime(time):
        if str(time).count(':') > 1:
            return datetime.strptime(time, '%H:%M:%S')
        elif str(time).count(':') == 1:
            return datetime.strptime(time, '%M:%S')
        else:
            return datetime.strptime(time, '%S')