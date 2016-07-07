import random

import websites.jokes_dotcc.scrape as jokescc
import websites.randomjoke_dotcom.scrape as randomjoke

def getRandomJoke():
	index = random.randint(*(1, 2))
	if index == 1:
		joke = jokescc.getJoke('dirty')
	elif index == 2:
		joke = randomjoke.getJoke('dirty')
	return joke