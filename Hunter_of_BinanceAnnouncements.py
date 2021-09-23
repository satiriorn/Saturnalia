from requests import get
from bs4 import BeautifulSoup
import telegram.ext, os, re
from decimal import Decimal as D
from gate_api import ApiClient, Configuration, Order, SpotApi

class Hunter:
	_instance, _mafina = None, None
	NewListing = "Binance will list (TRX)"
	chat_id = "-506807179"
	Currency = "_USDT"
	def __new__(cls, M):
		if not hasattr(cls, '_inst'):
			Hunter._instance = super(Hunter, cls).__new__(cls)
			Hunter._mafina = M
			return Hunter._instance

	@classmethod
	def StartHunter(self):
		self._mafina.jobchat[self.chat_id] = self._mafina.job.run_repeating(self.CheckListingJob, interval=10, first=0, context=self.chat_id)

	@staticmethod
	def CheckListingJob(context: telegram.ext.CallbackContext):
		hunter = Hunter._instance._mafina
		UpdateListing = Hunter.getLatestNews()[0]
		LastListing = hunter._DB.GetUsername(context.job.context)
		if context.job.context in hunter.UseCommand.keys():
			if hunter.UseCommand[context.job.context] == "NewListing":
				for x in range(3):
					context.bot.send_message(context.job.context, Hunter.NewListing)
					#Hunter.BuyingNewCrypto()
		else:
			if "binance will list" in UpdateListing.lower():
				if LastListing != UpdateListing:
					print(UpdateListing)
					Hunter.NewListing = UpdateListing
					Hunter._instance._mafina.UseCommand[context.job.context] = "NewListing"
					hunter._DB.UpdateListing(context.job.context, UpdateListing)
					Hunter.BuyingNewCrypto()
					for x in range(3):
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
		last_price = tickers[0].last
		accounts = spot_api.list_spot_accounts(currency="USDT")
		available = D(accounts[0].available)
		amount_order = float(available)/float(last_price)
		order = Order(amount=str(amount_order), price=last_price, side='buy', currency_pair=currency_pair)
		created = spot_api.create_order(order)
		print(created.status)