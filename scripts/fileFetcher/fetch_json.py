import requests
from requests import HTTPError
import gzip, json
import apt
import sys
from pprint import pprint
from collections import OrderedDict

source_url = 'https://udd.debian.org/how-can-i-help.json.gz'

def download_gz(url):
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


    # get system apt packages
    cache = apt.Cache()

    system_pkg = []
    for pkg in cache:
        #print(pkg)
        system_pkg.append(pkg)


    fb_pkg = []
    for i in range(1,len(json_data)):
        for name, subdict in json_data[i].items():
            if name == "package":
                print json_data[i]["package"]
                fb_pkg.append(json_data[i]["package"].decode("utf8"))
            elif name == "packages":
                for package in json_data[i]["packages"]:
                    print package

    #common = set(system_pkg).intersection(fb_pkg)
    #print (system_pkg)
    #print (fb_pkg)
    #print (common)


download_gz(source_url)