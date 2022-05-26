from bs4 import BeautifulSoup
import requests
import openpyxl

url = 'https://tinyurl.com/usx53k33'
page = requests.get(url)



soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('article', class_='list-card')

# prices = soup.find_all('div', class_='list-card-price')

# for i in range(len(prices)):
    # print(prices[i].text)
print(lists)