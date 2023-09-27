from bs4 import BeautifulSoup
import requests
from time import sleep

headers = {"User-Agent": "CrookedHands/2.0 (EVM x8), CurlyFingers20/1;p"}
webpage = "https://scrapingclub.com"


def get_url():
    for page_counter in range(1, 8):

        url = f"https://scrapingclub.com/exercise/list_basic/?page={page_counter}"

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="w-full rounded border")

        for i in data:
            # name = i.find("h4").text
            # price = i.find("h5").text
            # url_image =  i.find("img", class_="card-img-top img-fluid").get("src")
            # image = f"{webpage}{url_image}"
            # print(f"{name} {price} {image}")
            card_url = webpage + i.find("a").get("href")
            yield card_url


def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(3)  # The website won't recognize the spider

        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_="my-8 w-full rounded border")

        name = data.find("h3", class_="card-title").text
        price = data.find("h4").text
        description = data.find("p", class_="card-description").text
        url_img = data.find("img", class_="card-img-top").get("src")
        image = webpage + url_img

        yield name, price, description, image
