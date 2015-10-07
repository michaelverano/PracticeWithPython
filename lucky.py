#!	python3
#	lucky.python3 - Opens several Google results.

import requests, sys, webbrowser, bs4, logging

#Debug Mode
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # turns debug mode off

print('Googling...') # display text while downloading the Google page.
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
logging.debug('printing res.raise_for_status... ' + str(res.raise_for_status))

# TODO: Retrieve top search result links.
soup 		= bs4.BeautifulSoup(res.text, 'lxml')

# TODO: Open a browser tab for search results.
linkElems 	= soup.select('.r a') 
numOpen 	= min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))