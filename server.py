import tornado.ioloop
import tornado.web
import tornado.httpserver
import os, sys

sys.path.insert(0, os.path.normpath('Simple Moving Average Crossover'))
sys.path.insert(0, os.path.normpath('Exponential Moving Average Crossover'))
sys.path.insert(0, os.path.normpath('Pairs Trading'))

import SimpleMovingAverageCrossoverTrader as simple_mva

import PairsTrader as pairs_trader


class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	self.render("template.html",
            mva_days="",
            pairs_mva="",
            mva_display="none",
            pairs_display="none",
            cash="",
            text="",
            btc_checked="checked",
            eth_checked="",
            ltc_checked="",
            bch_checked="",
            xrp_checked="",
            btc2_checked="",
            eth2_checked="checked",
            ltc2_checked="",
            bch2_checked="",
            xrp2_checked="",
            price_data_x=[],
            price_data_y=[],
            mva_data_x=[],
            mva_data_y=[],
            algo_data_y=[],
            hold_higher_data_y=[],
            hold_lower_data_y=[]
            )

    def run_mva(self, currency, currency2, mva_5_min_input, debug, cash_input, filename):
        ### get results from Simple Moving Average Crossover Trader ###
        trader = simple_mva.SimpleMovingAverageCrossoverTrader(currency, mva_5_min_input, debug, cash_input, filename)
        trader.trade()
        results = trader.results()
        price_line = trader.get_price_line()
        mva_line = trader.get_mva_line()
        algo_line = trader.get_algo_line()
        hold_line = trader.get_hold_line()
        ### handle setting correct checkbox ###
        btc_checked = ""
        eth_checked = ""
        ltc_checked = ""
        bch_checked = ""
        xrp_checked = ""
        btc2_checked = ""
        eth2_checked = ""
        ltc2_checked = ""
        bch2_checked = ""
        xrp2_checked = ""
        if (currency == "BTC"):
            btc_checked = "checked"
        elif (currency == "ETH"):
            eth_checked = "checked"
        elif (currency == "LTC"):
            ltc_checked = "checked"
        elif (currency == "BCH"):
            bch_checked = "checked"
        elif (currency == "XRP"):
            xrp_checked = "checked"
        if (currency2 == "BTC"):
            btc2_checked = "checked"
        elif (currency2 == "ETH"):
            eth2_checked = "checked"
        elif (currency2 == "LTC"):
            ltc2_checked = "checked"
        elif (currency2 == "BCH"):
            bch2_checked = "checked"
        elif (currency2 == "XRP"):
            xrp2_checked = "checked"
        self.render("template.html",
            mva_days=round(float(mva_5_min_input) / float(288), 1),
            pairs_mva="",
            mva_display="block",
            pairs_display="none",
            cash=cash_input,
            text="", #results are inaccurate
            btc_checked=btc_checked,
            eth_checked=eth_checked,
            ltc_checked=ltc_checked,
            bch_checked=bch_checked,
            xrp_checked=xrp_checked,
            btc2_checked=btc2_checked,
            eth2_checked=eth2_checked,
            ltc2_checked=ltc2_checked,
            bch2_checked=bch2_checked,
            xrp2_checked=xrp2_checked,
            price_data_x=list(range(0, len(price_line))),
            price_data_y=price_line,
            mva_data_x=list(range(mva_5_min_input, len(mva_line) + mva_5_min_input)),
            mva_data_y=mva_line,
            algo_data_y=algo_line,
            hold_higher_data_y=hold_line,
            hold_lower_data_y=[]
        )

    def run_pairs(self, currency, currency2, mva_5_min_input, debug, cash_input, filename1, filename2):
        ### get results from Simple Moving Average Crossover Trader ###
        trader = pairs_trader.PairsTrader(mva_5_min_input, debug, cash_input, filename1, filename2)
        trader.trade()
        price_line_higher = trader.get_price_line_higher()
        price_line_lower = trader.get_price_line_lower()
        algo_line = trader.get_algo_line()
        hold_line_higher = trader.get_hold_line_higher()
        hold_line_lower = trader.get_hold_line_lower()
        ### handle setting correct checkbox ###
        btc_checked = ""
        eth_checked = ""
        ltc_checked = ""
        bch_checked = ""
        xrp_checked = ""
        btc2_checked = ""
        eth2_checked = ""
        ltc2_checked = ""
        bch2_checked = ""
        xrp2_checked = ""
        if (currency == "BTC"):
            btc_checked = "checked"
        elif (currency == "ETH"):
            eth_checked = "checked"
        elif (currency == "LTC"):
            ltc_checked = "checked"
        elif (currency == "BCH"):
            bch_checked = "checked"
        elif (currency == "XRP"):
            xrp_checked = "checked"
        if (currency2 == "BTC"):
            btc2_checked = "checked"
        elif (currency2 == "ETH"):
            eth2_checked = "checked"
        elif (currency2 == "LTC"):
            ltc2_checked = "checked"
        elif (currency2 == "BCH"):
            bch2_checked = "checked"
        elif (currency2 == "XRP"):
            xrp2_checked = "checked"
        self.render("template.html",
            mva_days=round(float(mva_5_min_input) / float(288), 1),
            pairs_mva="",
            mva_display="none",
            pairs_display="block",
            cash=cash_input,
            text="",
            btc_checked=btc_checked,
            eth_checked=eth_checked,
            ltc_checked=ltc_checked,
            bch_checked=bch_checked,
            xrp_checked=xrp_checked,
            btc2_checked=btc2_checked,
            eth2_checked=eth2_checked,
            ltc2_checked=ltc2_checked,
            bch2_checked=bch2_checked,
            xrp2_checked=xrp2_checked,
            price_data_x=list(range(0, len(price_line_higher))),
            price_data_y=price_line_higher,
            mva_data_x=[],
            mva_data_y=[],
            algo_data_y=algo_line,
            hold_higher_data_y=hold_line_higher,
            hold_lower_data_y=hold_line_lower
        )

    def post(self):
        ### get values from form ###
        cash_input = int(self.get_argument('cash'))
        currency = self.get_argument('currency')
        currency2 = self.get_argument('currency2')
        mva_5_min_input = int(float(self.get_argument('mva_days')) * 288)
        debug = True
        ### find correct filename ###
        filename = ""
        if (currency == "BTC"):
            filename = "prices/5-minute/bitcoin.txt"
        elif (currency == "ETH"):
            filename = "prices/5-minute/ethereum.txt"
        elif (currency == "LTC"):
            filename = "prices/5-minute/litecoin.txt"
        elif (currency == "BCH"):
            filename = "prices/5-minute/bitcoin-cash.txt"
        elif (currency == "XRP"):
            filename = "prices/5-minute/ripple.txt"
        if self.get_argument("run_mva", None) != None: 
            self.run_mva(currency, currency2, mva_5_min_input, debug, cash_input, filename)
        elif self.get_argument("run_pairs", None) != None:
            filename2 = ""
            if (currency2 == "BTC"):
                filename2 = "prices/5-minute/bitcoin.txt"
            elif (currency2 == "ETH"):
                filename2 = "prices/5-minute/ethereum.txt"
            elif (currency2 == "LTC"):
                filename2 = "prices/5-minute/litecoin.txt"
            elif (currency2 == "BCH"):
                filename2 = "prices/5-minute/bitcoin-cash.txt"
            elif (currency2 == "XRP"):
                filename2 = "prices/5-minute/ripple.txt"
            self.run_pairs(currency, currency2, mva_5_min_input, debug, cash_input, filename, filename2)
    

class Server(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            # Add more paths here
        ]
        settings = {
        "debug": True,
        "template_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"),
        "static_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
        }
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    application = Server()
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    #app = make_app()
    #app.listen(8888)
    #tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
	main()