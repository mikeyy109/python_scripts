#! python3
# passwordManager - An insecure password manager

PASSWORDS = {'email': 'F8dskk73h3Bsj8S', 'blog': 'nsSj7629Sab7G3l', 'other': 12345}

import sys, pyperclip

if len(sys.argv) < 2:
	print('Usage: python3 passwordManager.py [account]')
	sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard..')
else:
	print('There is no account named ' + account)