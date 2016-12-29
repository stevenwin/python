from bs4 import BeautifulSoup
import urllib
import json

#fm = requests.get("http://www.sherdog.com/stats/fightfinder?association=&weightclass=Bantamweight&SearchTxt=&page=1")

# try:
for x in range(0, 3):
	try:
		sherdog = urllib.urlopen('http://www.sherdog.com/stats/fightfinder?association=&weightclass=Bantamweight&SearchTxt=&page='+str(x)).read()
		soup = BeautifulSoup(sherdog, "html5lib")
		data = {}

		body = soup.find("table", {"class": "fightfinder_result"})

		for link in body.find_all('a'):
			data[link.get_text()] = link.get('href')

		for k, v in data.items():
			print k + ': ' + v
	except:
		pass

json_str = json.dumps(data)

json_data = json.loads(json_str)

print type(json_data)
for key, v in json_data.items():
	print key+'(key )'+v+'(value)'

# except (AttributeError):
# 	pass