from bs4 import BeautifulSoup as BS
import requests as req

query = 'python'
url = "https://github.com/search?q={q}"
res = req.get(url.format(q=query))
soup = BS(res.text, 'lxml')
repositories = soup.find_all('a', class_='v-align-middle')
stars = soup.select('div.mr-3 a.Link--muted')


for i in range(0, len(repositories)):
    print('Respository: ' , repositories[i].text)
    print("Stars: ", stars[i].text[stars[i].text.find(' '):])
