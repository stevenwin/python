from bs4 import BeautifulSoup

with open("fm.html") as fm_file:
	fm_soup = BeautifulSoup(fm_file, "html5lib")

tag_tbody = fm_soup.find("tbody")
tag_tr = tag_tbody.find_all("tr", {"class": "b-statistics__table-row"})

for tr in tag_tr:
	td = tr.find("td")
	try:
		print tr.td.a.get("href")
	except AttributeError:
		pass