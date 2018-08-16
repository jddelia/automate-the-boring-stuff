''' This program takes lists of strings and prints
    the contents of each list in columns.
    Assignment detail can be found at:
    https://automatetheboringstuff.com/chapter6/,
    Table Printer assignment. '''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def table_printer(list):
    col_width = [0] * len(list)
    for i in range(len(list)):
        col_width[i] = len(sorted(list[i], key=len, reverse=True)[0])
    print(col_width)

    for i in range(len(list[0])):
        for n in range(len(list)):
            print(list[n][i].rjust(col_width[n]), end=" ")
        print()

table_printer(tableData)
