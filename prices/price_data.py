from datetime import datetime


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

	def __init__(self, time, price=None, index = None):
		self.time = time
		self.prices = []
		if price is not None:
			for i in range(0, index):
				self.prices.append("None")
			self.prices.append(price)


	def addPrice(self, price):
		self.prices.append(price)

	"""
	Return a list of comma-seperated values
	of all the prices at the current time
	"""
	def output_prices(self):
		x = str(self.time) + ","
		for i in self.prices:
			x += i
			x += ","
		return x[:-1]

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
		self.times = []

	def print_to_file(self, filename):
		output_file = file(filename, 'w+')
		output_str = "Date,"
		for i in self.currList:
			output_str += i
			output_str += ','
			output_file.write(output_str[:-1])
		output_file.write('\n')
		for i in self.times:
			output_file.write(i.output_prices())
			output_file.write('\n')

	def add_currency(self, curr_name, filename):
		curr_index = -1
		if self.currList.count(curr_name) is 1:
			curr_index = self.currList.index(curr_name)
		elif self.currList.count(curr_name) is 0: #going to be this one unless a currency is added twice
			self.currList.append(curr_name)
			curr_index = self.currList.index(curr_name)
		else:
			print "Error: currency found more than once in list!"
			return

		currency_data = file(filename)

		#each line of data in the file
		for line in currency_data:
			data = line.split("|")
			time = datetime.strptime(data[0][:-3], '%Y-%m-%d %H:%M')
			price = data[3]
			#check to see if time already exists in the PriceDatabase
			found = False
			for i in self.times:
				if i.time == time: #add price to this time
					i.prices.append(price)
					found = True
					break
			if not found:
				self.times.append(Date(time, price, curr_index))

		#add None to all times not added with this currency
		for i in self.times:
			if len(i.prices) < curr_index + 1:
				i.addPrice("None")

	def currency_index(self, curr_name):
		if self.currList.count(curr_name) is 1:
			return self.currList.index(curr_name)
		else:
			return -1



def main():
	data = PriceDatabase()
	data.add_currency("BTC", "full-data/bitcoin.txt")
	data.add_currency("ETH", "full-data/ethereum.txt")
	data.print_to_file("output.csv")

if __name__ == '__main__':
	main()
