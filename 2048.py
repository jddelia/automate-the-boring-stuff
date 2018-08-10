#! /usr/bin/python3

""" This program uses selenium to play a
    game of 2048 through automation. """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

window = webdriver.Chrome()
window.get('https://gabrielecirulli.github.io/2048/')
game = window.find_element_by_tag_name('body')

while True:
    game.send_keys(Keys.UP)
    game.send_keys(Keys.RIGHT)
    game.send_keys(Keys.DOWN)
    game.send_keys(Keys.LEFT)
