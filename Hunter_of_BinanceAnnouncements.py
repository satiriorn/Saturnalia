import telegram.ext, os, re, math, Thread, requests
import time
from decimal import Decimal as D
from gate_api import ApiClient, Configuration, Order, SpotApi

class Hunter:
	_instance, _mafina = None, None
	NewListing = ""
	chat_id = "-506807179"
	Currency = "_USDT"
	LastListing = ""
	def __new__(cls, M):
		if not hasattr(cls, '_inst'):
			Hunter._instance = super(Hunter, cls).__new__(cls)
			Hunter._mafina = M
			return Hunter._instance

	def HunterListing(self):
		try:
			hunter = Hunter._instance._mafina
			bot = Hunter._instance._mafina.updater.dispatcher.bot
			if Hunter.LastListing == "":
				Hunter.LastListing = hunter._DB.GetUsername(self.chat_id)
			while True:
				time.sleep(3)
				try:
					Thread.Thread(self.CheckListing, (hunter, bot))
				except Exception:
					time.sleep(1)
					Thread.Thread(self.HunterListing(), ())
		except Exception:
			time.sleep(3)
			Thread.Thread(self.HunterListing(), ())

	def CheckListing(self, hunter, bot):
		try:
			while True:
				if self.chat_id in hunter.UseCommand.keys():
					if hunter.UseCommand[self.chat_id] == "NewListing":
						bot.send_messages(self.chat_id, Hunter.NewListing)
				time.sleep(2)
				latest_announcement = requests.get(
					"https://www.binance.com/bapi/composite/v1/public/cms/article/catalog/list/query?catalogId=48&pageNo=1&pageSize=15&rnd=" + str(
						time.time())).json()
				UpdateListing = latest_announcement['data']['articles'][0]['title'] + " " + time.strftime("%H:%M:%S",
																										  time.localtime())
				print(UpdateListing)
				if "binance will list" in UpdateListing.lower():
					if self.LastListing != UpdateListing:
						Hunter._instance._mafina.UseCommand[self.chat_id] = "NewListing"
						hunter._DB.UpdateListing(self.chat_id, UpdateListing)
						self.LastListing = UpdateListing
						bot.send_message(self.chat_id, Hunter.NewListing)
		except Exception:
			time.sleep(2)
			self.CheckListing(hunter, bot)
	"""

	@staticmethod
	def BuyingNewCrypto():
		Name_crypto = re.search(r"\(([A-Za-z0-9_]+)\)", Hunter.NewListing).group(1)
		currency_pair = Name_crypto + "_USDT"
		config = Configuration(key=os.getenv('Gate_key'), secret=os.getenv('Gate_secret'))
		spot_api = SpotApi(ApiClient(config))
		tickers = spot_api.list_tickers(currency_pair=currency_pair)
		last_price = float(tickers[0].last)
		accounts = spot_api.list_spot_accounts(currency="USDT")
		available = float(D(accounts[0].available))
		price_buying = last_price + last_price / 100 * (10)
		amount_order = available/price_buying
		amount_order = math.floor(amount_order * 10) / 10
		print(amount_order)
		print(available)
		print(str(price_buying))
		order = Order(amount=str(amount_order), price=str(price_buying), side='buy', currency_pair=currency_pair)
		created = spot_api.create_order(order)
		print(created.status)
	"""