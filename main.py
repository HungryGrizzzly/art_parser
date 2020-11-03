from bs4 import BeautifulSoup
import requests

URL = 'http://duma.gov.ru/duma/deputies/7/'

result = requests.get(URL)

soup = BeautifulSoup(result.text)

ebaniDeputi = soup.find_all('li', {"class": "list-persons__item"})

for dep in ebaniDeputi:
    aTag = dep.find('a', {"class": "person__title__link"})
    name = aTag.find('strong').text + " " + aTag.find("span").text
    link = dep.find('a', {"class": "person__title__link"})['href']

    print(name)
    print("Ссылка: http://duma.gov.ru{}".format(link))
    print("\n")
