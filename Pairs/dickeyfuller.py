import numpy as np


def importPrices(filename):
	fl = open(filename)
	prices = []
	for line in fl:
		prices.append(float(line))
	return prices

class PairsTrader(object):

	def __init__(self):
		self.currencies = []

	def addCurrency(self, curr_name):
		self.currencies.append(Currency(curr_name))

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
	def __init__(self, name):
		self.name = name
		self.prices = importPrices("../prices/" + name + ".txt")
		self.len = len(self.prices)


def main():
	trader = PairsTrader()
	trader.addCurrency("BTC")
	trader.addCurrency("ETH")
	trader.addCurrency("BCH")
	trader.printPairs()

if __name__ == '__main__':
	main()