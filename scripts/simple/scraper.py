from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
        try:
            html = urlopen(url)
        except HTTPError as e:
            return None

        try:
            bsObj = BeautifulSoup(html.read(), "lxml")
            title = bsObj.body.h1
        except AttributeError as e:
            return None

        return title


def get_html(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("There was an error opening this url")
        return None

    try:
        bsObj = BeautifulSoup(html)
    except AttributeError:
        print("There was an error reading this data")
        return None

    return bsObj


data = get_html("http://www.pythonscraping.com/pages/warandpeace.html")

namelist = data.findAll("span", {"class":"green"})


pycat_data = get_html("http://kkabardi.me")

alist = pycat_data.findAll("article", {"class":"post"})

for a in alist:
    print(a.get_text())


wiki_den = get_html("https://el.wikipedia.org/wiki/%CE%9C%CE%B9%CE%BC%CE%AE_%CE%9D%CF%84%CE%B5%CE%BD%CE%AF%CF%83%CE%B7")

contextlist = wiki_den.findAll("span", {"class":"toctext"})

for context in contextlist:
    print(context.get_text())
