class SimpleMovingAverageCrossoverTrader:
    def __init__(self, name, mva, debug, start_cash, filename):
        self.mva_days = mva
        self.buy = 0.0
        self.start_cash = float(start_cash) #setting to float to prevent integer division
        self.cash = float(start_cash) #setting to float ot prevent integer division
        self.shares = float(0) #setting to float ot prevent integer division
        self.debug = debug
        self.prices = []
        self.algo_line = []
        self.hold_line = []
        self.mva_line = []
        file_prices = open(filename, 'r')
        lines = file_prices.read().splitlines()
        for line in lines:
            vals = line.split("|")
            self.prices.append(float(vals[3]))
        self.initial_hold = float(start_cash) / float(self.prices[0])

    def find_average(self, day):
        avg = 0.0
        for x in range(0, self.mva_days):
            avg += self.prices[day - x]
        return avg/self.mva_days

    def trade(self):
        days = 0
        #simulating buying right away
        self.shares = self.cash / self.prices[0]
        self.cash = 0.0
        for price in self.prices:
            if (days > self.mva_days):
                average = self.find_average(days)
                self.mva_line.append(average)
                if (price > average and self.shares==0.0): #predicting increase in price
                    if self.debug:
                        print("day ", days, ", we bought at price: ", price)
                    #buying shares
                    self.shares = self.cash / float(price)
                    self.cash = 0.0
                elif (price < average and self.shares != 0.0): #predicting drop in price
                    if self.debug:
                        print("day ", days, ", we sold at price: ", price)
                    #selling shares
                    self.cash = self.shares * float(price)
                    self.shares = 0.0
            self.algo_line.append(self.cash + (self.shares * price))
            self.hold_line.append(price * self.initial_hold)
            days += 1
        #sell at the end
        self.cash += self.shares * self.prices[-1]
        self.shares = 0.0

    def get_mva_line(self):
        return self.mva_line

    def get_price_line(self):
        return self.prices

    def get_hold_line(self):
        return self.hold_line

    def get_algo_line(self):
        return self.algo_line

    def get_profit(self):
        return self.cash - self.start_cash

    def results(self):
        returns_algo = float(self.get_profit()) / float(self.prices[0]) * 100
        returns_buy_hold = ((self.start_cash * (self.prices[-1]/self.prices[0])) - self.start_cash)/self.start_cash * 100
        #need to split this between lines
        result = "total profit: " + str(self.get_profit()) + "\nreturns (algorithm): " + str(returns_algo) + "%\nreturns (buy and hold): " + str(returns_buy_hold) + "%\n"
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
        trader = MovingAverageCrossoverTrader(currency, x, False, 1000, filename)
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