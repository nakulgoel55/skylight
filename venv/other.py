from edit_text_files import read_file, write_file
import os
import random
from variables import *
from data import textfile_array, month_to_days
from datetime import date, datetime
import smtplib
from edit_text_files import *

def menu_show_frequency_controller():

    # We need to show the menu 1 in 3 times this function is called, otherwise, it gets annoying.
    # To do so, we look at the counter value
    if data_type(read_file('counter_menu.txt')) != int:
        menu_counter = int(read_file('counter_menu.txt'))
        # Counter = counter + 1 since function is called
        write_file('counter_menu.txt', str((menu_counter) + 1))

def return_to_menu():
    write_file('menu_counter.txt', 0)
    return False

# If data_type is the expected data type it returns True and vice versa. Prevents data_type errors.
def data_type(user_input, expected_data_type):

    # This function is mostly important for integers, hence, there is a different test for integers.
    if expected_data_type == int:
        # Try except for integers
        try:
            # Try converting user_input into an integer
            user_input = int(user_input)
            # Make sure it is an integer and return True if so
            if type(user_input) == int:
                return True
        # If unable to convert user_input to integer
        except ValueError:
            print("Numbers only. Don't enter a string or float")
            return False

    # We might need to check for other data types.
    if type(user_input) == expected_data_type:
        return True

    else:
        print("You didn't provide the expected data.")
        return False




# Our program shouldn't always say hi to the user, otherwise it would become repetitive.
def random_greeting():
    words = ['Hi', 'Hey', 'Hello', 'Greetings']
    # Using random to pick a random word
    return random.choice(words)


def path_maker(file_name):
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    a = 'text_files/same'
    b = a.replace("same", str(file_name))
    # For accessing the file in a folder contained in the current folder
    filename = os.path.join(file_dir, b)
    return filename


def daily_life_path_maker(file_name):
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    a = 'daily_life/same'
    b = a.replace("same", str(file_name))
    # For accessing the file in a folder contained in the current folder
    filename = os.path.join(file_dir, b)
    return filename


# Writes to file, creates file if file doesn't exist, writes data in file, but deletes all previous data
def write_file(file_name, data):
    # Since File is inside another directory, we create a dynamic path to that file to access it.
    filename = path_maker(file_name)
    # w+ creates file if it doesn't exist
    input_data = open(filename, 'w+')
    input_data.write(str(data))

    # close file_name which is the parameter/ file we want to write the data to.
    input_data.close()


# Writes to file, creates file if file doesn't exist, writes data in file, but deletes all previous data
def write_file_daily_life(file_name, data):
    # Since File is inside another directory, we create a dynamic path to that file to access it.
    filename = daily_life_path_maker(file_name)
    # w+ creates file if it doesn't exist
    input_data = open(filename, 'w+')
    input_data.write(str(data))

    # close file_name which is the parameter/ file we want to write the data to.
    input_data.close()


# Reads specific line from a text file.
def read_file_line(file_name, line_num):
    # Since File is inside another directory, we create a dynamic path to that file to access it.
    filename = path_maker(file_name)
    # use method .readlines() to break it into single line strings.
    lines = open(filename, 'r').readlines()
    # returns data from desired line - 1.
    # -1 is subtract because only one function calls this function and it takes in user input
    # from 1 instead of 0. It was more convenient to subtract 1 here than there from "line_num"
    return lines[line_num - 1]


# Replaces/writes on a particular line
def replace_line(file_name, line_num, text):
    # Since File is inside another directory, we create a dynamic path to that file to access it.
    filename = path_maker(file_name)
    # use method .readlines() to break it into single line strings.
    lines = open(filename, 'r').readlines()
    # Replaces text in line and leaves enough spaces to move to next file in text file.
    lines[line_num] = text + str('\n')
    out = open(filename, 'w')
    out.writelines(lines)
    out.close()


