# Grab all fighter's URLs and stick into list

from bs4 import BeautifulSoup
import requests

#with open("fm.html") as fm_file:
#	fm_soup = BeautifulSoup(fm_file, "html5lib")
fighters_link = [
"http://fightmetric.com/statistics/fighters?char=a&page=all",
"http://fightmetric.com/statistics/fighters?char=b&page=all",
"http://fightmetric.com/statistics/fighters?char=c&page=all",
"http://fightmetric.com/statistics/fighters?char=d&page=all",
"http://fightmetric.com/statistics/fighters?char=e&page=all",
"http://fightmetric.com/statistics/fighters?char=f&page=all",
"http://fightmetric.com/statistics/fighters?char=g&page=all",
"http://fightmetric.com/statistics/fighters?char=h&page=all",
"http://fightmetric.com/statistics/fighters?char=i&page=all",
"http://fightmetric.com/statistics/fighters?char=j&page=all",
"http://fightmetric.com/statistics/fighters?char=k&page=all",
"http://fightmetric.com/statistics/fighters?char=l&page=all",
"http://fightmetric.com/statistics/fighters?char=m&page=all",
"http://fightmetric.com/statistics/fighters?char=n&page=all",
"http://fightmetric.com/statistics/fighters?char=o&page=all",
"http://fightmetric.com/statistics/fighters?char=p&page=all",
"http://fightmetric.com/statistics/fighters?char=q&page=all",
"http://fightmetric.com/statistics/fighters?char=r&page=all",
"http://fightmetric.com/statistics/fighters?char=s&page=all",
"http://fightmetric.com/statistics/fighters?char=t&page=all",
"http://fightmetric.com/statistics/fighters?char=u&page=all",
"http://fightmetric.com/statistics/fighters?char=v&page=all",
"http://fightmetric.com/statistics/fighters?char=w&page=all",
"http://fightmetric.com/statistics/fighters?char=y&page=all",
"http://fightmetric.com/statistics/fighters?char=x&page=all",
"http://fightmetric.com/statistics/fighters?char=z&page=all"
]

fighter_link = []

# FUNCTION - Run through all fighter top level URLs and grab the individual fighter URLs
def get_fighter_url(url):
	fm = requests.get(url)
	fm_soup = BeautifulSoup(fm.text)

	tag_tbody = fm_soup.find("tbody")
	tag_tr = tag_tbody.find_all("tr", {"class": "b-statistics__table-row"})

	for tr in tag_tr:
		td = tr.find("td")
		try:
			fighter_link.append(tr.td.a.get("href"))
		except AttributeError:
			pass

	return fighter_link

# Grab all the individual fighter URLs and stick it in a list
for link in fighters_link:
	get_fighter_url(link)

for link in fighter_link:
	print link