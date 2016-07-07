import random

import websites.jokes_dotcc.scrape as jokescc
import websites.jokesyou_dotcom.scrape as jokesyou
import websites.randomjoke_dotcom.scrape as randomjoke

def getRandomJoke():
	index = random.randint(*(1, 3))
	joke = ''
	if index == 1:
		joke = jokescc.getJoke('blonde')
	elif index == 2:
		joke = jokesyou.getJoke('blondejokes')
	elif index == 3:
		joke = randomjoke.getJoke('blonde')
	return joke