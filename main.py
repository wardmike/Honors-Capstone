import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from matplotlib.figure import Figure

import os, sys
sys.path.insert(0, os.path.normpath('Moving Average Crossover'))

import MovingAverageCrossoverTrader as mva

##############################################
### Main GUI for Honors Capstone project.  ###
### add more description here			   ###
##############################################
class Main_GUI:

	def __init__(self, master):
		self.master = master
		#title for the window
		master.title("Honors Capstone")
		#dimensions of window (width then height)
		master.geometry("1100x650")
		#window is not resizable
		master.resizable(False, False)

		strategy_selected = tk.IntVar()
		strategy_selected.set(-1)

		#section for selecting algo
		self.algo_selection = tk.LabelFrame(master, text="Select Algorithm", padx = 5, pady = 5)
		self.algo_selection.place(x = 20, y = 20, width=220, height=220)

		self.radio_moving_average_crossover = tk.Radiobutton(self.algo_selection, variable=strategy_selected, text = "Moving Average Crossover", justify=tk.LEFT, value=0)
		self.radio_moving_average_crossover.place(x = 0, y = 10, width=200, height=50)

		self.radio_mean_reversion = tk.Radiobutton(self.algo_selection, variable=strategy_selected, text="Mean Reversion", justify=tk.LEFT, value=1)
		self.radio_mean_reversion.place(x = 0, y = 60, width=135, height=50)

		self.radio_pairs_trading = tk.Radiobutton(self.algo_selection, variable=strategy_selected, text="Pairs Trading", justify=tk.LEFT, value=2)
		self.radio_pairs_trading.place(x = 0, y = 110, width=135, height=50)

		#section for parameter inputs
		self.parameter_selection = tk.LabelFrame(master, text="Parameter Inputs", padx = 5, pady = 5)
		self.parameter_selection.place(x = 260, y = 20, width=220, height=150)

		#label for moving average days
		self.label_mva_days = tk.Label(self.parameter_selection, text="Moving Average Value")
		self.label_mva_days.place(x = 0, y = 0, width=150)

		#entry box for moving average days
		self.entry_mva_days = tk.Entry(self.parameter_selection, bd = 1)
		self.entry_mva_days.place(x = 150, y = 0,  width=50)

		#label for starting amount ($)
		self.label_starting_money = tk.Label(self.parameter_selection, text="Starting Amount ($)")
		self.label_starting_money.place(x = 0, y = 50, width=150)

		#entry box for starting amount ($)
		self.entry_starting_money = tk.Entry(self.parameter_selection, bd = 1)
		self.entry_starting_money.place(x = 150, y = 50,  width=50)

		self.currency_selected = tk.IntVar()
		self.currency_selected.set(-1)

		#section for selecting currency
		self.currency_selection = tk.LabelFrame(master, text="Select Currency", padx = 5, pady = 5)
		self.currency_selection.place(x = 20, y = 260, width=220, height=105)

		self.radio_bitcoin = tk.Radiobutton(self.currency_selection, variable=self.currency_selected, text = "Bitcoin", justify=tk.LEFT, value=0)
		self.radio_bitcoin.place(x = 0, y = 0, width=200, height=25)

		self.radio_ethereum = tk.Radiobutton(self.currency_selection, variable=self.currency_selected, text="Ethereum", justify=tk.LEFT, value=1)
		self.radio_ethereum.place(x = 0, y = 25, width=135, height=25)

		self.radio_litecoin = tk.Radiobutton(self.currency_selection, variable=self.currency_selected, text="Litecoin", justify=tk.LEFT, value=2)
		self.radio_litecoin.place(x = 0, y = 50, width=135, height=25)

		self.second_currency_selected = tk.IntVar()
		self.second_currency_selected.set(-1)

		#section for selecting second currency
		self.second_currency_selection = tk.LabelFrame(master, text="Second Currency (Pairs Trading)", padx = 5, pady = 5)
		self.second_currency_selection.place(x = 20, y = 385, width=220, height=105)
	
		self.radio_bitcoin = tk.Radiobutton(self.second_currency_selection, variable=self.second_currency_selected, text = "Bitcoin", justify=tk.LEFT, value=0)
		self.radio_bitcoin.place(x = 0, y = 0, width=200, height=25)

		self.radio_ethereum = tk.Radiobutton(self.second_currency_selection, variable=self.second_currency_selected, text="Ethereum", justify=tk.LEFT, value=1)
		self.radio_ethereum.place(x = 0, y = 25, width=135, height=25)

		self.radio_litecoin = tk.Radiobutton(self.second_currency_selection, variable=self.second_currency_selected, text="Litecoin", justify=tk.LEFT, value=2)
		self.radio_litecoin.place(x = 0, y = 50, width=135, height=25)

		self.button_run_algo = tk.Button(master, text="Run Algorithm", command=self.run_algo)
		self.button_run_algo.place(x = 50, y = 540, width=150, height=50)

		self.outputText = tk.Text(master, height=10, width=70, borderwidth=2, relief="groove")
		self.outputText.place(x = 500, y = 20)

		self.outputText.config(state=tk.DISABLED)

		self.outputText_scroller = tk.Scrollbar(master)
		self.outputText_scroller.place(x = 981, y = 25, height=150)
		self.outputText_scroller.config(command=self.outputText.yview)
		self.outputText.config(yscrollcommand=self.outputText_scroller.set)

		movingAverageFigure = Figure(figsize=(5,5), dpi=100)
		movingAveragePlot = movingAverageFigure.add_subplot(111)
		movingAveragePlot.plot([1,2,3,4,5,6,7,8],[5,6,1,7,8,2,3,0])

		totalAmountFigure = Figure(figsize=(5,5), dpi=100)
		totalAmountPlot = totalAmountFigure.add_subplot(111)
		totalAmountPlot.plot([1,2,3,4,5,6,7,8],[5,6,1,7,8,2,3,0])

		canvas = FigureCanvasTkAgg(movingAverageFigure, master)
		canvas.show()
		canvas.get_tk_widget().place(x=240, y=180, height=225, width=900)

		canvas = FigureCanvasTkAgg(totalAmountFigure, master)
		canvas.show()
		canvas.get_tk_widget().place(x=240, y=405, height=225, width=900)


	def run_algo(self):
		#code to run moving average crossover here
		if self.entry_mva_days.get() == "":
			#throw error
			pass
		else:
			mva_days = int(self.entry_mva_days.get())
			currency = ""
			filename = ""
			if self.currency_selected.get() == 0:
				currency = "BTC"
				filename = "prices/5-minute/bitcoin.txt"
			elif self.currency_selected.get() == 1:
				currency = "ETH"
				filename = "prices/5-minute/ethereum.txt"
			elif self.currency_selected.get() == 2:
				currency = "LTC"
				filename = "prices/5-minute/litecoin.txt"
			if currency != "" and mva_days != "":
				trader = mva.MovingAverageCrossoverTrader(currency, mva_days, False, filename)
				trader.trade()
				results = trader.results()
				self.outputText.config(state=tk.NORMAL)
				self.outputText.insert(tk.END, results)
				self.outputText.config(state=tk.DISABLED)
				#self.outputText.config(text=results)

	def run_moving_average_crossover(self):
		pass

#################################################
### Create an instance of the Main_GUI object ###
#################################################
def main():
	root = tk.Tk()
	capstone_gui = Main_GUI(root)
	root.mainloop()


if __name__ == '__main__':
	main()
