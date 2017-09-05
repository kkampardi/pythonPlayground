import argparse
from crawler import Crawler

# init parameters
parser = argparse.ArgumentParser(description="Simple and unlimited sitemap generator")
parser.add_argument('--url', action="store", default="", help="e.g. http://kkabardi.me")
parser.add_argument('--exclude', action="store", default="", help="Exclude urls" )
parser.add_argument('--no-verbose', action="store_true", default="", help="Prints verbose output")
parser.add_argument('--output', action="store", default="sitemap.xml", help="Shows the output for the file path")

# parse parameters
args = parser.parse_args()
url = args.url.rstrip("/")
links_fetched = []

# initializeing crawler
crawler = Crawler(url, exclude=args.exclude, no_verbose=args.no_verbose);

# fetch links
links = crawler.start()


# write into file
with open(args.output, "w") as file:

	file.write('<?xml version="1.0" encoding="UTF-8"?>\n\t<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

	for link in links:
		file.write("\n\<url>\n<loc>\n{0}{1}/\n</loc>\n</url>".format(url, link))

	file.write('</urlset>')