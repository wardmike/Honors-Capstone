
"""
PricePoint contains a price for one cryptocurrency
at one point in time.
Ex: Bitcoin's price on November 9 at 8:05am
"""
class PricePoint(object):

	def __init__(self):
		self.price = None

	def appPrice(self, price):
		self.price = price

"""
Date contains all the prices of all supported
cryptocurrencies at one point in time.
Ex: Prices of Bitcoin, Ethereum, and Litecoin
on November 9 at 8:05am.
"""
class Date(object):

	def __init__(self, date):
		self.date = date
		self.prices = []

	def addPrice(price):
		self.prices.append(price)

"""
PriceDatabase includes all the prices of all
supported cryptocurrencies for all supported
times.
Ex: Prices of Bitcoin, Ethereum, and Litecoin
from August 1 to November 9, with data points
every 5 minutes.
self.currList contains all supported cryptocurrencies
in the same order the prices will appear in the
self.prices list of each Date object.
self.dates contains all the Date objects.
"""
class PriceDatabase(object):

	def __init__(self):
		self.currList = []
		self.dates = []

	def addCurrency(self, currency):
		self.currList.append(currency)


