from pydub import AudioSegment
import badge
def Cut(update, context):
    print(update)
    if badge.Cute == True:
        file = context.bot.getFile(update.message.audio.file_id)
        file.download('jopa.mp3')
        startMin = 0
        startSec = 5
        endMin = 0
        endSec = 16

        startTime = startMin*60*1000+startSec*1000
        endTime = endMin*60*1000+endSec*1000

        #song = AudioSegment.from_mp3('ＤＥＳＯＬＡＴＥ - NIGHTDRIVE PHONK MIX.mp3')
        #extract = song[startTime:endTime]

        #extract.export('ＤＥＳＯＬＡＴＥ - NIGHTDRIVE PHONK MIX-extract.mp3', format="mp3")
        badge.Cute = False
    else:
        badge.Cute = True