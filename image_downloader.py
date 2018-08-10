#! /usr/bin/python3

""" This program downloads searched images from
    photo hosting websites. """

import sys
import requests
from selenium import webdriver
import bs4

flickr = requests.get('https://www.flickr.com/search/?text=dogs')
flickr_soup = bs4.BeautifulSoup(flickr.text, "lxml")

images = flickr_soup.select('')

print(images)
