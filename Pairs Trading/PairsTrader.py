class PairsTrader:
    def __init__(self, mva, debug, start_cash, filename1, filename2):
        self.mva_days = mva
        self.start_cash = float(start_cash) #setting to float to prevent integer division
        self.cash = float(start_cash)
        ### amounts held of higher and lower priced currencies
        self.shares_higher = float(0)
        self.shares_lower = float(0)
        self.debug = debug
        ### arrays for holding prices
        self.prices_higher = []
        self.prices_lower = []
        self.line_algo = []
        self.line_curr_1 = []
        self.line_curr_2 = []
        self.line_diff = []
        self.line_avg = []
        self.line_upper = []
        self.line_lower = []
        self.line_hold_lower = []
        self.line_hold_higher = []
        self.holdingHigher = True
        file_prices_1 = open(filename1, 'r')
        file_prices_2 = open(filename2, 'r')
        lines = file_prices_1.read().splitlines()
        for line in lines:
            vals = line.split("|")
            self.prices_higher.append(float(vals[3]))
        lines = file_prices_2.read().splitlines()
        for line in lines:
            vals = line.split("|")
            self.prices_lower.append(float(vals[3]))
        ### check to see if higher is in lower array and vice versa
        if self.prices_higher[0] < self.prices_lower[0]:
            self.prices_higher, self.prices_lower = self.prices_lower, self.prices_higher #swap arrays
        ### 
        self.initial_hold_higher = float(start_cash) / float(self.prices_higher[0])
        self.initial_hold_lower = float(start_cash) / float(self.prices_lower[0])
        self.cash = 0
        self.max_time = len(self.prices_higher)
        if len(self.prices_lower) < self.max_time:
            self.max_time = self.prices_lower

    def find_average(self, day):
        avg = 0.0
        for x in range(0, self.mva_days):
            avg += self.line_diff[day - x]
        return avg/self.mva_days

    def price_difference(self, i):
        return self.prices_higher[i] - self.prices_lower[i]

    def trade(self):
        days = 0
        #simulating buying right away
        self.shares_higher = float(self.start_cash) / float(self.prices_higher[0])
        self.cash = 0.0
        aboveAvg = False #determines whether difference is above mva
        for i in range(0, self.max_time):
            ### find difference and add to line_diff
            diff = self.price_difference(i)
            self.line_diff.append(diff)
            if (days > self.mva_days): #only if we're far enough along to use mva
                ### find average
                average = self.find_average(days)
                self.line_avg.append(average)
                ### find upper bound: 105%
                upper = average * 1.1
                self.line_upper.append(upper)
                ### find lower bound: 95%
                lower = average * 0.9
                self.line_lower.append(lower)
                ### see if diff has crossed either line
                if (diff > upper and self.shares_lower > 0): #cross above upper line; difference is moving up
                    #sell lower and buy higher
                    if self.debug:
                        print("day ", days, ", we sold lower and bought higher")
                    ### sell lower
                    self.cash = self.shares_lower * self.prices_lower[i]
                    self.shares_lower = 0
                    ### buy higher
                    self.shares_higher = self.cash / self.prices_higher[i]
                    self.cash = 0
                elif (diff < lower and self.shares_higher > 0): #cross below lower line; difference is moving down
                    #sell higher and buy lower
                    if self.debug:
                        print("day ", days, ", we sold upper and bought lower")
                    ### sell higher
                    self.cash = self.shares_higher * self.prices_higher[i]
                    self.shares_higher = 0
                    ### buy lower
                    self.shares_lower = self.cash / self.prices_lower[i]
                    self.cash = 0
            self.line_algo.append((self.shares_higher * self.prices_higher[i]) + (self.shares_lower * self.prices_lower[i]))
            days += 1
        #sell at the end
        self.cash += (self.shares_higher * self.prices_higher[i]) + (self.shares_lower * self.prices_lower[i])
        self.shares_higher = 0.0
        self.shares_lower = 0.0

    def get_mva_line(self):
        return self.mva_line

    def get_price_line_higher(self):
        return self.prices_higher

    def get_price_line_lower(self):
        return self.prices_lower

    def get_hold_line_higher(self):
        return [self.initial_hold_higher * i for i in self.prices_higher]

    def get_hold_line_lower(self):
        return [self.initial_hold_lower * i for i in self.prices_lower]

    def get_algo_line(self):
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