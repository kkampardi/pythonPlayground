#! python3
#pw.py - An insecure password locker program

PASSWORDS = {
    'gmail': '1234',
    'blog': 'test'
    }


import sys, pyperclip
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
from getpass import getpass

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

# handle arguments
account = sys.argv[1] # first argument is the account name

if account in PASSWORDS:
    print (account)
    pyperclip.copy(PASSWORDS[account])
    print ('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named  '+ account)
