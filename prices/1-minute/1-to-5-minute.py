'''
Simple script to extract 5-minute data from 1-minute data.
'''

import sys
from datetime import datetime

def oneToFiveMinute(filename, year, month, day, hour, minute):
	year = int(year)
	month = int(month)
	day = int(day)
	hour = int(hour)
	minute = int(minute)
	oneMinFile = open(filename + ".txt", "r")
	fiveMinFile = open(filename + "5min.txt", "w")
	for line in oneMinFile:
		vals = line.split("|")
		price_time = datetime.strptime(vals[0], '%Y-%m-%d %H:%M:%S')
		if price_time.minute % 5 == 0:
			if price_time.year == year:
				if price_time.month == month:
					if price_time.day == day:
						if price_time.hour == hour:
							if price_time.minute >= minute:
								fiveMinFile.write(line)
						elif price_time.hour > hour:
							fiveMinFile.write(line)
					elif price_time.day > day:
						fiveMinFile.write(line)
				elif price_time.month > month:
					fiveMinFile.write(line)
			elif price_time.year > year:
				fiveMinFile.write(line)

	oneMinFile.close()
	fiveMinFile.close()

if __name__ == '__main__':
	oneToFiveMinute(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])