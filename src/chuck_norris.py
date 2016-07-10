import random

import websites.jokesyou_dotcom.scrape as jokesyou
import websites.randomjoke_dotcom.scrape as randomjoke

def getRandomJoke():
	joke = jokesyou.getJoke('chucknorrisjokes')
	return joke