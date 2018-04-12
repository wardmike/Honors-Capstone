import tornado.ioloop
import tornado.web
import tornado.httpserver
import os, sys

sys.path.insert(0, os.path.normpath('Simple Moving Average Crossover'))
sys.path.insert(0, os.path.normpath('Exponential Moving Average Crossover'))
sys.path.insert(0, os.path.normpath('Pairs Trading'))
sys.path.insert(0, os.path.normpath('Mean Reversion'))

import SimpleMovingAverageCrossoverTrader as simple_mva
import ExponentialMovingAverageCrossoverTrader as exponential_mva
import PairsTrader as pairs_trader
import MeanReversionTrader as mean_reversion

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class MainHandler(tornado.web.RequestHandler):
    ### values for form ###
    alert = ""
    mva_5_min_input = 500
    offset = ""
    pairs_mva = ""
    mva_display = "none"
    mr_display = "none"
    pairs_display = "none"
    hold_two_display = "none"
    cash = ""
    text = ""
    simple_checked = "checked"
    exponential_checked = ""
    btc_checked = "checked"
    eth_checked = ""
    ltc_checked = ""
    bch_checked = ""
    xrp_checked = ""
    btc2_checked = ""
    eth2_checked = "checked"
    ltc2_checked = ""
    bch2_checked = ""
    xrp2_checked = ""
    price_data_x = []
    price_data_y = []
    mva_data_x = []
    mva_data_y = []
    upper_data_y = []
    lower_data_y = []
    algo_data_y = []
    hold_higher_data_y = []
    hold_lower_data_y = []
    ### supporting values ###
    debug = False
    currency = "BTC"
    filename = "prices/5-minute/bitcoin.txt"
    currency2 = "ETH"
    filename2 = "prices/5-minute/ethereum.txt"

    def update_currency(self):
        if (self.currency == "BTC"):
            self.btc_checked = "checked"
            self.filename = "prices/5-minute/bitcoin.txt"
        elif (self.currency == "ETH"):
            self.eth_checked = "checked"
            self.filename = "prices/5-minute/ethereum.txt"
        elif (self.currency == "LTC"):
            self.ltc_checked = "checked"
            self.filename = "prices/5-minute/litecoin.txt"
        elif (self.currency == "BCH"):
            self.bch_checked = "checked"
            self.filename = "prices/5-minute/bitcoin-cash.txt"
        elif (self.currency == "XRP"):
            self.xrp_checked = "checked"
            self.filename = "prices/5-minute/ripple.txt"

    def update_currency2(self):
        if (self.currency2 == "BTC"):
            self.btc2_checked = "checked"
            self.filename2 = "prices/5-minute/bitcoin.txt"
        elif (self.currency2 == "ETH"):
            self.eth2_checked = "checked"
            self.filename2 = "prices/5-minute/ethereum.txt"
        elif (self.currency2 == "LTC"):
            self.ltc2_checked = "checked"
            self.filename2 = "prices/5-minute/litecoin.txt"
        elif (self.currency2 == "BCH"):
            self.bch2_checked = "checked"
            self.filename2 = "prices/5-minute/bitcoin-cash.txt"
        elif (self.currency2 == "XRP"):
            self.xrp2_checked = "checked"
            self.filename2 = "prices/5-minute/ripple.txt"


    def render_page(self):
        self.render("template.html",
            alert=self.alert,
            mva_days=round(float(self.mva_5_min_input) / float(288), 1),
            offset=self.offset,
            pairs_mva=self.pairs_mva,
            mva_display=self.mva_display,
            mr_display=self.mr_display,
            pairs_display=self.pairs_display,
            hold_two_display=self.hold_two_display,
            cash=self.cash,
            text=self.text,
            simple_checked=self.simple_checked,
            exponential_checked=self.exponential_checked,
            btc_checked=self.btc_checked,
            eth_checked=self.eth_checked,
            ltc_checked=self.ltc_checked,
            bch_checked=self.bch_checked,
            xrp_checked=self.xrp_checked,
            btc2_checked=self.btc2_checked,
            eth2_checked=self.eth2_checked,
            ltc2_checked=self.ltc2_checked,
            bch2_checked=self.bch2_checked,
            xrp2_checked=self.xrp2_checked,
            price_data_x=self.price_data_x,
            price_data_y=self.price_data_y,
            mva_data_x=self.mva_data_x,
            mva_data_y=self.mva_data_y,
            upper_data_y=self.upper_data_y,
            lower_data_y=self.lower_data_y,
            algo_data_y=self.algo_data_y,
            hold_higher_data_y=self.hold_higher_data_y,
            hold_lower_data_y=self.hold_lower_data_y
        )

    def get(self):
    	self.render_page()

    def run_mva(self):
        ## check if offset has been entered
        if self.get_argument('mva-type', None) == None:
            self.alert = "Error: please select simple or exponential moving average."
            self.render_page()
            return
        mva_type = self.get_argument('mva-type')
        ### get results from Simple Moving Average Crossover Trader ###
        trader = ""
        if (mva_type == 'simple_mva'):
            self.simple_checked = "checked"
            self.exponential_checked = ""
            trader = simple_mva.SimpleMovingAverageCrossoverTrader(self.currency, self.mva_5_min_input, self.debug, self.cash, self.filename)
        else:
            self.simple_checked = ""
            self.exponential_checked = "checked"
            trader = exponential_mva.ExponentialMovingAverageCrossoverTrader(self.currency, self.mva_5_min_input, self.debug, self.cash, self.filename)
        trader.trade()
        #results = trader.results()
        price_line = trader.get_price_line()
        mva_line = trader.get_mva_line()
        algo_line = trader.get_algo_line()
        hold_line = trader.get_hold_line()
        
        ### update values
        self.pairs_mva = ""
        self.mva_display = "block"
        self.mr_display = "none"
        self.pairs_display = "none"
        self.hold_two_display = "block"
        self.price_data_x = list(range(0, len(price_line)))
        self.price_data_y = price_line
        self.upper_data_y=[]
        self.lower_data_y=[]
        self.mva_data_x=list(range(self.mva_5_min_input, len(mva_line) + self.mva_5_min_input))
        self.mva_data_y=mva_line
        self.algo_data_y=algo_line
        self.hold_higher_data_y=hold_line
        self.hold_lower_data_y=[]
        ### render the page
        self.alert = ""
        self.render_page()

    def run_mean_reversion(self):
        ### check if offset has been entered
        if self.get_argument('offset', None) == None:
            self.alert = "Error: please enter a proper offset."
            self.render_page()
            return
        self.offset = self.get_argument('offset')
        if not is_float(self.offset):
            self.alert = "Error: please enter a proper offset."
            self.render_page()
            return
        ### get results from Simple Moving Average Crossover Trader ###
        trader = mean_reversion.MeanReversionTrader(self.currency, self.mva_5_min_input, self.offset, self.debug, self.cash, self.filename)
        trader.trade()
        #results = trader.results()
        line_prices = trader.get_line_price()
        line_avg = trader.get_line_avg()
        line_upper = trader.get_line_upper()
        line_lower = trader.get_line_lower()
        line_algo = trader.get_line_algo()
        line_hold = trader.get_line_hold()
        ### handle setting correct checkbox ###
        self.update_currency()
        self.pairs_mva=""
        self.mva_display="none"
        self.mr_display="block"
        self.pairs_display="none"
        self.hold_two_display="block"
        self.price_data_x=list(range(0, len(line_prices)))
        self.price_data_y=line_prices
        self.mva_data_x=list(range(self.mva_5_min_input, len(line_avg) + self.mva_5_min_input))
        self.mva_data_y=line_avg
        self.upper_data_y=line_upper
        self.lower_data_y=line_lower
        self.algo_data_y=line_algo
        self.hold_higher_data_y=line_hold
        self.hold_lower_data_y=[]
        ### render the page
        self.alert = ""
        self.render_page()

    def run_pairs(self):
        ### check if currency2 has been entered
        if self.get_argument('currency2', None) == None:
            self.alert = "Error: please select second currency."
            self.render_page()
            return
        self.currency2 = self.get_argument('currency2')
        self.update_currency2()
        ### get results from Simple Moving Average Crossover Trader ###
        trader = pairs_trader.PairsTrader(self.mva_5_min_input, self.debug, self.cash, self.filename, self.filename2)
        trader.trade()
        price_line_higher = trader.get_price_line_higher()
        price_line_lower = trader.get_price_line_lower()
        algo_line = trader.get_algo_line()
        hold_line_higher = trader.get_hold_line_higher()
        hold_line_lower = trader.get_hold_line_lower()
        #self.pairs_mva=offset
        self.mva_display="none"
        self.mr_display="none"
        self.pairs_display="block"
        self.hold_two_display="none"
        self.price_data_x=list(range(0, len(price_line_higher)))
        self.price_data_y=price_line_higher
        self.mva_data_x=[]
        self.mva_data_y=[]
        self.upper_data_y=[]
        self.lower_data_y=[]
        self.algo_data_y=algo_line
        self.hold_higher_data_y=hold_line_higher
        self.hold_lower_data_y=hold_line_lower
        ### render the page
        self.alert = ""
        self.render_page()

    def post(self):
        ### get values from form ###
        if self.get_argument('cash', None) == None:
            self.alert = "Error: please enter a proper value for starting cash."
            self.render_page()
            return
        cash = self.get_argument('cash')
        if not is_int(cash):
            self.alert = "Error: please enter a proper value for starting cash."
            self.render_page()
            return
        self.cash = int(cash)
        if self.get_argument('currency', None) == None:
            self.alert = "Error: please select a currency."
            self.render_page()
            return
        self.currency = self.get_argument('currency')
        if self.get_argument('mva_days', None) == None:
            self.alert = "Error: please enter a valid moving average length."
            self.render_page()
            return
        mva_days = self.get_argument('mva_days')
        if not is_float(mva_days):
            self.alert = "Error: please enter a valid moving average length."
            self.render_page()
            return
        self.mva_5_min_input = int(float(mva_days) * 288)
        debug = False
        self.update_currency()
        if self.get_argument("run_mva", None) != None:
            self.run_mva()
        elif self.get_argument("run_mean-reversion", None) != None:
            self.run_mean_reversion()
        elif self.get_argument("run_pairs", None) != None:
            self.run_pairs()


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