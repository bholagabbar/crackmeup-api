
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

whichSite = randint(1,2)
if whichSite == 1:
	print jokesDotCCDotcom()
	print "\nSource - jokes.cc.com"

elif whichSite == 2:
	print jokesYouDotcom()
	print "\nSource - jokesyou.com"

else:
	print randomjokesDotcom()
