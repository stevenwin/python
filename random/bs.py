from bs4 import BeautifulSoup
import requests

#fm = requests.get("http://fightmetric.com/statistics/fighters")

with open("fm.html") as soup_file:
	soup_fm = BeautifulSoup(soup_file, "html5lib")

fm_tbody = soup_fm.find("tbody")
fm_table = soup_fm.find("table", {"class": "b-statistics__table"})
fm_tr = fm_tbody.find_all("tr", {"class": "b-statistics__table-row"})
fm_td = fm_table.find_all("td", {"class": "b-statistics__table-col"})

for tr in fm_tr:
	print "First Name: " + tr.td.get_text().strip()










"""for book_title in all_book_titles:
	book_title_span = book_title.span
	print("Title Name is :"+book_title_span.a.string)

	published_date = book_title.find_next("div",class_="views-field-field-date-of-publication-value")
	print("Published Date is :"+published_date.span.string)

	price = book_title.find_next("div",class_="views-field-sell-price")
	print("Price is :"+price.span.string)"""