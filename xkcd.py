#! /usr/bin/python3

# This program downloads xkcd comics.

import requests, bs4

url = 'http://xkcd.com/'
page = requests.get(url)
x = 0

while x < 5:
    pageSoup = bs4.BeautifulSoup(page.text)
    print('\n\n')
    image = pageSoup.select('img')

    print('Downloading... http:'  + image[1].get('src'))
    res = requests.get('http:' + image[1].get('src'))
    with open(image[1].get('src')[23:], 'wb') as fp:
        for chunk in res.iter_content(100000):
            fp.write(chunk)

    prev = pageSoup.select('li a')
    page = requests.get(url + prev[6].get('href'))
    page.raise_for_status()
    x += 1
