#! /usr/bin/python3

# This program creates a dictionary of 2010 Census Tract data.

import openpyxl
import os
import pprint

os.chdir('/home/jddelia/python/automate/chap12/')

census_book = openpyxl.load_workbook('censuspopdata.xlsx')
census_sheet = census_book.get_sheet_by_name('Population by Census Tract')
census_data = {}

for i in census_sheet.rows[1:]:
    if i[1].value not in census_data:
        census_data[i[1].value] = {}
    if i[2].value not in census_data[i[1].value]:
        census_data[i[1].value][i[2].value] = {}
        census_data[i[1].value][i[2].value]['pop'] = i[3].value
        census_data[i[1].value][i[2].value]['tract'] = 1
        continue
    census_data[i[1].value][i[2].value]['pop'] += i[3].value
    census_data[i[1].value][i[2].value]['tract'] += 1

pprint.pprint(census_data)
