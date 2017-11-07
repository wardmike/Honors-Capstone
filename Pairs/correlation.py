import numpy as np


def importPrices(filename):
	fl = open(filename)
	prices = []
	for line in fl:
		prices.append(float(line))
	return prices

def importPrices_full_data(filename):
	fl = open(filename)
	prices = []
	for line in fl:
		prices.append(float(line.split("|")[3]))
	return prices

class Find_Correlation(object):

	def __init__(self):
		self.currencies = []

	def addCurrency(self, curr_name, full_data):
		self.currencies.append(Currency(curr_name, full_data))

	def printPairs(self):
		for i in range(0, len(self.currencies)):
			for j in range(i+1, len(self.currencies)):
				print self.currencies[i].name + " and " + self.currencies[j].name + ":"
				print findPair(self.currencies[i], self.currencies[j])


def findPair(curr1, curr2):
	if curr1.name != curr2.name:
		smallest_size = curr1.len if curr1.len < curr2.len else curr2.len
		return np.corrcoef(curr1.prices[curr1.len - smallest_size:], curr2.prices[curr2.len - smallest_size:])[1, 0]


class Currency(object):
	def __init__(self, name, full_data = False):
		self.name = name
		if full_data:
			self.prices = importPrices_full_data("../prices/full-data/" + name + ".txt")
		else:
			self.prices = importPrices("../prices/txt/" + name + ".txt")
		self.len = len(self.prices)


def main():
	finder = Find_Correlation()
	finder.addCurrency("BTC")
	finder.addCurrency("ETH")
	finder.addCurrency("BCH")
	finder.addCurrency("LTC")
	finder.addCurrency("NEO")
	finder.addCurrency("XEM")
	finder.addCurrency("XMR")
	finder.addCurrency("XRP")
	finder.addCurrency("DASH")
	#finder.printPairs()

	# finder2 - prices every 5 minutes from 05 October to 03 November
	finder2 = Find_Correlation()
	finder2.addCurrency("bitcoin")
	finder2.addCurrency("ethereum")
	finder2.addCurrency("bitcoin-cash")
	finder2.printPairs()

if __name__ == '__main__':
	main()