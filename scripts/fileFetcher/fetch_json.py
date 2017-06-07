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
                data = json.loads(line.decode("utf-8"))
    return data

def get_help_items():

    hi = get_data(hi_url)

    """ Get system installed packages  """
    cache = apt.Cache()
    system_packages = []
    for pkg in cache:
        if cache[pkg.name].is_installed:
            system_packages.append(pkg.name)


    """ Filter the list of help items against the system installed packages list """
    hi_filtered = []
    for i in range(1, len(hi)):
        for key, value in hi[i].items():
            if key == "packages":
                for package in value:
                    if package in system_packages:
                        hi_filtered.append(hi[i])
            elif key == "package":
                if value in system_packages:
                    hi_filtered.append(hi[i])

    print(len(hi))
    print(len(hi_filtered))

    """ display the filtered data related info """
    for item in hi_filtered:
        if item["type"] == "wnpp":
            # puts " - #{r['source']} - https://bugs.debian.org/#{r['wnppbug']} - #{wnpptype(r['wnpptype'])}"
            print("- {} - #https://bugs.debian.org/#{} - #bug type {} ".format(item['source'], item['wnppbug'], item['wnpptype']))
        elif item["type"] == "gift":
            # puts " - #{r['package']} - https://bugs.debian.org/#{r['bug']} - #{r['title']}"
            print("- {} - https://bugs.debian.org/#{} - #{} ".format(item['package'], item['bug'],
                                                                           item['title']))
        elif item["type"] == "testing-autorm":
            puts
            " - #{r['source']} - https://tracker.debian.org/pkg/#{r['source']} - removal on #{Time.at(r['removal_time']).to_date.to_s}#{bugs}"
            print("- {} - https://bugs.debian.org/#{} - #{} ".format(item['package'], item['bug'],
                                                                    item['title']))
        elif item["type"] == "rfs":
            #puts " - #{r['source']} - https://bugs.debian.org/#{r['id']} - #{r['title']}"
            print("- #{} - https://bugs.debian.org/#{} - #{} ".format(item['source'], item['id'],
                                                                   item['title']))
        elif item["type"] == "no-testing":
            # puts " - #{r['package']} - https://tracker.debian.org/pkg/#{r['id']}"
            print("- {} - https://bugs.debian.org/#{} ".format(item['package'], item['source']))
        elif item["type"] == "infra":
            pass

get_help_items()