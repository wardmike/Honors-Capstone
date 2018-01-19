class MovingAverageCrossoverTrader:
    def __init__(self, name, mva, debug, filename):
        self.mva_days = mva
        self.buy = 0.0
        self.profit = 0.0
        self.cash = 1000.00
        self.debug = debug
        self.prices = []
        file_prices = open(filename, 'r')
        lines = file_prices.read().splitlines()
        for line in lines:
            vals = line.split("|")
            self.prices.append(float(vals[3]))

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
                        print("day ", days, ", we bought at price: ", price)
                    buy = price
                elif (price < average and buy != 0.0): #predicting drop in price
                    if self.debug:
                        print("day ", days, ", we sold at price: ", price)
                        print("Profit for this trade: ", price - buy)
                    self.profit += price - buy
                    buy = 0.0
            days += 1

    def get_profit(self):
        return self.profit

    def results(self):
        result = "total profit: " + str(self.profit) + "\nreturns (algorithm): " + str(self.profit/self.prices[0] * 100) + "%\n"
        return result
        #print "returns (buy and hold): ", self.prices[-1]/self.prices[0] * 100, "%"

def test_currency(currency, filename):
    print(currency)
    best_profit = 0
    best_mva = 0
    fl = open(filename)
    prcs = []
    for line in fl:
        vals = line.split("|")
        prcs.append(float(vals[3]))
    for x in range(2, 240): #range changes depending on daily or 5-minutes
        trader = MovingAverageCrossoverTrader(currency, x, False, filename)
        trader.trade()
        trader.print_results()
        if trader.get_profit() > best_profit:
            best_profit = trader.get_profit()
            best_mva = x
    print("best profit: ", best_profit)
    print("best mva: ", best_mva)
    print("returns (buy and hold): ", prcs[-1]/prcs[0] * 100, "%")
    print("returns (algorithm): ", best_profit/prcs[0] * 100, "%")


def main():
    '''
    test_currency("BTC", "prices/txt/BTC.txt")
    test_currency("ETH", "prices/txt/ETH.txt")
    test_currency("BCH", "prices/txt/BCH.txt")
    test_currency("DASH", "prices/txt/DASH.txt")
    test_currency("LTC", "prices/txt/LTC.txt")
    test_currency("NEO", "prices/txt/NEO.txt")
    test_currency("XEM", "prices/txt/XEM.txt")
    test_currency("XMR", "prices/txt/XMR.txt")
    test_currency("XRP", "prices/txt/XRP.txt")
    '''
    test_currency("BTC", "../prices/5-minute-just-prices/bitcoin.txt")


if __name__ == "__main__":
    main()