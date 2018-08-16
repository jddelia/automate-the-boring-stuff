''' This program produces quizes about state capitals,
    randomizing the question order. '''

from random import randint
from random import choice
from random import shuffle
import os


capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
    'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

def cap_lst():    # List of capitals dictionary.
    caps_lst = []
    for state, cap in capitals.items():
        caps_lst.append([state, cap])
    return caps_lst

answer_lst = cap_lst()

answers = ""
for i in answer_lst:
    answers += i[0] + ': ' + i[1] + '\n'

def mult_choice(lst, c):                         # Format for questions.
    mult_lst = [c]
    for i in lst:                                # Creates list of capitals.
        if len(mult_lst) == 4:
            break
        rand_choice = choice(i)
        if rand_choice in mult_lst:
            rand_choice = choice(i)
            continue
        mult_lst.append(rand_choice)

    # Format for quiz questions
    shuffle(mult_lst)   # Shuffle list of random questions, including answer.
    a =  mult_lst[0].ljust(10) + "\t" + mult_lst[1].rjust(10) + "\n"
    a += mult_lst[2].ljust(10) + "\t" + mult_lst[3].rjust(10) + "\n\n"
    return a

def geo_quizes(integer):            # Function to create quizes.
    os.makedirs('geoQuizes')         # Create new directory and
    os.chdir('geoQuizes')           # switch cwd to it.
    fin = open('answers.txt', 'w')
    fin.write(str(answers))
    ans_lst = answer_lst.copy()
    for n in range(integer):                # Amount of quizes being created.
        quiz_n = "State Capitals Quiz\n\n\nSelect the correct answer for each.\n\n"
        quiz = 'quiz' + str(n) + '.txt'
        shuffle(ans_lst)
        count = 1
        for i in ans_lst:           # Iterate through shuffled list.
            quiz_n += str(count) + ". State: " + i[0] + "\n\n"
            quiz_n += mult_choice(ans_lst, i[1])
            count += 1
        fp = open(quiz, 'w')                # Create file and close at end.
        fp.write(quiz_n)
        fp.close()

geo_quizes(2)
