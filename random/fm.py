from bs4 import BeautifulSoup
import Requests

from open(fm.html) as fm_file:
	fm_soup = BeautifulSoup(fm_file, "hmtl5lib")

tag_tbody = fm_soup.find("tbody")
