# import beautiful soup?
from time import time

from datetime import time, date

import gtfo
url = gtfo.roundtrip().departing("JFK").returning("JNB").open()
print(url)
exit()

# import read file? 

# TODO: install submlime plugin for easy edit CSVs
# TODO: install submlime plugin for easy open explorer
# TODO: install phone app for free airport wifis

# constants OR read config file
MPG = 27
pricePerGal = 2.29
hourWage = (24000 / 52 ) / 40 
airportTimeAdd = time(1, 30, 0)
driveTimeAdd  = time(0, 0, 0)
shuttleTimeAdd = time(0,0,0)
airportTimeMulti = 1.00
driveTimeMulti  = 1.00
shuttleTimeMulti = 1.00


scheduleStrictness = 10
searchDayStart = date("December 18 2018")
searchDayEnd = date("Janurary 8 2019")


def main():
	pass
	# read driveDest.csv validate?
	# make requests to google flights
		# start with longest trip length possible
		# dynamic stop?  nonono too many requests can be banned

	# match driveDest to google flights numbers


if __name__ == '__main__':
	main()
