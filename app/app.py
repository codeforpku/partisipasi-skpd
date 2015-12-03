#/usr/bin/python

from urllib2 import urlopen
from bs4 import BeautifulSoup as bs

def fetchdata():
   soup = bs(urlopen('https://www.riau.go.id/home/skpd/partisipasi').read())
   data = [x.text.encode('ascii') for x in soup.find_all('td')]
   skpd = [data[x] for x in range(len(data)) if x%2 == 0]
   skor = [data[x] for x in range(len(data)) if x%2 == 1]
   data_readable = dict(zip(skpd, skor))
   return data_readable

