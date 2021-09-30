from requests import get
from bs4 import BeautifulSoup
import telegram.ext, os, re
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

	@classmethod
	def StartHunter(self):
		self._mafina.jobchat[self.chat_id] = self._mafina.job.run_repeating(self.CheckListingJob, interval=1, first=0, context=self.chat_id)

	@staticmethod
	def CheckListingJob(context: telegram.ext.CallbackContext):
		hunter = Hunter._instance._mafina
		UpdateListing = Hunter.getLatestNews()[0]
		if Hunter.LastListing == "":
			Hunter.LastListing = hunter._DB.GetUsername(context.job.context)
		if context.job.context in hunter.UseCommand.keys():
			if hunter.UseCommand[context.job.context] == "NewListing":
				context.bot.send_message(context.job.context, Hunter.NewListing)
		else:
			if "binance will list" in UpdateListing.lower():
				if Hunter.LastListing != UpdateListing:
					print(UpdateListing)
					Hunter.BuyingNewCrypto()
					Hunter.NewListing = UpdateListing
					Hunter._instance._mafina.UseCommand[context.job.context] = "NewListing"
					hunter._DB.UpdateListing(context.job.context, UpdateListing)
					Hunter.LastListing = UpdateListing
					context.bot.send_message(context.job.context, Hunter.NewListing)

	@staticmethod
	def getLatestNews(url = "https://www.binance.com/en/support/announcement/c-48"):
		newList = []
		text = get(url).text
		html = BeautifulSoup(text, 'html.parser')
		a = html.find_all("a", {'class': 'css-1ej4hfo'})
		for ann in a:
			newList.append(ann.text)
		return newList

	@staticmethod
	def BuyingNewCrypto():
		Name_crypto = re.search(r"\(([A-Za-z0-9_]+)\)", Hunter.NewListing)
		currency_pair = str(Name_crypto.group(1)) + "_USDT"
		config = Configuration(key=os.getenv('Gate_key'), secret=os.getenv('Gate_secret'))
		spot_api = SpotApi(ApiClient(config))
		tickers = spot_api.list_tickers(currency_pair=currency_pair)
		last_price = float(tickers[0].last)
		accounts = spot_api.list_spot_accounts(currency="USDT")
		available = float(D(accounts[0].available))
		amount_order = available/last_price
		price_buying = last_price+last_price/100*(10)
		order = Order(amount=str(amount_order), price=str(price_buying), side='buy', currency_pair=currency_pair)
		created = spot_api.create_order(order)
		print(created.status)