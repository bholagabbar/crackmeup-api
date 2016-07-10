import blond, dark, dirty, gross, men_women, walks_into_a_bar, yo_mama, chuck_norris, random_joke

def trigger(category):
	switcher = {
		"Blond" : blond.getRandomJoke(),
		"Dark" : dark.getRandomJoke(),
		"Dirty" : dirty.getRandomJoke(),
		"Gross" : gross.getRandomJoke(),
		"Gender" : men_women.getRandomJoke(),
		"Walks into a bar" : walks_into_a_bar.getRandomJoke(),
		"Yo mama": yo_mama.getRandomJoke(),
		"Chuck norris": chuck_norris.getRandomJoke(),
		"Random": random_joke.getJoke(),
	}
	return switcher.get(category, "nothing")