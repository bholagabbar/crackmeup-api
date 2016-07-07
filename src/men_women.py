import random

import websites.jokes_dotcc.scrape as jokescc
import websites.jokesyou_dotcom.scrape as jokesyou
import websites.randomjoke_dotcom.scrape as randomjoke

def getRandomJoke():
	index = random.randint(*(1, 3))
	joke = ''
	if index == 1:
		joke = jokescc.getJoke('men-women')
	elif index == 2:
		index2 = random.randint(*(1, 2))
		if index2 == 1:
			joke = jokesyou.getJoke('womenjokes')
		else:
			joke = jokesyou.getJoke('menjokes')
	elif index == 3:
		joke = randomjoke.getJoke('couples')
	return joke