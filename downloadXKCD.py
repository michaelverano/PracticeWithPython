#!	python3
#	downloadXKCD.py - Downlods every single XKCD comic.

import requests, os, bs4, logging

#Debug Mode
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # turns debug mode off when not commented.

url	= 'http://xkcd.com'	 			# starting url
os.makedirs('xkcd', exist_ok=True)	# store comics in ./xkcd

while not url.endswith('#'):
	# Download the page.
	print('Downloading page %s' % url)
	res = requests.get(url)
	res.raise_for_status() # Check to see the website exists.
	
	soup = bs4.BeautifulSoup(res.text, 'lxml')
	logging.debug('raise for status...' + str(soup))

	# Find the url of the comic image.
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find comic image.')
	else:
		logging.debug('ComicElem are...' + str(comicElem)) # used for debugging.
		comicURL = comicElem[0].get('src').strip('//')
		# Download the image.
		print('Downloading images %s... ' % (comicURL))
		res = requests.get('http://' + comicURL)
		res.raise_for_status()

		# Save the image to ./xkcd.
		imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

	# Get the prev button's url.
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')
	
print('Done.')