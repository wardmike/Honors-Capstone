#!/usr/bin/python3
import requests
from datetime import datetime
class currency:
	def __init__ (self, name, symbol):
		self.name = name
		self.symbol = symbol

def get_json():
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=50')
    return r.json()

def print_to_file(json):
    file_data = open("data.txt", "a")
    file_data.write(json["time"]["updated"])
    file_data.write("   ")
    file_data.write(get_current_bitcoin_price(json))
    file_data.write("\n")
    return

json = get_json()
for each in json:
	file_data = open("/home/stan/Desktop/Working/"+each['id']+".txt", "a")
	file_data.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"|")
	c = currency(each['id'], each["symbol"])
	c.rank = each['rank']
	c.price_usd = each['price_usd']
	c.price_btc = each['price_btc']
	c.h24_volume_usd = each['24h_volume_usd']
	if c.h24_volume_usd is None:
		c.h24_volume_usd = '0'

	c.market_cap_usd = each['market_cap_usd']
	if c.market_cap_usd is None:
		c.market_cap_usd = '0'

	c.available_supply = each['available_supply']
	if c.available_supply is None:
		c.available_supply = '0'

	c.total_supply = each['total_supply']
	if c.total_supply is None:
		c.total_supply = '0'

	c.perc_change_1hr = each['percent_change_1h']
	if c.perc_change_1hr is None:
		c.perc_change_1hr = '0'

	c.perc_change_24hr = each['percent_change_24h']
	if c.perc_change_24hr is None:
		c.perc_change_24hr = '0'

	c.perc_change_7d = each['percent_change_7d']
	if c.perc_change_7d is None:
		c.perc_change_7d = '0'

	file_data.write(c.name +"|"+ c.symbol+"|"+c.price_usd+"|"+c.price_btc+"|"+c.h24_volume_usd+"|"+c.market_cap_usd+"|"+c.available_supply+"|"+c.total_supply+"|"+c.perc_change_1hr+"|"+c.perc_change_24hr+"|"+c.perc_change_7d+"|")
	file_data.write("\n")
