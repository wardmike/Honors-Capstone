class MeanReversionTrader:
    def __init__(self, currency, mva, margin, debug, start_cash, filename):
        self.mva_days = mva
        self.start_cash = float(start_cash) #setting to float to prevent integer division
        self.cash = float(start_cash)
        self.shares = 0
        self.debug = debug
        ### array for holding prices
        self.prices = []
        self.line_algo = []
        self.line_curr_1 = []
        self.line_curr_2 = []
        self.line_avg = []
        self.line_upper = []
        self.line_lower = []
        self.line_hold = []
        self.upper = 1 + (float(margin) / float(100))
        self.lower = 1 - (float(margin) / float(100))
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

    def price_difference(self, i):
        return self.prices_higher[i] - self.prices_lower[i]

    def trade(self):
        days = 0
        #simulating buying right away
        self.shares = float(self.cash) / float(self.prices[0])
        self.cash = 0.0
        for i in range(0, len(self.prices)):
            ### find difference and add to line_diff
            price = self.prices[i]
            if (days > self.mva_days): #only if we're far enough along to use mva
                ### find average
                average = self.find_average(days)
                self.line_avg.append(average)
                ### find upper bound: 105%
                upper_val = average * self.upper
                self.line_upper.append(upper_val)
                ### find lower bound: 95%
                lower_val = average * self.lower
                self.line_lower.append(lower_val)
                ### see if diff has crossed either line
                if (price > upper_val and self.cash > 0): #cross above upper line; buy
                    #sell lower and buy higher
                    if self.debug:
                        print("day ", days, ", we bought at ", price)
                    ### buy
                    self.shares = self.cash / price
                    self.cash = 0
                elif (price < lower_val and self.shares > 0): #cross below lower line; sell
                    #sell higher and buy lower
                    if self.debug:
                        print("day ", days, ", we sold at ", price)
                    ### sell
                    self.cash = self.shares * price
                    self.shares = 0
            self.line_algo.append(self.cash + (self.shares * price))
            self.line_hold.append(self.initial_hold * price)
            days += 1
        #sell at the end
        self.cash += self.shares * self.prices[-1]
        self.shares = 0.0

    def get_line_avg(self):
        return self.line_avg

    def get_line_price(self):
        return self.prices

    def get_line_upper(self):
        return self.line_upper

    def get_line_lower(self):
        return self.line_lower

    def get_line_hold(self):
        return self.line_hold

    def get_line_algo(self):
        return self.line_algo

    def get_profit(self):
        return self.cash - self.start_cash

    #def results(self):
    #    returns_algo = float(self.get_profit()) / float(self.prices[0]) * 100
    #    returns_buy_hold = ((self.start_cash * (self.prices[-1]/self.prices[0])) - self.start_cash)/self.start_cash * 100
    #    #need to split this between lines
    #    result = "total profit: " + str(self.get_profit()) + "\nreturns (algorithm): " + str(returns_algo) + "%\nreturns (buy and hold): " + str(returns_buy_hold) + "%\n"
    #    return result
    #    #print "returns (buy and hold): ", self.prices[-1]/self.prices[0] * 100, "%"

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