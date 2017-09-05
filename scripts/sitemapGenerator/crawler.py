import urllib.request
import re


class Crawler:
    def __init__(self, url, exclude=None, no_verbose=False):
        self.url = url
        self.exclude = exclude
        self.no_verbose = no_verbose
        self.links_fetched = []
        self.visited_links = []

    def start(self):
        self.crawl(self.url)

        return self.links_fetched

    def crawl(self, url):
        if not self.no_verbose:
            print(url)

        response = urllib.request.urlopen(url)
        page = str(response.read())

        pattern = '<a [^>]*href=[\'|"](.*?)[\'"].*?>'

        links_fetched = re.findall(pattern, page)
        links = []

        for link in links_fetched:
            self.add_url(link, links, self.exclude)
            self.add_url(link, self.links_fetched)

        for link in links:
            if link not in self.visited_links:
                self.visited_links.append(link)
                self.crawl("{0}{1}".format(self.url, link))

    def add_url(self, link, link_list, exclude_pattern=None):
        link = link.rstrip("/")

        if link:
            url_parts = link.split("://")

            not_in_list = link not in link_list
            is_internal_link = link[0] is "/" or link.split("/")[0] is self.url.split("/")[0]
            excluded = False

            if exclude_pattern:
                excluded = re.search(exclude_pattern, link)

            if not_in_list and is_internal_link and not excluded:
                link_list.append(link)