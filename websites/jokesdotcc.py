import json
import random
import urllib

from bs4 import BeautifulSoup

dataFile = open('C:/Users/bholagabbar/Desktop/crackmeup-api/websites/jokescc-data.txt') #change to complete path! Idk w
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
	jokeData = soup.findAll('div', {'class':'content_wrap'})[0].get_text()
	if 'Next' in jokeData:
		jokeData = jokeData[jokeData.index('Next')+5:]
	return jokeData.rstrip()