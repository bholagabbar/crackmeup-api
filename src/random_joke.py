# DO NOT NAME FILE AS `random.py`

# Modifying the original 'crackmeup' script from http://github.com/bholagabbar/crackmeup

import urllib
import random
import re

from bs4 import BeautifulSoup

def jokesDotCCDotcom():

	'''to get random jokes from jokes.cc.com, we're going to use the API I dug up from their site (#sweg).
	-Send a request to http://jokes.cc.com/feeds/random/(any number between 1-6811)
	-Data recieved is in JSON
	-Extract this link, send a urllib request there and scrape out the joke from the HTML recieved
	'''
	randomLinkToGoToAPI = 'http://jokes.cc.com/feeds/random/' + str(random.randint(1, 6779))
	JSONData = urllib.urlopen(randomLinkToGoToAPI).read()
	#parse data
	parsedJokeLink = JSONData[JSONData.index('http') : JSONData.index('","queryString')].replace('\\',"")
	#Now send a request to parse this random joke link
	handle = urllib.urlopen(parsedJokeLink)
	htmlGunk =  handle.read()
	soup = BeautifulSoup(htmlGunk, "html.parser")
	jokeData = soup.findAll('div', {'class':'content_wrap'})[0].get_text()
	if 'Next' in jokeData:
		jokeData = jokeData[jokeData.index('Next')+5:]
	return jokeData
	
def jokesYouDotcom():
	urlToRead = "http://www.jokesyou.com/"
	handle = urllib.urlopen(urlToRead)
	htmlGunk =  handle.read()
	soup = BeautifulSoup(htmlGunk, "html.parser")
	joke = soup.findAll('div', {'class':'right'})[0].findAll('p')[0]
	joke = str(joke)
	#Regex replace
	joke = re.sub(r'<p>', r'', joke)
	joke = re.sub(r'</p>|<br/>', r'\n', joke)
	return joke


def getJoke():
	whichSite = random.randint(1,2)
	if whichSite == 1:
		return jokesDotCCDotcom()
	else:
		return jokesYouDotcom()