import xlsxwriter
from scraping_of_all_webpages import array


def writer(given_parameter):
    # Create the xls file
    file = xlsxwriter.Workbook(r"C:\Users\agmat\PycharmProjects\pythonProject\DataScraper\converted.xlsx")
    # Create page
    page = file.add_worksheet("products")

    row = 0
    col = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)

    for item in given_parameter():
        page.write(row, col, item[0])  # name
        page.write(row, col+1, item[1])  # price
        page.write(row, col+2, item[2])  # description
        page.write(row, col+3, item[3])  # image
        row += 1

    file.close()


writer(array)
