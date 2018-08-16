#! /usr/bin/python3

""" This program allows user to send email from the
    command line. """

import sys
from selenium import webdriver
import bs4

email = webdriver.Chrome()
email.get('http://google.com/mail')

account = email.find_element_by_name('identifier')
account.send_keys(sys.argv[1])
next = email.find_element_by_id('identifierNext')
next.click()

pwrd = email.find_element_by_name('password')
pwrd.send_keys(sys.argv[2])
next = email.find_element_by_id('passwordNext')
next.click()
