import json
import random
import urllib
import os

from bs4 import BeautifulSoup

dataFile = open(os.getcwd()+'\\src\\websites\\jokes_dotcc\\jokescc-data.txt')
dataDic = dict(json.loads(dataFile.read()))

def getJoke(category):
	index = random.choice(dataDic[category])
	apiLink = 'http://jokes.cc.com/feeds/random/' + str(index)
	JSONData = urllib.urlopen(apiLink).read()
	#parse data
	parsedJokeLink = JSONData[JSONData.index('http') : JSONData.index('","queryString')].replace('\\',"")
	#Now send a request to parse this random joke link
	handle = urllib.urlopen(parsedJokeLink)
	htmlGunk =  handle.read()
	soup = BeautifulSoup(htmlGunk, "html.parser")
	joke = soup.findAll('div', {'class':'content_wrap'})[0].get_text()
	if 'Next' in joke:
		joke = joke[joke.index('Next')+5:]
	joke = joke.replace("\n", " ")
	joke = joke.replace("\t", " ")
	joke = joke.strip()
	return joke