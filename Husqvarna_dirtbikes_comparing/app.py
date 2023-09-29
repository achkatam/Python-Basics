import requests
from bs4 import BeautifulSoup, SoupStrainer
import xlsxwriter

url2021 = "https://www.motorcycle.com/specs/husqvarna/off-road/2021/fx/450/detail.html"
url2019 = "https://www.motorcycle.com/specs/husqvarna/off-road/2019/fx/450/detail.html"

response = requests.get(url2021)
response2 = requests.get(url2019)

soup = BeautifulSoup(response.text, "lxml")  # This is the html parser
soup2 = BeautifulSoup(response2.text, "lxml")  # This is the html parser

data = soup.find_all("div", class_="vs-specs-table-row")
data2 = soup2.find_all("div", class_="vs-specs-table-row")

workbook = xlsxwriter.Workbook('dirtbike_comparer.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column("A:A", 30)
worksheet.set_column("B:B", 50)
worksheet.set_column("C:C", 30)
worksheet.set_column("D:D", 50)

row = 0
col = 0

for item in data:
    kvp_key = item.find("div", class_="spec-key bold").text.replace(" ", "").replace("\n", "")
    kvp_value = item.find("div", class_="spec-value").text.replace(" ", "").replace("\n", "")
    worksheet.write(row, col, kvp_key)
    worksheet.write(row, col + 1, kvp_value)
    row += 1

row = 0

for item in data2:
    kvp_key = item.find("div", class_="spec-key bold").text.replace(" ", "").replace("\n", "")
    kvp_value = item.find("div", class_="spec-value").text.replace(" ", "").replace("\n", "")
    worksheet.write(row, col + 2, kvp_key)
    worksheet.write(row, col + 3, kvp_value)
    row += 1

workbook.close()
