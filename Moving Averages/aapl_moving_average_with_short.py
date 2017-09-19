##################################################
#
# 10 - Day Moving Average of AAPL Stock with Short
# by Michael Ward
#
##################################################

days_passed = -1

#called once on algorithm start
def initialize(context):
    # Reference to AAPL
    context.aapl = sid(24)

    # Position 100% of our portfolio to be long in AAPL
    if data.can_trade(context.aapl):
    	order_target_percent(context.aapl, 1)
    

#called every day before market open
def before_trading_start(context, data):
    days_passed = days_passed + 1

#called once at the end of each minute
def handle_data(context, data):
    aapl_current = data[context.aapl].price
	aapl_10_day = data.history(context.aapl, 'price', 10, '1d')
	aapl_10_day_average = aapl_10_day.mean()

    if(days_passed > 9):
        if (aapl_current > aapl_10_day):
            print "------------------"
            print "Buying aapl stocks"
            print "10-day avg: ", aapl_10_day
            print "current price", aapl_current
            order_target_percent(context.aapl, 1.00)
        elif:
            print "------------------"
            print "Selling aapl stocks"
            print "10-day avg: ", aapl_10_day
            print "current price: ", aapl_current
            order_target_percent(context.aapl, -1.00)
        else:
            pass


    

def buy_aapl_shares(shares):
    order(context.aapl, shares)
    log.info("Buying %s" % (context.aapl.symbol))
    
#called once per day before trading starts
def before_trading_start(context, data):
	pass


