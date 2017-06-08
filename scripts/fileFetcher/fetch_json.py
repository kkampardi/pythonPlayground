import requests
from requests import HTTPError, RequestException
import gzip, json
import apt, os
import pprint

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

    """ uncompress the tmp gz to a list"""
    with gzip.open('files/delete_me.gz', 'rb') as infile:
        for line in infile:
            data = json.loads(line.decode("utf-8"))

    #os.unlink('files/delete_me.gz')
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

    """ pripare data for render  """
    help_data = {
        "wnpp": [],
        "gift": [],
        "testing-autorm": [],
        "no-testing": [],
        "infra": [],
        "rfs": []
    }

    for item in hi_filtered:
       if item["type"] == "wnpp":
                # puts " - #{r['source']} - https://bugs.debian.org/#{r['wnppbug']} - #{wnpptype(r['wnpptype'])}"
                help_data["wnpp"].append(item)
       elif item["type"] == "gift":
                # puts " - #{r['package']} - https://bugs.debian.org/#{r['bug']} - #{r['title']}"
                help_data["gift"].append(item)
       elif item["type"] == "testing-autorm":
                puts
                help_data["testing-autorm"].append(item)
       elif item["type"] == "rfs":
                #puts " - #{r['source']} - https://bugs.debian.org/#{r['id']} - #{r['title']}"
                help_data["rfs"].append(item)
       elif item["type"] == "no-testing":
                # puts " - #{r['package']} - https://tracker.debian.org/pkg/#{r['id']}"
                help_data["no-testing"].append(item)
       elif item["type"] == "infra":
                help_data["infra"].append(item)

    # print(len(hi_filtered))

    print("Original hi %s" % (len(hi)))
    print("Filtered hi %s " % (len(hi_filtered)))

    for key,value in help_data.items():
        for item in value:
            if key == "wnpp":
                #puts " - #{r['source']} - https://bugs.debian.org/#{r['wnppbug']} - #{wnpptype(r['wnpptype'])}"
                print('Packages where help is needed, including orphaned ones (from WNPP):\n' )
                print("- {} - https://bugs.debian.org/#{} - #{} ".format(item['source'], item['wnppbug'], item['wnpptype']))
            if key == "gift":
                #puts"- #{r['package']} - https://bugs.debian.org/#{r['bug']} - #{r['title']}"
                print("- {} - https://bugs.debian.org/#{} - #{} ".format(item["package"], item["bug"], item['title']))
            if key == "infra":
                # puts" - #{r['package']} - https://bugs.debian.org/#{r['bug']} - #{r['title']}"
                print("- {} - https://tracker.debian.org/pkg/#{} - # {}".format(item['package'], item['bug'], item['source']))
                print( 'Bugs affecting Debian infrastructure (tagged \'newcomer\'):' 'New bugs affecting Debian infrastructure (tagged \'newcomer\'):')
            if key == "no-testing":
                # puts " - #{r['package']} - https://tracker.debian.org/pkg/#{r['source']}"
                print("- {} - https://tracker.debian.org/pkg/#{}".format(item['package'], item['source']))
            if key == "testing-autorm":
                #puts " - #{r['source']} - https://tracker.debian.org/pkg/#{r['source']} - removal on #{Time.at(r['removal_time']).to_date.to_s}#{bugs}"
                print("Packages going to be removed from Debian \'testing\' (the maintainer might need help):' : 'New packages going to be removed from Debian \'testing\' (the maintainer might need help):")
                print("- {} - https://tracker.debian.org/pkg/#{r['source']} - removal on {} - #{bugs} - # {}".format(item['source'], item['removal_time'], item['bugs']))
            if key == "rfs":
                # puts " - #{r['source']} - https://bugs.debian.org/#{r['id']} - #{r['title']}"
                print('Packages waiting for sponsorship (reviews/tests are also useful): :New packages waiting for sponsorship (reviews/tests are also useful):')
                print("- {} - https://bugs.debian.org/#{} - # {}".format(item['source'], item['id'], item['title']))



get_help_items()