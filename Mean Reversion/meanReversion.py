#Mean Reversion - Michael Ward, September 2017

TIME_FRAME = 5

#called once on algorithm start
def initialize(context):
	context.aapl = sid(24)

	 # Position 100% of our portfolio to be long in AAPL
    if data.can_trade(context.aapl):
    	order_target_percent(context.aapl, 1)

#called once at the end of each minute
def handle_data(context, data):
	#calculate x-day average of stock
	aapl_current = data[context.aapl].price
	aapl_x_day = data.history(context.aapl, 'price', TIME_FRAME, '1d')
	aapl_x_day_average = aapl_x_day.mean()
	#calculate bars at 0.98 and 1.02

	bar_high = 1.02 * aapl_x_day

	bar_low = 0.98 * aapl_x_day


	#buy or sell depening on wether it's higher or lower
