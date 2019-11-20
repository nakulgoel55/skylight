from money_manager import money
from goals_manager import goals
from thoughts_manager import thoughts
from talk_manager import talk
from restart import restart
from edit_text_files import *
from data import textfile_array, month_to_days
from other import *
from datetime import date
import datetime


# Main Manager
def manager():

    # Prints person's name
    print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")

    user_input = input(
'''

What would you like me to do?  
Show Money Manager: mm
Goals Manager: gm
Thoughts Manager: tm
talk: t
Quit Program: qp
settings: s
    - Regularity: re
    - Rename: rn
    - Restart Program: rp
    
'''
    )

    # Open money manager
    if user_input == 'mm':

        while True:

            # If it returns False, break money(). If it returns True, continue money().
            if not money():
                break

            else:
                continue

    # Open goal manager
    elif user_input == 'gm':
        while True:

            # If it returns False, break out of goals(). If it returns True, continue goals().
            if not goals():
                break

            else:
                continue


    # Open thoughts manager
    elif user_input == 'tm':
        while True:
            # If it returns False, break thoughts(). If it returns True, continue thoughts().
            if not thoughts():
                break

            else:
                continue

    # Open thoughts manager
    elif user_input == 't':
        while True:
            # If it returns False, break thoughts(). If it returns True, continue thoughts().
            if not talk():
                break

            else:
                continue

    # Quit program by returning false and breaking out of the loop
    elif user_input == 'qp':
        write_file('counter_menu.txt', 0)
        # Since False is returned, this loop will break and program will end.
        return False

    # Restart the whole program
    elif user_input == 'rp':
        print("\n")
        restart()
        print("\n")

    elif user_input == 's':
        settings()
        
    # Shows regularity of a user
    elif user_input == 're':
        # Store list of dates user ran the program in a list
        dates_list = list_file_data('regularity.txt')

        # Only get out unique elements
        output = []
        for each_element in dates_list:
            # Using not in to get unique element
            if each_element not in output:
                # If element is unique it is appended to 'output' list
                output.append(each_element)

        # We don't want to show more than 7 dates
        print("\n\n\nHere are your general regularity dates")
        if len(output) < 8:

            for each_element in output:
                print(each_element)
        else:
            for each_element in output[-7:-1]:
                print(each_element)

        # Leave a line
        print('\n')
        user_input_2 = input("Would you like to view a more elaborate report? yes -> y, no -> n: ")

        # If yes, we use the same method as above for all three menus. Goals, thoughts, and money.
        if user_input_2 == 'y':

            dates_list_goals = list_file_data('regularity_goals.txt')

            output = []
            for each_element in dates_list_goals:
                if each_element not in output:
                    output.append(each_element)

            print("\n\n\nHere are your goals regularity dates")

            if len(output) < 8:
                for each_element in output:
                    print(each_element)

            else:
                for each_element in output[-7:-1]:
                    print(each_element)

            dates_list_money = list_file_data('regularity_money.txt')

            output = []
            for each_element in dates_list_money:
                if each_element not in output:
                    output.append(each_element)

            print("\n\n\nHere are your money regularity dates")
            if len(output) < 8:
                for each_element in output:
                    print(each_element)

            else:
                for each_element in output[-7:-1]:
                    print(each_element)

            dates_list_thoughts = list_file_data('regularity_thoughts.txt')
            output = []

            for each_element in dates_list_thoughts:
                if each_element not in output:
                    output.append(each_element)

            print("\n\n\nHere are your thoughts regularity dates")
            if len(output) < 8:

                for each_element in output:
                    print(each_element)
            else:

                for each_element in output[-7:-1]:
                    print(each_element)

        else:
            print("Okay! ")

    # Rename by taking input and writing it to file 'name.txt'. User might want to change his/ her name.
    elif user_input == 'rn':
        new_name = input("Hey, what would you like me to call you? ")
        write_file('name.txt', str(new_name))

    # If input is unexpected
    else:
        print("Please try again")

    # This return makes the main menu loop unless user wants to quit program
    return True
