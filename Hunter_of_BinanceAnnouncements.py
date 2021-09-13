from requests import get
from bs4 import BeautifulSoup
import telegram.ext

class Hunter:
	_instance, _mafina = None, None
	NewListing = ""
	chat_id = "-506807179"
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
		UpdateListing = Hunter.getLatestNews()[0]
		LastListing = Hunter._instance._mafina._DB.GetUsername(context.job.context)
		if "binance will list" in UpdateListing.lower():
			if (LastListing!=UpdateListing):
				print(UpdateListing)
				Hunter.NewListing = UpdateListing
				Hunter._instance._mafina.UseCommand[context.job.context] = "NewListing"

	@staticmethod
	def AttentionJob(context: telegram.ext.CallbackContext):
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