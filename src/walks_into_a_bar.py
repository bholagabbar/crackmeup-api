import random

import websites.jokes_dotcc.scrape as jokescc
import websites.jokesyou_dotcom.scrape as jokesyou

def getRandomJoke():
	index = random.randint(*(1, 2))
	joke = ''
	if index == 1:
		joke = jokescc.getJoke('walks-into-a-bar')
	elif index == 2:
		joke = jokesyou.getJoke('barjokes')
	return joke