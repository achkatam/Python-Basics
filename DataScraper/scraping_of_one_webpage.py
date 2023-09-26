import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/?page=1"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

# For a single result
# data = soup.find("div", class_="w-full rounded border")
# # print(data)
#
# # Find the name of the product
# name = data.find("h4").text
# # print(name)  # returns just the name of the product
#
# # Find the price of the product
# price = data.find("h5").text
# # print(price)
#
# # Get the image of tag and class
# url_image = data.find("img", class_="card-img-top img-fluid").get("src")
# # print(url_image)  # returns the image link
#
# image = "https://scrapingclub.com" + url_image
# # print(image)

# Multiple results from certain page
data = soup.find_all("div", class_="w-full rounded border")

index_of_product = 1

for i in data:
    name = i.find("h4").text
    price = i.find("h5").text
    url_image = i.find("img", class_="card-img-top img-fluid").get("src")
    image = "https://scrapingclub.com" + url_image
    print(index_of_product)
    index_of_product += 1
    print(f"{name}  {price}  {image}")
