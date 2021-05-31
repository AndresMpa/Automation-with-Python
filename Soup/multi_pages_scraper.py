from bs4 import BeautifulSoup as BS
from sys import argv as ar
import requests as req
import doctest as dt
import time

def get_info_url(page, query):
    """
    This function get the information from the github respositories
    get_info_url(2, 'JS')
    ...
    """

    url = 'https://github.com/search?p={pages}&q={query}&type=Repositories'
    res = req.get(url.format(pages=page, query=query))
    soup = BS(res.text, 'lxml')
    time.sleep(1)
    return soup

def analize_info(soup):
    """
    This function print the information gotten from github
    analize_info(soup)
    ...
    """

    repositories = soup.find_all('a', class_='v-align-middle')
    stars = soup.select('div.mr-3 a.Link--muted')

    for i in range(0, len(repositories)):
        print('Respository: ' , repositories[i].text)
        print("Stars: ", stars[i].text[stars[i].text.find(' '):])

def get_repo(limit, query):
    result = 1
    while result <= limit:
        print("#########################")
        print("Pages number: ", result)
        print("#########################")
        analize_info(get_info_url(result, query))
        result += 1

dt.testmod()

if __name__ == "__main__":
    query = 'python'
    limit = 3
    if len(ar) > 1:
        query = ar[1]
    if len(ar) > 2:
        query = ar[1]
        limit = int(ar[2])

    print(ar)
    print(query, limit)

    get_repo(limit, query)
