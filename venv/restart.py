# Restart program by erasing files and get necessary data through user input.
# restart_default() Called if some text file is missing in the user's folder.

from edit_text_files import *
from restart import *
from data import textfile_array, month_to_days
from datetime import date
import datetime
from other import data_type


def restart_default():

    # text file_array holds name of all text files
    # for each text file in the list delete all data irrespective of if data exists or not.
    for each in textfile_array:
        # delete all data in file
        write_file(each, '')

    # This function is seperate from restart() just for this message.
    # Makes user feel a bit comfortable because the program knows the user is new
    print('''Hey, it looks like you are a new user.
I need  data to make a plan best suited for you.
Let's begin with the basic questions.
Answer them very carefully.\n''')

    # If there is no start date, the program can't do calculations.
    # This is why we add the current date as the start date
    if len(list_file_data('start_date.txt')) == 0:
        # object today created containing information about date
        today = datetime.datetime.now()
        # writes this data to a file "start_date.txt"
        write_file('start_date.txt', str(today.year))
        append_file('start_date.txt', str(today.month))
        append_file('start_date.txt', str(today.day))

    # Makes sure that name.txt is empty. If it is empty, it asks for a new name and writes it in "name.txt"
    if len(list_file_data('name.txt')) == 0:

        element = input("What would you like me to call you? ")

        # Checks for expected data type.
        if data_type(element, str) and any(c.isalpha() for c in element):

            write_file('name.txt', str(element))
            print("I will now call you " + read_file('name.txt') + ".\n")

        else:

            print("Looks like you didn't give me the input I needed. ")
            restart_default()

    # If empty, put 0 as first element in these lists. Helps with calculations.
    element = ['today_expenditure.txt',
               'excess.txt',
               'deficient.txt',
               'counter_money.txt',
               'counter_thoughts.txt',
               'counter_goals.txt']
    for i in element:
        if len(list_file_data(i)) == 0:
            write_file(i, 0)


# Deletes all data in file using a for loop.
def restart():

    print("REMEMBER IF NOTHING YOU TYPE WORKS, TYPE 'M'.")

    element = str(input('''
Are you sure you want to restart?"
This will delete all your data."
If yes, type -> 'restart', if no, type -> 'n'
'''))

    if element == 'restart':

        for each in textfile_array:
            write_file(each, '')

        print('''Hey, this program has been restarted like you wanted.
                I need some data to make a plan for you.\n''')

        # If there is no start date, the program can't do calculations. This is why we add the current date as the start date
        if len(list_file_data('start_date.txt')) == 0:
            # object today created containing information about date
            today = datetime.datetime.now()
            # writes this data to a file "start_date.txt"
            write_file('start_date.txt', str(today.year))
            append_file('start_date.txt', str(today.month))
            append_file('start_date.txt', str(today.day))

        # Makes sure that name.txt is empty. If it is empty, it asks for a new name and writes it in "name.txt"
        if len(list_file_data('name.txt')) == 0:

            element = input("What would you like me to call you? ")
            # Checks for expected data type.
            if data_type(element, str) and any(c.isalpha() for c in element):
                write_file('name.txt', str(element))
                print("I will now call you " + read_file('name.txt') + ".\n")

            else:

                print("Looks like you didn't give me the input I needed. ")
                restart()

        # If empty, put 0 as first element in these lists
        element = ['today_expenditure.txt', 'excess.txt', 'deficient.txt']

        for i in element:

            if len(list_file_data(i)) == 0:
                write_file(i, 0)

