import tornado.ioloop
import tornado.web
import tornado.httpserver
import os, sys

sys.path.insert(0, os.path.normpath('Simple Moving Average Crossover'))

import SimpleMovingAverageCrossoverTrader as simple_mva


class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	self.render("template.html",
            mva_days="",
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
            hold_data_y=[]
            )

    def post(self):
        mva_5_min_input = int(float(self.get_argument('mva_days')) * 288)
        cash_input = int(self.get_argument('cash'))
        currency = self.get_argument('currency')
        btc_checked = ""
        eth_checked = ""
        ltc_checked = ""
        bch_checked = ""
        xrp_checked = ""
        filename = ""
        if (currency == "BTC"):
            btc_checked = "checked"
            filename = "prices/5-minute/bitcoin.txt"
        elif (currency == "ETH"):
            filename = "prices/5-minute/ethereum.txt"
            eth_checked = "checked"
        elif (currency == "LTC"):
            filename = "prices/5-minute/litecoin.txt"
            ltc_checked = "checked"
        elif (currency == "BCH"):
            filename = "prices/5-minute/bitcoin-cash.txt"
            bch_checked = "checked"
        elif (currency == "XRP"):
            filename = "prices/5-minute/ripple.txt"
            xrp_checked = "checked"
        trader = simple_mva.SimpleMovingAverageCrossoverTrader(currency, mva_5_min_input, True, cash_input, filename)
        trader.trade()
        results = trader.results()
        price_line = trader.get_price_line()
        mva_line = trader.get_mva_line()
        algo_line = trader.get_algo_line()
        hold_line = trader.get_hold_line()
        self.render("template.html",
            mva_days= round(float(mva_5_min_input) / float(288), 1),
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
            hold_data_y=hold_line
            )

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