# Reads from file, removes \n, appends data to a list, returns list
def list_file_data(file_name):
    # Since File is inside another directory, we create a dynamic path to that file to access it.
    filename = path_maker(file_name)
    # Initialize empty list
    data_list = []
    # A object that stores text in .txt file and use method .readlines() to break it into single
    # line strings.
    input_data = open(filename, 'r')

    workable_data = input_data.readlines()

    # For each single line string, strip away '\n' and store to variable data2
    for element in workable_data:
        if element.strip():
            data2 = element.rstrip('\n')
            # Append data2 to list data_list
            data_list.append(str(data2))
        else:
            continue

    input_data.close()

    # Returns list of data
    return data_list


# Adds last seven rows in any text file.
# This is required when we want to see activity in the last seven days
def add_last_few_elements_default_7(file_name, number_of_element = 7):
    # Since File is inside another directory, we create a dynamic path to that file to access it.
    filename = path_maker(file_name)
    # Returns all data in file in the form of a list to list1
    list1 = list_file_data(filename)

    element = 0
    # for loop to add data in the last seven days if data is of type integer
    for each_element in list1[len(list1) - number_of_element: len(list1)]:

        if type(i) == int:
            element += each_element
        else:
            continue
    return element


# Reads from file, returns only first element
def read_file(file_name):
    # Since File is inside another directory, we create a dynamic path to that file to access it.
    filename = path_maker(file_name)
    # Initialize empty list
    data_list = []
    # Read data in file and returns data to a list
    input_data = open(filename, 'r')
    workable_data = input_data.readlines()

    # For each element in the list, remove \n and append it to a list data_list
    for element in workable_data:
        if element.strip():
            data2 = element.rstrip('\n')
            data_list.append(str(data2))
        else:
            continue

    # close the file 'file_name' which is the parameter for this function/ the file
    # the program reads from.
    input_data.close()

    if len(data_list) == 0:
        # We return an integer because a string can make the program crash in case
        # the program expected an integer.
        return 0

    else:
        # Returns first element of the list data_list.
        return data_list[0]


# Reads from file, returns only first element
def read_file_daily_life(file_name):
    # Since File is inside another directory, we create a dynamic path to that file to access it.
    filename = daily_life_path_maker(file_name)
    # Initialize empty list
    data_list = []
    # Read data in file and returns data to a list
    input_data = open(filename, 'r')
    workable_data = input_data.readlines()

    # For each element in the list, remove \n and append it to a list data_list
    for element in workable_data:
        if element.strip():
            data2 = element.rstrip('\n')
            data_list.append(str(data2))
        else:
            continue

    # close the file 'file_name' which is the parameter for this function/ the file
    # the program reads from.
    input_data.close()

    if len(data_list) == 0:
        # We return an integer because a string can make the program crash in case
        # the program expected an integer.
        return 0

    else:
        # Returns first element of the list data_list.
        return data_list[0]


# Appends to file, creates file if file doesn't exist, writes data in file.
def append_file(file_name, data):
    # Since File is inside another directory, we create a dynamic path to that file to access it.
    filename = path_maker(file_name)
    # + creates file if it doesn't exist
    input_data = open(str(filename), 'a+')
    # \m is important so that data is written in the next line
    input_data.write('\n' + str(data))
    # close file_name which is the parameter/ file we want to append the data to.
    input_data.close()


# Deletes last line in a text file.
# The problem is complicated because if a user opens a text file and puts the pointer
# In the wrong place the program would do very unusual things.
# This particular function is not my original code.
# The pointer must always be in the right position in the text file
def delete_lastline(file_name):
    # Since File is inside another directory, we create a dynamic path to that file to access it.
    filename = path_maker(file_name)
    file = open(filename, "r+", encoding="utf-8")

    # Move the pointer (similar to a cursor in a text editor) to the end of the file.
    file.seek(0, os.SEEK_END)

    # This code means the following code skips the very last character in the file -
    # i.e. in the case the last line is null we delete the last line
    # and the penultimate one
    pos = file.tell() - 1

    # Read each character in the file one at a time from the penultimate
    # character going backwards, searching for a newline character
    # If we find a new line, exit the search
    while pos > 0 and file.read(1) != "\n":
        pos -= 1
        file.seek(pos, os.SEEK_SET)

    # So long as we're not at the start of the file, delete all the characters ahead of this position
    if pos > 0:
        file.seek(pos, os.SEEK_SET)
        file.truncate()

    file.close()
