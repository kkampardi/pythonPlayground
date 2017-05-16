# Script to scrape a URL and return list of links

import argparse
from bs4 import BeautifulSoup, SoupStrainer
from urllib.error import URLError
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen

# Scrapes all links (<a></a>) with "href" attribute set, returns unique set
def scrape_links(url):
    links = set()
    try:
        response = urlopen(url);
    except URLError as e:
        print(e.reason)
        links = None
    else:
        for a in BeautifulSoup(response, parse_only=SoupStrainer("a", href=True)).find_all("a"):
            if not bool(urlparse(a["href"]).netloc):
                link = urljoin(url, a["href"])
            else:
                link = a["href"]
            if link not in links:
                links.add(link)
    finally:
        return links

# Main
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Link scraper")
    parser.add_argument("-t", required=True, help="target URL: (format is http://somedomain.com)")
    parser.add_argument("-o", help="output file for scraped links")
    args = parser.parse_args()

    if not args.t.startswith("http"):
        print("Invalid URL format, URLs should  begin with 'http://', or 'https://'")
    else:
        result = scrape_links(args.t)
        print (result)
        if args.o:
            try:
                f = open(args.o, "w+")
            except:
                print("Error opening file")
            else:
                for r in result:
                    f.write("%s\r\n" % r)
            finally:
                f.close()
        else:
            for r in result:
                print("%s" % r)