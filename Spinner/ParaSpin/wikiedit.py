import requests 
import datetime
import string
import wikipedia
'''No BeautifulSoup needed as Wikipedia's own API does the work.'''
###################################################
############ Wikipedia Error Finder ###############
###################################################



''' List of errors to be searched for'''
def Wiki():
	errors = ['could\'ve','would\'ve','should\'ve',' .','can\'t', 'aren\'t', 'didn\'t', 'don\'t', 'doesn\'t', 'it\'s' ]
	pages = {}

	'''Loops 'range' amount of times through random articles, and compares
	content with list or errors, returning found errors, on pages
	that do not work due to DisambiguationError, it ignores and continues
	to cycle'''
	for i in range(19):
		try:
			page = wikipedia.WikipediaPage(title=wikipedia.random(pages=1))
			for x in errors:
				if x in page.content:
					pages[page.title] = x
		except wikipedia.exceptions.DisambiguationError:
			print 'Multiple entries found'

	return pages