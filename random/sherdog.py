from bs4 import BeautifulSoup
import requests, urllib

#fm = requests.get("http://www.sherdog.com/stats/fightfinder?association=&weightclass=Bantamweight&SearchTxt=&page=1")

sherdog = urllib.urlopen('http://www.sherdog.com/stats/fightfinder?association=&weightclass=Bantamweight&SearchTxt=&page=1').read()
soup = BeautifulSoup(sherdog)
print type(soup)