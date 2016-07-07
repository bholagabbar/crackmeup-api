import random

import websites.jokes_dotcc.scrape as jokescc

def getRandomJoke():
	joke = jokescc.getJoke('dark-humor')
	return joke