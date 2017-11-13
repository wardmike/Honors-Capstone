'''
Simple script to get only prices from 5-minute full-data.
'''


def shorten_data(curr_name):
	input_filename = "../prices/full-data/" + curr_name + ".txt"
	output_filename =  "../prices/5-minute-just-prices/" + curr_name + ".txt"
	intput_file = open(input_filename, "r")
	output_file = open(output_filename, "w")
	for line in intput_file:
		vals = line.split("|")
		output_file.write(vals[3])
		output_file.write("\n")



def main():
	shorten_data("bitcoin")




if __name__ == '__main__':
	main()