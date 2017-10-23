class MovingAverageCrossoverTrader(object):
    def __init__(self, name):
        self.mva_days = 10
        self.buy = 0.0
        self.profit = 0.0
        self.cash = 1000.00
        self.prices = []
        filename = "prices/" + name + ".txt"
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
                if (price > average and buy==0.0):
                    print "day ", days, ", we bought at price: ", price
                    buy = price
                elif (price < average and buy != 0.0):
                    print "day ", days, ", we sold at price: ", price
                    print "Profit for this trade: ", price - buy
                    self.profit += price - buy
                    buy = 0.0
            days += 1

    def print_results(self):
        print "total profit: ", self.profit
        print "returns (algorithm): ", self.profit/self.prices[0] * 100, "%"
        print "returns (buy and hold): ", self.prices[-1]/self.prices[0] * 100, "%"


def main():
    trader = MovingAverageCrossoverTrader("btc")
    trader.trade()
    trader.print_results()


if __name__ == "__main__":
    main()
