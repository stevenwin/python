from bs4 import BeautifulSoup
import requests
import json

#fm = requests.get("http://fightmetric.com/statistics/fighters")

with open("fm.html") as soup_file:
	soup_fm = BeautifulSoup(soup_file, "html5lib")

fm_tbody = soup_fm.find("tbody")
fm_table = soup_fm.find("table", {"class": "b-statistics__table"})
fm_tr = fm_tbody.find_all("tr", {"class": "b-statistics__table-row"})
fm_td = fm_table.find_all("td", {"class": "b-statistics__table-col"})

fname = []
#Grab all the statistics

# Put Data into JSON Object
data = {}




for tr in fm_tr:
<<<<<<< HEAD

	fname = tr.td
	lname = fname.find_next("td")
=======
	fname = tr.td.get_text()
	"""lname = fname.find_next("td")
>>>>>>> c84080abdcabd27ecea971193191750ad6eb1fea
	nickname = lname.find_next("td")
	height = nickname.find_next("td")
	weight = height.find_next("td")
	reach = weight.find_next("td")
	stance = reach.find_next("td")
	win = stance.find_next("td")
	lose = win.find_next("td")
	draw = lose.find_next("td")
	
	data['fname'] = tr.td
	data['lname'] = fname.find_next("td")
	data['reach'] = weight.find_next("td")
	json.data = json.dumps(data)

	print("First Name: "+fname.get_text().strip())
	print("Last Name: "+lname.get_text().strip())
	print("Nickname: "+nickname.get_text().strip())
	print("Height: "+height.get_text().strip())
	print("Reach: "+reach.get_text().strip())
	print("")"""

for name in fname:
	print name
#Grab Fighter URLs
<<<<<<< HEAD
fighterLink = list()
for link in fm_table.find_all("a", href=True):
	fighterLink.append(link['href'])
=======
#fighterLink = []
#for link in fm_table.find_all("a", href=True):
#	print link['href']
>>>>>>> c84080abdcabd27ecea971193191750ad6eb1fea

print fighterLink[0]


"""for book_title in all_book_titles:
	book_title_span = book_title.span
	print("Title Name is :"+book_title_span.a.string)

	published_date = book_title.find_next("div",class_="views-field-field-date-of-publication-value")
	print("Published Date is :"+published_date.span.string)

	price = book_title.find_next("div",class_="views-field-sell-price")
	print("Price is :"+price.span.string)"""