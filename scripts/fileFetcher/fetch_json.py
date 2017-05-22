import requests
from requests import HTTPError
import gzip, json
import apt
import sys

source_url = 'https://udd.debian.org/how-can-i-help.json.gz'

def download_gz(source_url):
    """ get the gz and store it to a temporary file"""
    try:
        req = requests.get(source_url, stream=True)
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
                json_data = json.loads(line.decode("utf-8"))

    # store help items in a python dict
    fb_pkg = {}
    for i in range(1, len(json_data)):
        for name, subdict in json_data[i].items():
            if name == "package":
                # print json_data[i]["package"]
                fb_pkg.append(json_data[i]["package"])
            elif name == "packages":
                for package in json_data[i]["packages"]:
                    fb_pkg.append(package)


    cache = apt.Cache()
    system_pkg = []
    for pkg in cache:
        if cache[pkg.name].is_installed:
            compare(pkg.name, fb_pkg)


def compare(package_name, help_items):
    for item in help_items:
        if package_name == item:
            print ("%s is equal to %s!" %( package_name,item))

download_gz(source_url)