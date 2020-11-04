from bs4 import BeautifulSoup
import requests


def getDeputies():
    URL = 'http://duma.gov.ru/duma/deputies/7/'

    result = requests.get(URL)
    soup = BeautifulSoup(result.text)
    return soup.find_all('li', {"class": "list-persons__item"})


def transpateToEnglish(payload="q=Hello%2C%20world!&source=ru&target=en"):
    url = "https://rapidapi.p.rapidapi.com/language/translate/v2"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept-encoding': "application/gzip",
        'x-rapidapi-key': "49c15c9d35msh91b37b84e0b260dp102d00jsn7d79df5b6a6e",
        'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text


def main():
    ebaniDeputi = getDeputies()

    for num, dep in enumerate(ebaniDeputi, start=1):
        aTag = dep.find('a', {"class": "person__title__link"})
        name = str(num) + ". " + aTag.find('strong').text + \
            " " + aTag.find("span").text
        link = dep.find('a', {"class": "person__title__link"})['href']

        print(name)
        print("Ссылка: http://duma.gov.ru{}".format(link))
        print("\n")


if __name__ == "__main__":
    main()
