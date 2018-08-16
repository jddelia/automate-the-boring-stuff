# This program launches Google Maps to find address on clipboard

import sys, webbrowser, pyperclip

def mapit():
    if len(sys.argv) > 1:
        address = ' '.join(sys.argv[1:])
    else:
        address = pyperclip.paste()

    webbrowser.open('https://www.google.com/maps/place/' + address)

mapit()
