import re, math, Thread, requests, os
import time
from decimal import Decimal as D
from gate_api import ApiClient, Configuration, Order, SpotApi

class Hunter:
	_instance, _mafina = None, None
	Purchased = False
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
				Hunter.LastListing = hunter._DB.GetUsername(self.chat_id).split("|")[0
			while True:
				time.sleep(9)
				try:
					if self.Purchased:
						Thread.Thread(self.SellCrypto, ())
						self.CheckListing(hunter, bot)
					else:
						Thread.Thread(self.CheckListing, (hunter, bot))
				except Exception:
					time.sleep(3)
					Thread.Thread(self.HunterListing(), ())
		except Exception:
			time.sleep(3)
			Thread.Thread(self.HunterListing(), ())

	def CheckListing(self, hunter, bot):
		try:
			if self.chat_id in hunter.UseCommand.keys():
				if hunter.UseCommand[self.chat_id] == "NewListing":
					bot.send_message(self.chat_id, self.LastListing)
					return 0
			latest_announcement = requests.get(
				"https://www.binance.com/bapi/composite/v1/public/cms/article/catalog/list/query?catalogId=48&pageNo=1&pageSize=15&rnd=" + str(
					time.time())).json()
			UpdateListing = latest_announcement['data']['articles'][0]['title']
			print(UpdateListing+ " " + time.strftime("%H:%M:%S", time.localtime()))
			if "binance will list" in UpdateListing.lower():
				if self.LastListing != UpdateListing:
					print("Check")
					self.BuyingNewCrypto(UpdateListing)
					Hunter._instance._mafina.UseCommand[self.chat_id] = "NewListing"
					self.LastListing = UpdateListing
					bot.send_message(self.chat_id, self.LastListing)
					hunter._DB.UpdateListing(self.chat_id, UpdateListing+"|" + time.strftime("%H:%M:%S", time.localtime()))

		except Exception:
			time.sleep(2)


	def BuyingNewCrypto(self, UpdateListing):
		self.Name_crypto = re.search(r"\(([A-Za-z0-9_]+)\)", UpdateListing).group(1)
		self.currency_pair = self.Name_crypto + "_USDT"
		self.config = Configuration(key=os.getenv('Gate_key'), secret=os.getenv('Gate_secret'))
		self.spot_api = SpotApi(ApiClient(self.config))
		self.tickers = self.spot_api.list_tickers(currency_pair=self.currency_pair)
		last_price = float(self.tickers[0].last)
		self.accounts = self.spot_api.list_spot_accounts(currency="USDT")
		available = float(D(self.accounts[0].available))
		self.price_buying = last_price + last_price / 100 * (10)
		amount_order = available / self.price_buying
		amount_order = math.floor(amount_order * 10) / 10
		print(amount_order)
		print(available)
		print(str(self.price_buying))
		order = Order(amount=str(amount_order), price=str(self.price_buying), side='buy', currency_pair=self.currency_pair)
		self.created_buy = self.spot_api.create_order(order)
		print(self.created_buy.status)
		if str(self.created_buy.status) == "closed":
			self.Purchased = True



	def SellCrypto(self):
		sell_price = self.price_buying + self.price_buying / 100 * (80)
		if str(self.created_buy.status) == "closed":
			last_price = float(self.tickers[0].last)
			print(last_price)
			print(sell_price)
			if sell_price <= float(self.tickers[0].last):
				available = self.spot_api.list_spot_accounts(currency=self.Name_crypto)[0].available
				last_price = last_price + last_price / 100 * (-5)
				order = Order(amount=str(available), price=str(last_price), side='sell',
							  currency_pair=self.currency_pair)
				self.created_sell = self.spot_api.create_order(order)
				if (self.created_sell.status == "closed"):
					self.Purchased = False
