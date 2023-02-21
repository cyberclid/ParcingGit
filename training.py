import requests
from bs4 import BeautifulSoup
for count in range(1,8):
    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    datas = soup.findAll('div', class_='col-lg-4 col-md-6 mb-4')
    for data in datas:
        name = data.find('h4', class_='card-title').text
        price = data.find('h5').text
        url_img = 'https://scrapingclub.com' + data.find('img',class_='card-img-top img-fluid').get('src')
        print(name + price, url_img, sep='\n')
