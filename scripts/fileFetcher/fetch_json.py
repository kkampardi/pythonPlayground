import requests
from requests import HTTPError, RequestException
import gzip, json
import apt
import sys
from pprint import pprint

hi_url = 'https://udd.debian.org/how-can-i-help.json.gz'

def download_gz(hi_url):
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
                if value in packages:
                    hi_filtered.append(hi[i])
            if key == "package":
                if value in packages:
                    hi_filtered.append(hi[i])

    # print (len(hi))
    # print (len(hi_filtered))
    # print (hi_filtered)

    """ support filtering by type
    for i in range(1, len(hi_filtered)):
        for name, package in hi_filtered[i].items():
            print (name, package)
            if hi_filtered[i]['type'] == 'gift':
                print (hi_filtered[i])
    """

download_gz(hi_url)