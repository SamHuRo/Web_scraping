import bs4
import requests
from os import system

system('clear')

#URL of the page
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

#List of the book title with 4 or 5 stars
rating_books = []


#Loop for to go through each page of the web
for pages in range(1,51):
    #Creating soup
    url_page = url_base.format(pages)
    #Result of the request
    results = requests.get(url_page)
    #Convert rhe result
    soup = bs4.BeautifulSoup(results.text, 'lxml')
    #Select the books of the page
    books = soup.select('.product_pod')

    #Loop for each book
    for book in books:
        #Verify that has 4 or 5 stars
        if (len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0):
            #Save the title
            book_title = book.select('a')[1]['title']
            #Append the title to the list
            rating_books.append(book_title)

#Print the result of the 
for t in rating_books:
    print(t)
