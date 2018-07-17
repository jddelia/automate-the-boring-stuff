''' This program uses regular expressions to extract
    phone numbers and email addresses from text. '''

import pyperclip
import re

txt = pyperclip.paste()

def phone_numbers(txt):
    ''' This function extracts the phone
        numbers from copied text. '''

    phone_num_lst = []
    phone_numbers = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    phone_mo = phone_numbers.findall(txt)

    if phone_mo == None:
        return None

    for i in phone_mo:
        phone_num_lst.append('-'.join(i))

    return phone_num_lst

phone_nums = phone_numbers(txt)

def email_addrs(txt):
    ''' This function extracts the emails
        from copied text. '''

    email_lst = []
    email_reg = re.compile(r'\w*@\w*\.\w{3}')
    email_mo = email_reg.findall(txt)

    if email_mo == None:
        return None

    for i in email_mo:
        email_lst.append(i)

    return email_lst

emails = email_addrs(txt)

def phones_and_emails(phones, emails):
    ''' This function organizes the phone
        numbers and emails into a text. '''

    phone_email_txt = "Phone numbers are:\n\n"

    if phones == None:
        phone_email_txt += "No phone numbers.\n"
    else:
        for n in phones:
            phone_email_txt += n + "\n"

    phone_email_txt += "\nEmail addresses are:\n\n"

    if emails == None:
        phone_email_txt += "No email addresses.\n"
    else:
        for e in emails:
            phone_email_txt += e + "\n"

    pyperclip.copy(phone_email_txt)

phones_and_emails(phone_nums, emails)
