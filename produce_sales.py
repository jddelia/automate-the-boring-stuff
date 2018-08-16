#! /usr/bin/python3

""" This program parses through a spreadsheet and
    updates the price of specific produce items. """

import openpyxl
import os

os.chdir('/home/jddelia/python/automate/chap12')

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active
produce = {'Celery': 1.19, 'Garlic': 3.07, 'Lemon': 1.27}

for i in sheet.rows[1:]:
    if i[0].value in produce:
        sheet[i[1].coordinate] = produce[i[0].value]
        print(i[0].value, i[1].value)

wb.save('produceSales_updated.xlsx')
