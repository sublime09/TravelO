from bs4 import BeautifulSoup
from time import time
from pprint import pprint
from datetime import time, date

# TODO: install submlime plugin for easy edit CSVs
# TODO: install submlime plugin for easy open explorer
# TODO: install phone app for free airport wifis

# pprint(vars(gtfo), indent=2, depth=1)
# this searches methods

saveFilename = 'gFlightResult.html' 

def readSavedFlight():
	html_doc = None
	with open('gFlightResult.html', 'r') as f:
		html_doc = f.read()
	return html_doc

def gtfoToUrlToFile():
	import gtfo
	import urllib.request
	tripDeets = gtfo.roundtrip().departing("ROA").returning("STL")
	gFlightURL = str(tripDeets.url())
	html_doc = None
	with urllib.request.urlopen(str(gFlightURL)) as f:
		html_doc = f.read()
	with open(saveFilename, 'wb') as f:
		f.write(html_doc)
	return html_doc


html_doc = readSavedFlight()

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())


# constants OR read config file
MPG = 27
pricePerGal = 2.29
hourWage = (24000 / 52) / 40
airportTimeAdd = time(1, 30, 0)
driveTimeAdd = time(0, 0, 0)
shuttleTimeAdd = time(0, 0, 0)
airportTimeMulti = 1.00
driveTimeMulti = 1.00
shuttleTimeMulti = 1.00

searchDayStart = date(2018, 12, 18)
searchDayEnd = date(2019, 1, 8)
searchMinTripDays = 10
assert (searchDayEnd - searchDayStart).days > searchMinTripDays


def main():
    pass
    # read driveDest.csv validate?
    # make requests to google flights
    # start with longest trip length possible
    # dynamic stop?  nonono too many requests can be banned

    # match driveDest to google flights numbers


if __name__ == '__main__':
    main()
