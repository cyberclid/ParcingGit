from typing import List, Any

import requests
from bs4 import BeautifulSoup
url = 'https://new-science.ru/category/cifrovye-tehnologii/'
page = requests.get(url)
filteredNews = []
soup = BeautifulSoup(page.text, "html.parser")
allNews = soup.findAll('p', class_="post-excerpt")
print(*allNews)

