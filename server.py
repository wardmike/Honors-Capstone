import tornado.ioloop
import tornado.web
import tornado.httpserver
import os, sys

sys.path.insert(0, os.path.normpath('Simple Moving Average Crossover'))
sys.path.insert(0, os.path.normpath('Exponential Moving Average Crossover'))
sys.path.insert(0, os.path.normpath('Pairs Trading'))

import SimpleMovingAverageCrossoverTrader as simple_mva


class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	self.render("template.html",
            mva_days="",
            pairs_mva="",
            mva_display="none",
            pairs_display="none",
            cash="",
            text="",
            btc_checked="",
            eth_checked="",
            ltc_checked="",
            bch_checked="",
            xrp_checked="",
            price_data_x=[],
            price_data_y=[],
            mva_data_x=[],
            mva_data_y=[],
            algo_data_y=[],
            hold_data_y=[],
            hold_2_data_y=[]
            )

    def run_mva(self, currency, mva_5_min_input, debug, cash_input, filename):
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
        self.render("template.html",
            mva_days=round(float(mva_5_min_input) / float(288), 1),
            pairs_mva="",
            mva_display="block",
            pairs_display="none",
            cash=cash_input,
            text=results,
            btc_checked=btc_checked,
            eth_checked=eth_checked,
            ltc_checked=ltc_checked,
            bch_checked=bch_checked,
            xrp_checked=xrp_checked,
            price_data_x=list(range(0, len(price_line))),
            price_data_y=price_line,
            mva_data_x=list(range(mva_5_min_input, len(mva_line) + mva_5_min_input)),
            mva_data_y=mva_line,
            algo_data_y=algo_line,
            hold_data_y=hold_line,
            hold_2_data_y=[]
        )

    def run_pairs(self, currency1, currency2, mva_5_min_input, debug, cash_input, filename1, filename2):
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
        self.render("template.html",
            mva_days=round(float(mva_5_min_input) / float(288), 1),
            pairs_mva="",
            mva_display="none",
            pairs_display="block",
            cash=cash_input,
            text=results,
            btc_checked=btc_checked,
            eth_checked=eth_checked,
            ltc_checked=ltc_checked,
            bch_checked=bch_checked,
            xrp_checked=xrp_checked,
            price_data_x=list(range(0, len(price_line))),
            price_data_y=price_line,
            mva_data_x=list(range(mva_5_min_input, len(mva_line) + mva_5_min_input)),
            mva_data_y=mva_line,
            algo_data_y=algo_line,
            hold_data_y=hold_line,
            hold_2_data_y=[]
        )

    def post(self):
        ### get values from form ###
        cash_input = int(self.get_argument('cash'))
        currency = self.get_argument('currency')
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
        if self.get_argument("run_mva"):
            mva_5_min_input = int(float(self.get_argument('mva_days')) * 288)
            self.run_mva(currency, mva_5_min_input, debug, cash_input, filename)
        elif self.get_argument("run_pairs"):
            pass
    

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