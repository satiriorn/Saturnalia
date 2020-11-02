from pydub import AudioSegment
import badge, DB, AddMusic, os

def Cut(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    print(update)
    if badge.Cute == True and update.message.text == None:
        file = context.bot.getFile(update.message.audio.file_id)
        title = update.message.audio.title
        if title!=None:
            file.download(title+'.mp3')
        else:
            title = "ExtractTrack.mp3"
            file.download(title)
        context.bot.send_message(update.message.chat_id, answer["33"])
    elif badge.Cute == True and update.message.text != None:
        time = str(update.message.text).split('-')
        start = (time[0]).split(':')
        finish = (time[1]).split(':')
        startMin = int(start[0])
        startSec = int(start[1])
        endMin = int(finish[0])
        endSec = int(finish[1])
        startTime = startMin * 60 * 1000 + startSec * 1000
        endTime = endMin * 60 * 1000 + endSec * 1000
        NameMusic = AddMusic.GetMp3()
        song = AudioSegment.from_mp3(NameMusic[0])
        extract = song[startTime:endTime]
        ExtractName = NameMusic[0].replace('.mp3',"")+'-extract.mp3'
        extract.export(ExtractName, format="mp3")
        context.bot.send_audio(update.message.chat_id, open(ExtractName, 'rb'))
        remove(NameMusic[0])
        remove(ExtractName)
        badge.Cute = False
    else:
        context.bot.send_message(update.message.chat_id, answer["32"])
        badge.Cute = True

def remove(name):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), name)
    os.remove(path)