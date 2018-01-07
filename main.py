import Tkinter as tk

import os, sys
sys.path.insert(0, os.path.normpath('Moving Average Crossover'))

import MovingAverageCrossoverTrader

"""
Main GUI for Honors Capstone project.
**add more description here**
"""
class Main_GUI:

	def __init__(self, master):
		self.master = master
		#title for the window
		master.title("Honors Capstone")
		#dimensions of window (width then height)
		master.geometry("800x400")
		#window is not resizable
		master.resizable(False, False)

		strategy_selected = tk.IntVar()
		strategy_selected.set(0)

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
		self.parameter_selection.place(x = 260, y = 20, width=220, height=220)

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

		currency_selected = tk.IntVar()
		currency_selected.set(0)

		#section for selecting currency
		self.currency_selection = tk.LabelFrame(master, text="Select Currency", padx = 5, pady = 5)
		self.currency_selection.place(x = 500, y = 20, width=225, height=105)

		self.radio_bitcoin = tk.Radiobutton(self.currency_selection, variable=currency_selected, text = "Bitcoin", justify=tk.LEFT, value=0)
		self.radio_bitcoin.place(x = 0, y = 0, width=200, height=25)

		self.radio_ethereum = tk.Radiobutton(self.currency_selection, variable=currency_selected, text="Ethereum", justify=tk.LEFT, value=1)
		self.radio_ethereum.place(x = 0, y = 25, width=135, height=25)

		self.radio_litecoin = tk.Radiobutton(self.currency_selection, variable=currency_selected, text="Litecoin", justify=tk.LEFT, value=2)
		self.radio_litecoin.place(x = 0, y = 50, width=135, height=25)

		second_currency_selected = tk.IntVar()
		second_currency_selected.set(0)

		#section for selecting second currency
		self.second_currency_selection = tk.LabelFrame(master, text="Second Currency (Pairs Trading)", padx = 5, pady = 5)
		self.second_currency_selection.place(x = 500, y = 135, width=225, height=105)

		self.radio_bitcoin = tk.Radiobutton(self.second_currency_selection, variable=second_currency_selected, text = "Bitcoin", justify=tk.LEFT, value=0)
		self.radio_bitcoin.place(x = 0, y = 0, width=200, height=25)

		self.radio_ethereum = tk.Radiobutton(self.second_currency_selection, variable=second_currency_selected, text="Ethereum", justify=tk.LEFT, value=1)
		self.radio_ethereum.place(x = 0, y = 25, width=135, height=25)

		self.radio_litecoin = tk.Radiobutton(self.second_currency_selection, variable=second_currency_selected, text="Litecoin", justify=tk.LEFT, value=2)
		self.radio_litecoin.place(x = 0, y = 50, width=135, height=25)

		#self.button_moving_average_crossover = Button(master, text="Moving Average Crossover", command=self.run_moving_average_crossover)
		#self.button_moving_average_crossover.place(x = 15, y = 15, width=200, height=100)


	def run_moving_average_crossover(self):
		#code to run moving average crossover here
		pass

"""
Create an instance of the Main_GUI object
"""
def main():
	root = tk.Tk()
	capstone_gui = Main_GUI(root)
	root.mainloop()


if __name__ == '__main__':
	main()
