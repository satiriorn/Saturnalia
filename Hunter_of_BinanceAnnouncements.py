from requests import get
from bs4 import BeautifulSoup
import telegram.ext, os, re

from gate_api import ApiClient, Configuration, Order, SpotApi

class Hunter:
	_instance, _mafina = None, None
	NewListing = ""
	chat_id = "-506807179"
	Currency = "_USDT"
	def __new__(cls, M):
		if not hasattr(cls, '_inst'):
			Hunter._instance = super(Hunter, cls).__new__(cls)
			Hunter._mafina = M
			return Hunter._instance

	@classmethod
	def StartHunter(self):
		self._mafina.jobchat[self.chat_id] = self._mafina.job.run_repeating(self.CheckListingJob, interval=30, first=0, context=self.chat_id)

	@staticmethod
	def CheckListingJob(context: telegram.ext.CallbackContext):
		hunter = Hunter._instance._mafina
		UpdateListing = Hunter.getLatestNews()[0]
		LastListing = hunter._DB.GetUsername(context.job.context)
		if context.job.context in hunter.UseCommand.keys():
			if hunter.UseCommand[context.job.context] == "NewListing":
				for x in range(3):
					context.bot.send_message(context.job.context, Hunter.NewListing)
		else:
			if "binance will list" in UpdateListing.lower():
				if LastListing != UpdateListing:
					print(UpdateListing)
					Hunter.NewListing = UpdateListing
					Hunter._instance._mafina.UseCommand[context.job.context] = "NewListing"
					hunter._DB.UpdateListing(context.job.context, UpdateListing)
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
		config = Configuration(key=os.getenv('Gate_Key'), secret=os.getenv('Gate_secret'))
		spot_api = SpotApi(ApiClient(config))
		pair = spot_api.get_currency_pair(currency_pair)
