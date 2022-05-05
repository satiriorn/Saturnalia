"""
from easyocr import Reader
import os

class OCR:
   _instance, _mafina = None, None

   def __new__(cls, M):
      if not hasattr(cls, '_inst'):
         OCR._instance = super(OCR, cls).__new__(cls)
         OCR._mafina = M
         return OCR._instance

   def readText(self, update, context, answer, chat_id, lang):
      title = ""
      try:
         if chat_id in self._mafina.UseCommand.keys():
            if self._mafina.UseCommand[chat_id] == "WaitLangForTextDetect":
               context.bot.edit_message_text(chat_id=chat_id, text=answer["78"],
                                             message_id=update.callback_query.message.message_id)
               self.reader = Reader([self._mafina._keyboard.b[update.callback_query.data]])
               self._mafina.UseCommand.pop(chat_id)
               self._mafina.UseCommand[chat_id] = "WaitPhoto"
            elif self._mafina.UseCommand[chat_id] == "WaitPhoto":
               try:
                  file_id = update['message']['photo'][-1]['file_id']
               except Exception:
                  file_id = update.message.document.file_id
               file = context.bot.getFile(file_id)
               title = "{0}.jpg".format(chat_id)
               file.download(title)
               text = self.reader.readtext(title, detail=0, paragraph=True)
               print('\n'.join(text))
               context.bot.send_message(chat_id, '\n'.join(text))
               self._mafina.UseCommand.pop(chat_id)
               os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), title))
         else:
            context.bot.send_message(update.message.chat_id, answer["79"],
                                     reply_markup=self._mafina._keyboard.InlineKeyboard(
                                        self._mafina._keyboard.TranslateKeyboard, False))
            self._mafina.UseCommand[chat_id] = "WaitLangForTextDetect"
      except Exception:
         self._mafina.UseCommand.pop(chat_id)
         os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), title))
"""

