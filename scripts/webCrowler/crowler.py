from urllib.request import urlopen
from bs4 import BeautifulSoup


def crowler(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html)


    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])


crowler("http://en.wikipedia.org/wiki/Kevin_Bacon")