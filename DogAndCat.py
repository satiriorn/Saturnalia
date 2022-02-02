import Url, telegram.ext, datetime, os
from subprocess import check_output
import json
import subprocess


class Animal:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            Animal._instance = super(Animal, cls).__new__(cls)
            Animal._mafina = M
            return Animal._instance

    @staticmethod
    def Cat_photo(update, context, answer):
        try:
            Url.Photo(Url.get_url('https://api.thecatapi.com/v1/images/search'), update, context)
        except Exception:
            context.bot.send_message(context.bot_data[update.poll_answer.poll_id], answer["6"])

    @staticmethod
    def Dog_photo(update, context, answer):
        try:
            Url.Photo(Url.get_url('https://random.dog/woof.json'), update, context)
        except Exception:
            context.bot.send_message(context.bot_data[update.poll_answer.poll_id], answer["7"])

    @staticmethod
    def has_audio_streams(file_path):
        command = ['ffprobe', '-show_streams',
                   '-print_format', 'json', file_path]
        output = check_output(command)
        parsed = json.loads(output)
        streams = parsed['streams']
        audio_streams = list(filter((lambda x: x['codec_type'] == 'audio'), streams))
        return len(audio_streams) > 0

    @staticmethod
    def has_audio(filename):
        print(filename)
        result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                 "format=nb_streams", "-of",
                                 "default=noprint_wrappers=1:nokey=1", filename],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        return (int(result.stdout) - 1)

    @classmethod
    def StartSysAnimal(self):
        cursor = self._mafina._DB.UsersSysAnimal()
        target_tzinfo = datetime.timezone(datetime.timedelta(hours=3))
        target_time = None
        #times = [12, 9, 22, 18]
        winter_times = [13, 10, 23, 19]
        for x in cursor:
            for y in range(len(x)):
                if y + 2 < len(x):
                    for i in range(x[y+2]):
                        target_time = datetime.time(hour=winter_times[i], minute=00, second=15).replace(tzinfo=target_tzinfo)
                        self._mafina.jobchat[str(x[y])] = self._mafina.job.run_daily(self.AnimalJob, target_time,
                                                                             context=x[y])

    @classmethod
    def SysAnimal(self, update, context, answer, lang, chat_id):
        keyboard = self._mafina._keyboard
        mafina = self._mafina
        if chat_id in mafina.UseCommand.keys():
            cursor = mafina._DB.CheckUserInJob(chat_id)
            target_tzinfo = datetime.timezone(datetime.timedelta(hours=3))
            target_time = datetime.time(hour=9, minute=00, second=25).replace(tzinfo=target_tzinfo)
            for x in cursor:
                if str(x[0]) == str(chat_id):
                    print(len(keyboard.AnimalButton[lang]))
                    if update.callback_query.data == keyboard.AnimalButton[lang][len(keyboard.AnimalButton[lang])-1]:
                        self.ShowCountOfAnimal(update, context, answer, chat_id)
                        mafina.UseCommand.pop(chat_id)
                        return 0
                    else:
                        for y in range(len(keyboard.AnimalButton[lang])-1):
                            if update.callback_query.data == keyboard.AnimalButton[lang][0]:
                                mafina._DB.UpdateSysAnimal(chat_id, False)
                                break
                            elif update.callback_query.data == keyboard.AnimalButton[lang][y]:
                                print(y)
                                mafina._DB.UpdateFrequency(y, chat_id)
                                if x[1] == False:
                                    mafina._DB.UpdateSysAnimal(chat_id, True)

                else:
                    mafina._DB.InsertSysAnimal(chat_id, True)
                    mafina.jobchat[chat_id] = mafina.job.run_daily(self.AnimalJob, target_time, context=chat_id)
            context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                          message_id=update.callback_query.message.message_id)
            mafina.UseCommand.pop(chat_id)
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["56"],
                                          message_id=update.callback_query.message.message_id)
            context.bot.edit_message_reply_markup(chat_id, reply_markup=keyboard.InlineKeyboard(keyboard.AnimalButton[lang], False),
                                                  message_id=update.callback_query.message.message_id)
            mafina.UseCommand[str(chat_id)] = "ChangeSysAnimal"

    @classmethod
    def ShowCountOfAnimal(self, update, context, answer, chat_id):
        context.bot.edit_message_text(chat_id=chat_id, text=answer["76"].format(self._mafina._DB.GetCountOfFileAnimal(),
                                    self._mafina._DB.GetCountOfFileAnimal() - self._mafina._DB.GetCountAnimal(chat_id)),
                                      message_id=update.callback_query.message.message_id)


    @staticmethod
    def AnimalJob(context: telegram.ext.CallbackContext):
       try:
            x = Animal._mafina._DB.GetCountAnimal(context.job.context)
            fileID = Animal._mafina._DB.GetFileId(x)
            file = context.bot.getFile(fileID)
            if '-' in str(context.job.context):
                a = str(context.job.contex).replace('-', '')
                title = ("""{0}.gif""").format(a)
            else:
                title = ("""{0}.gif""").format(context.job.context)
            file.download(title)
            if(Animal.has_audio(title)):
                context.bot.send_video(context.job.context, open(title, 'rb'))
            else:
                context.bot.send_animation(context.job.context, open(title, 'rb'))
            Animal._mafina._DB.UpCountAnimal(context.job.context)
            os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), title))
       except Exception:
           Animal._mafina._DB.UpCountAnimal(context.job.context)