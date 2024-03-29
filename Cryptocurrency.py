import os, telegram.ext
from binance.client import Client

class Binance:
    _instance, _mafina = None, None
    def __new__(cls, M):
        api_key = os.getenv('Binance_key')
        api_secret = os.getenv('Binance_secret')
        cls.client = Client(api_key, api_secret)
        if not hasattr(cls, '_inst'):
            Binance._instance = super(Binance, cls).__new__(cls)
            Binance._mafina = M
            return Binance._instance

    @classmethod
    def Menu_Binance(self,  update, context, answer, lang):
        context.bot.send_message(update.message.chat_id, answer["39"],
                                 reply_markup=self._mafina._keyboard.InlineKeyboard(self._mafina._keyboard.MenuBinanceKeyboard[lang], False))

    @classmethod
    def Add_Pair(self, update, context, answer, chat_id):
        if chat_id in self._mafina.UseCommand.keys():
            if self._mafina.UseCommand[chat_id] == "GetPair":
                price = self._instance.client.get_symbol_ticker(symbol=update.message.text.upper())
                context.bot.send_message(chat_id, answer["73"].format(price['symbol']+ " "+ price['price']))
                if(self._mafina._DB.InsertCrypto(price['symbol'], chat_id, price['price'])):
                    context.bot.send_message(chat_id, answer["72"])
                else:
                    self._mafina.UseCommand.pop(chat_id)
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["71"], message_id=update.callback_query.message.message_id)
            self._mafina.UseCommand[chat_id] = "GetPair"

    @classmethod
    def Delete_Pair(self, update, context, answer, chat_id):
        if chat_id in self._mafina.UseCommand.keys():
            if self._mafina.UseCommand[chat_id] == "DeletePair":
                self._mafina._DB.DeleteCryptoPair(chat_id, update.callback_query.data)
                context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                              message_id=update.callback_query.message.message_id)
                self._mafina.UseCommand.pop(chat_id)
        else:
            result=self._mafina._DB.GetCryptoPairUser(chat_id, True)
            context.bot.edit_message_text(chat_id=chat_id, text=answer["74"], message_id=update.callback_query.message.message_id)
            context.bot.edit_message_reply_markup(chat_id,
                                                  reply_markup=self._mafina._keyboard.InlineKeyboard(result, False),
                                                  message_id=update.callback_query.message.message_id)
            self._mafina.UseCommand[chat_id] = "DeletePair"

    @classmethod
    def Display_selected_pairs(self, update, context, answer, chat_id):
        res = self._mafina._DB.GetCryptoPairUser(chat_id, True)
        x = 0
        result = ""
        while x < len(res):
            bn = self._instance.client.get_symbol_ticker(symbol=res[x])
            result += bn['symbol']+" "+bn['price']+"\n"
            x+=1
        context.bot.edit_message_text(chat_id=chat_id, text=answer["75"].format(result),  message_id=update.callback_query.message.message_id)

    def Start_Crypto_job(self):
        cursor = self._mafina._DB.GetAllCryptoUsers()
        for x in cursor:
            for y in range(len(x)):
                data = (x[y], self)
                self._mafina.jobchat[str(x[y])]=self._mafina.job.run_repeating(self.Notification, interval=350, first=0, context=data)

    @staticmethod
    def Notification(context: telegram.ext.CallbackContext):
        db = context.job.context[1]._mafina._DB
        chat_id = context.job.context[0]
        result = db.GetCryptoPairUser(chat_id)
        x = 0
        while x < len(result):
            binance_result = context.job.context[1]._instance.client.get_symbol_ticker(symbol=result[x])
            CurrentPrice = float(binance_result['price'])
            LastPrice = float(result[x+2])
            percentage = (CurrentPrice-LastPrice)*100/LastPrice
            percentage = round(percentage, 1)
            if(int(percentage)>=5):
                context.bot.send_message(chat_id, "Rose up {0}% ".format(percentage)+str(binance_result['symbol'])+" "+ str(CurrentPrice))
                db.UpdateCryptoPair(chat_id, binance_result)
            elif(int(percentage)<=-5):
                context.bot.send_message(chat_id, "Fell by {0}% ".format(percentage) + str(binance_result['symbol']) + " " + str(CurrentPrice))
                db.UpdateCryptoPair(chat_id, binance_result)
            x+=3
