import urllib.request
from bs4 import BeautifulSoup
def innerSoup(href):
	completeHref = "https://www.goodreads.com" + href
	innerPage = urllib.request.urlopen(completeHref)
	insideSoup = BeautifulSoup(innerPage, "html.parser")
	if insideSoup is not None:
		title = insideSoup.find('h1', {"id": "bookTitle"})
		pages = insideSoup.find('span', {"itemprop": "numberOfPages"})
		titleText = title.text[7:-1].replace(',', '')
		if pages is not None:
			result = titleText + ", " + pages.text
		else:
			result = titleText + ","
		print(result)
	else:
		return ""

def outerSoup(href):
	page = urllib.request.urlopen(href)
	soup = BeautifulSoup(page, "html.parser")
	myA = soup.findAll("a", {"class": "bookTitle"})
	outerResult = ""
	for link in myA:
		#outerResult += 
		innerSoup(link['href'])
	return outerResult

output = ""

for i in range(1, 11):
	pageConcat = 'https://www.goodreads.com/list/show/74439.YA_Novels_of_2018?page=' + str(i)
	#output += 
	outerSoup(pageConcat)

#print(output)
