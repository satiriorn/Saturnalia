import base64, time, os, random
from ffmpy import FFmpeg

class StandartCommand:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            StandartCommand._instance = super(StandartCommand, cls).__new__(cls)
            StandartCommand._mafina = M
            return StandartCommand._instance

    @classmethod
    def start(self, update, context, answer, chat_id):
        try:
            self._mafina._DB.CheckUser(update.message.chat.title, update.message.chat.username, chat_id,
                update.message.from_user.language_code, update.message.chat.type)
            context.bot.send_message(chat_id, answer["start"], reply_markup = self._mafina._keyboard.InitKeyboard(self._mafina._keyboard.MainKeyboard))
            self._mafina._setting.LanguageBot(update, context, answer, chat_id, True)
        except Exception:
            context.bot.send_message(update.message.chat_id, answer["0"])
    @classmethod
    def help(self, update, context, answer):
        context.bot.send_message(update.message.chat_id, answer["8"],
                                 reply_markup = self._mafina._keyboard.InitKeyboard(self._mafina._keyboard.MainKeyboard))

    @classmethod
    def Rest(self, update, context, answer, lang, chat_id, status=True):
        self._mafina.UseCommand[chat_id] = "Rest"
        if status:
            context.bot.send_message(chat_id=chat_id, text=answer["65"],
                                     reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.RestButton[lang], False))
        else:
            context.bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                          text=self._mafina._keyboard.RestButton[lang][0],
                                          message_id=update.callback_query.message.message_id)
            for i in range(6):
                if i == 0: time.sleep(5)
                context.bot.send_message(chat_id=chat_id, text=answer["66"])
                time.sleep(5)
                context.bot.send_message(chat_id=chat_id, text=answer["67"])
                time.sleep(5)
            context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=answer["68"])
            self._mafina.UseCommand.pop(chat_id)

    @classmethod
    def convert(self, update, context, answer, chat_id):
        if chat_id in self._mafina.UseCommand.keys():
            if self._mafina.UseCommand[chat_id] == "ConfirmSendVideo":
                file = context.bot.getFile(update.message.video.file_id)
                titlemp4 = ("{0}.mp4").format(chat_id)
                titlegif = ("{0}.gif").format(chat_id)
                file.download(titlemp4)
                ff = FFmpeg(inputs={titlemp4: None}, outputs={titlegif: '-vf scale=1280:720'})
                ff.run()
                context.bot.send_animation(chat_id, open(titlegif, 'rb'))
                self._mafina.UseCommand.pop(chat_id)
                self.DeletePath(titlemp4)
                self.DeletePath(titlegif)
        else:
            context.bot.send_message(chat_id, answer["36"])
            self._mafina.UseCommand[chat_id] = "ConfirmSendVideo"

    @classmethod
    def question(self, update, context, answer):
        r = random.randint(0, 100)
        state_sys_answer = self._mafina._DB.GetAnswerSystem(update.message.chat.id)
        if state_sys_answer == True:
            if (r <= 10):
                context.bot.send_message(update.message.chat_id, answer["16"])
            elif (r <= 20):
                context.bot.send_message(update.message.chat_id, answer["17"])
            elif (r <= 30):
                context.bot.send_message(update.message.chat_id, answer["18"])
            elif (r <= 40):
                context.bot.send_message(update.message.chat_id, answer["19"])
            elif (r <= 50):
                context.bot.send_message(update.message.chat_id, answer["20"])
            elif (r <= 60):
                context.bot.send_message(update.message.chat_id, answer["21"])
            elif (r <= 70):
                context.bot.send_message(update.message.chat_id, answer["22"])
            elif (r <= 80):
                context.bot.send_message(update.message.chat_id, answer["23"])
            elif (r <= 90):
                context.bot.send_message(update.message.chat_id, answer["24"])
            elif (r <= 100):
                context.bot.send_message(update.message.chat_id, answer["25"])
    @classmethod
    def Answers(self, update, context, chat_id):
        insert = True
        cursor = self._mafina._DB.GetAnswers(chat_id)
        answers = ()
        for x in cursor:
            answers = answers + x
            for y in range(len(x)):
                if x[y]==update.message.text:
                    insert = False
                    break

        if(insert) and len(str(update.message.text.split))>1: self._mafina._DB.InsertNewAnswer(update.message.text, chat_id)
        if 'IMafinabot' in str(update): context.bot.send_message(chat_id, self.CreateAnswer(answers))

    @staticmethod
    def CreateAnswer(answers):
        merge = random.randint(3, 7)
        text = ""
        for x in range(merge):
            pos =random.randrange(len(answers))
            res_split = answers[pos].split()
            print(res_split)
            pos_word=random.randrange(len(res_split))
            if pos_word>0:pos_word-=1
            if res_split[pos_word] in text:pass
            else:text += " " + res_split[pos_word]
            print(pos_word)
            print(len(res_split))
            for y in range(3):
                if pos_word<len(res_split)-1:
                    pos_word+=1
                    if res_split[pos_word] in text:
                        pass
                    else:
                        text += " "+res_split[pos_word]
                else:break
        return text


    @staticmethod
    def DeletePath(file):
        os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), file))

    @staticmethod
    def dec(s):
        return base64.b64decode(s)