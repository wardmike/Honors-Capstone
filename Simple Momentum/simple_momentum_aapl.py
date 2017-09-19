def initialize(context):
	context.aapl = sid(24)

	if data.can_trade(context.aapl):
    	order_target_percent(context.aapl, 1)

def handle_data(context, data):
	cash = context.portfolio.cash

	average_price = context.aapl.mavg(5)
	current_price = context.aapl.price

	if current_price > average_price and cash > current_price:
		shares_to_buy = int(cash/current_price)
		order(context.aapl, shares_to_buy)
	elif current_price < average_price:
		number_of_shares = context.portfolio.positions