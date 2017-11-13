class MovingAverageCrossoverTrader(object):
    def __init__(self, name, mva, debug):
        self.mva_days = mva
        self.buy = 0.0
        self.profit = 0.0
        self.cash = 1000.00
        self.debug = debug
        self.prices = []
        filename = "prices/txt/" + name + ".txt"
        file_prices = open(filename, 'r')
        lines = file_prices.read().splitlines()
        for line in lines:
            self.prices.append(float(line))

    def find_average(self, day):
        avg = 0.0
        for x in range(0, self.mva_days):
            avg += self.prices[day - x]
        return avg/self.mva_days

    def trade(self):
        days = 0
        buy = self.prices[0]
        for price in self.prices:
            if (days > self.mva_days):
                average = self.find_average(days)
                if (price > average and buy==0.0): #predicting increase in price
                    if self.debug:
                        print "day ", days, ", we bought at price: ", price
                    buy = price
                elif (price < average and buy != 0.0): #predicting drop in price
                    if self.debug:
                        print "day ", days, ", we sold at price: ", price
                        print "Profit for this trade: ", price - buy
                    self.profit += price - buy
                    buy = 0.0
            days += 1

    def get_profit(self):
        return self.profit

    def print_results(self):
        print "total profit: ", self.profit
        print "returns (algorithm): ", self.profit/self.prices[0] * 100, "%"
        print "returns (buy and hold): ", self.prices[-1]/self.prices[0] * 100, "%"

def test_currency(currency):
    print currency
    best_profit = 0
    best_mva = 0
    for x in range(2, 15):
        trader = MovingAverageCrossoverTrader(currency, x, False)
        trader.trade()
        #trader.print_results()
        if trader.get_profit() > best_profit:
            best_profit = trader.get_profit()
            best_mva = x
    print "best profit: ", best_profit
    print "best mva: ", best_mva


def main():
    test_currency("BTC")
    test_currency("ETH")
    test_currency("BCH")
    test_currency("DASH")
    test_currency("LTC")
    test_currency("NEO")
    test_currency("XEM")
    test_currency("XMR")
    test_currency("XRP")


if __name__ == "__main__":
    main()