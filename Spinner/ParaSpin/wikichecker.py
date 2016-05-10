import requests, bs4
import datetime
import string

###################################################
############ Wikipedia Page Activity ##############
###################################################

'''pages[page.title] = x'''

def WikiCheck():
	clients = ['David_Beckham', 'Kate_Winslet', 'David_Foster_Wallace']
	edits = {}
	for i in clients:
		dates = []
		'''Asking the user for input and then making a url using the standard wikipedia webpages'''

		url = 'https://en.wikipedia.org/w/index.php?title='
		url2 = '&action=history'

		pageurl = url + i + url2

		''' Grabbing the website of a user, checking it for errors and making it 
		into a BeautifulSoup object that can be searched'''
		res = requests.get(pageurl)
		res.raise_for_status()
		site = bs4.BeautifulSoup(res.text, "html.parser")

		''' Looking for the tag that contains the data information, looping through
		the information, converting it to a str and putting it in a list '''
	
		sitet = site.select('.mw-changeslist-date')
		for x in sitet:
			formatted =  x.getText()
			dates.append(str(formatted))

			y = datetime.datetime.strptime(dates[0], '%H:%M, %d %B %Y')
			now = datetime.datetime.now()

			calculation = now - y
			edits[i] = str(calculation.days)

	return edits

	'''print ' %s was last edited %s days ago' % (i, str(calculation.days))'''