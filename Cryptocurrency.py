import os
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
    def Add_Pair(self, update, context, answer, lang, chat_id):
        if chat_id in self._mafina.UseCommand.keys():
            if self._mafina.UseCommand[chat_id] == "GetPair":
                price = self._instance.client.get_symbol_ticker(symbol=update.message.text)
                context.bot.send_message(chat_id, price['symbol']+ " "+ price['price'])
                self._mafina._DB.InsertCrypto(price['symbol'], chat_id, price['price'])
        else:
            context.bot.edit_message_text(chat_id=chat_id, text=answer["71"], message_id=update.callback_query.message.message_id)
            self._mafina.UseCommand[chat_id] = "GetPair"

    def Delete_Pair(self):
        pass

#api_key = os.getenv('Binance_key')
#api_secret = os.getenv('Binance_secret')
#client = Client(api_key, api_secret)
#btc_price = client.get_symbol_ticker(symbol="XEMUSDT")
#print(client)
#print(btc_price)
#timestamp = client._get_earliest_valid_timestamp('XEMUSDT', '1d')
#print(timestamp)
#bars = client.get_historical_klines('XEMUSDT', '1d', timestamp, limit=1000)
#print(bars)