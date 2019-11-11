# goodreadsScraper
Scrapes whatever info is needed from a Goodreads list.

Run instructions:
It is reccomended to run as:
    python3 GoodreadsScraper.py > ___OUTPUTFILE___.csv

By default scrapes title and page number from 'YA Novels of 2018'
Can be changed by changing the following varables:
    ___LISTLINK___ (a link to the list to scrape)
    ___NUMBERPAGES___ (how many pages that list has)
    ___ITEMPROP___ (what to scrape other then title)
    
Possible ___ITEMPROP___ values: ratingValue, bookFormat, numberOfPages, isbn, name
name is the author's name.
