# lucky.py - Opens several Google search results.
# See page 248 in automate the boring stuffs!

import requests, sys, webbrowser, bs4

print('Googling...')
results = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
results.raise_for_status()

topresults = bs4.BeautifulSoup(results.text, "lxml")

allLinks = topresults.select('.r a')

numberToOpen = min(9, len(allLinks))
for x in range(numberToOpen):
	webbrowser.open('http://google.com' + allLinks[x].get('href'))