import requests
from requests import HTTPError, RequestException
import gzip, json
import apt
import sys
from pprint import pprint

hi_url = 'https://udd.debian.org/how-can-i-help.json.gz'


def get_data(hi_url):
    """ get the gz and store it to a temporary file"""
    try:
        req = requests.get(hi_url, stream=True)
    except RequestException as e:
        print(e.reason)

    """ store the gz in a temorary file """
    with open('files/delete_me.gz', 'wb') as handle:
        for block in req.iter_content(1024):
            handle.write(block)

    """ uncompress the tmp gz to a JSON tmp file"""
    with gzip.open('files/delete_me.gz', 'rb') as infile:
        with open('files/output.json', 'wb') as outfile:
            for line in infile:
                outfile.write(line)
                hi = json.loads(line.decode("utf-8"))

    return hi

def download_gz():

    hi = get_data(hi_url)

    """ get system installed packages  """
    cache = apt.Cache()
    packages = []
    for pkg in cache:
        if cache[pkg.name].is_installed:
            packages.append(pkg.name)


    """ filter the hi list of dicts so only installed packages remain  """
    hi_filtered = []
    for i in range(1, len(hi)):
        for key, value in hi[i].items():
            if key == "packages":
                print (key, value)

    for i in range(1, len(hi_filtered)):
        for key, value in hi_filtered[i].items():
                pass


download_gz()