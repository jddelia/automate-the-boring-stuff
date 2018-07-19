import pyperclip

txt = pyperclip.paste()

def bullet_point_adder(txt):
    new_txt = ''
    split_txt = txt.replace('*', '').split('\n')

    for i in split_txt:
        if i != '':
            new_txt += '* ' + i.capitalize() + '\n'
        else:
            new_txt += i + '\n'

    print(new_txt)

bullet_point_adder(txt)
