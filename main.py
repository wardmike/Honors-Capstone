import Tkinter as tk

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
		master.geometry("600x500")
		#window is not resizable
		master.resizable(False, False)

		strategy_selected = tk.IntVar()
		strategy_selected.set(0)

		#section for selecting algo
		self.algo_selection = tk.LabelFrame(master, text="Select Algorithm", padx = 5, pady = 5)
		self.algo_selection.place(x = 20, y = 20, width=220, height=400)

		self.radio_moving_average_crossover = tk.Radiobutton(self.algo_selection, variable=strategy_selected, text = "Moving Average Crossover", justify=tk.LEFT, value=0)
		self.radio_moving_average_crossover.place(x = 0, y = 0, width=200, height=50)

		self.radio_mean_reversion = tk.Radiobutton(self.algo_selection, variable=strategy_selected, text="Mean Reversion", justify=tk.LEFT, value=1)
		self.radio_mean_reversion.place(x = 0, y = 50, width=135, height=50)

		self.radio_pairs_trading = tk.Radiobutton(self.algo_selection, variable=strategy_selected, text="Pairs Trading", justify=tk.LEFT, value=2)
		self.radio_pairs_trading.place(x = 0, y = 100, width=135, height=50)

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
