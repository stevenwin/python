#! python3
# mapit.py - Launches a map in the browser using an address
# from the command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	# Get address from the command line
	address = ' '.join(sys.argv[1:]) #sys.argv returns a list
	# list is like [mapit, 4471, fraser, st], so we slice out mapit and join others
else:
	# Get address from clipboard
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

