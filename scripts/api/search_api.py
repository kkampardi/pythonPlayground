import requests
from requests_oauthlib import OAuth1

"""
Testing yelp search API
"""

"""
>>> from requests_oauthlib import OAuth1Session
>>> twitter = OAuth1Session('client_key',
                            client_secret='client_secret',
                            resource_owner_key='resource_owner_key',
                            resource_owner_secret='resource_owner_secret')
>>> url = 'https://api.twitter.com/1/account/settings.json'
>>> r = twitter.get(url)
"""

client_key = 'UvemK6t-sL29CBw1PHED9DHaoXE-laxvqwEi6c-vOl3rr1QYL3JNEaL6uEZDB__EboDEseDM6UJCrtdpSzrf1mfhFgOorrlmY05C_-1E2m05rS8xpJvcegQnzT1fWnYx'
client_secret = 'aRZbwJj2eUtyCIB9uaP95QXScci8QDIhnrkKwWt81BXoP2oIGfgn7uzpjCWR3Tvz'
auth = OAuth1(client_key, client_secret)
url = 'https://api.yelp.com/v3/businesses/search'
params = {
    "term": "food",
    "location": "Newport Beach",
}
r = requests.get(url, auth=auth, params=params)

print(r.text)
print(r.status_code)
