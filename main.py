import requests
from bs4 import BeautifulSoup
import json

url = 'https://scrapingclub.com/exercise/list_basic/?page='

data_dresses = {}
for j in range(1, 7):
    response = requests.get(url + str(j) + '=')

    with open(f'page/page_{j}.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

    with open(f'page/page_{j}.html', 'r', encoding='utf-8') as file:
        page_data = file.read()

    soup = BeautifulSoup(page_data, 'lxml')

    prices = soup.find_all('h5')
    dresses = soup.find_all('h4')

    for i in range(len(prices)):
        price = prices[i].text[1:-1]
        dress = dresses[i].text

        if dress not in data_dresses:
            data_dresses[dress] = [price]
        else:
            data_dresses[dress] = data_dresses[dress] + [price]

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data_dresses, file, ensure_ascii=False, indent=4)
