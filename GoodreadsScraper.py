# GoodreadsScraper.py
# reccomended run environment: python GoodreadsScraper.py > ___OUTFILE___.csv
# Author: Julien Legault

import urllib.request
from bs4 import BeautifulSoup

#Change this to the link to the list of books
#Note it ends with ?page=
___LISTLINK___ = 'https://www.goodreads.com/list/show/74439.YA_Novels_of_2018?page='

#Change this to the number of pages on the list
___NUMBERPAGES___ = 11

#Possible itemprops: ratingValue, bookFormat, numberOfPages, name (author's name)
___ITEMPROP___ = "numberOfPages"

# innerSoup(href)
# href: A string contating the extention to the book page
# href should be of the form '/book/show/___BOOK_TITLE___'
def innerSoup(href):
	completeHref = "https://www.goodreads.com" + href
	innerPage = urllib.request.urlopen(completeHref)
	insideSoup = BeautifulSoup(innerPage, "html.parser")
	#Haven't run across null books, but is possible
	if insideSoup is not None:
		title = insideSoup.find('h1', {"id": "bookTitle"})
		itemToFind = insideSoup.find('span', {"itemprop": ___ITEMPROP___})
		#removes unwanted commas to produce a csv file. quotes are already handled.
		titleText = title.text[7:-1].replace(',', '')
		#Many books do not have many of the itemprops, if not just the title is returned.
		if itemToFind is not None:
			result = titleText + ", " + itemToFind.text
		else:
			result = titleText + ","
		print(result)

# outerSoup(href)
# href a string contating the link to the list, ex.  ___LISTLINK___
# loops through each book on the page, calling innerSoup on each one
def outerSoup(href):
	page = urllib.request.urlopen(href)
	soup = BeautifulSoup(page, "html.parser")
	myA = soup.findAll("a", {"class": "bookTitle"})
	for link in myA:
		innerSoup(link['href'])

#main loop, just goes through every page calling outerSoup on that page
for i in range(1, ___NUMBERPAGES___):
	pageConcat = ___LISTLINK___ + str(i)
	outerSoup(pageConcat)
