from other import *


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


def regularity():
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


def rename():
    new_name = input("Hey, what would you like me to call you? ")
    write_file('name.txt', str(new_name))


def restart_program():
    print("\n")
    restart()
    print("\n")



# Settings Manager menu
# setting function is called again and self_input is used instead user_input to call a function inside setting().
def settings(self_input=None):

    setup()
    
    menu_show_frequency_controller()

    # self_input becomes important when a user types some unexpected data type. We don't want to break out of loop
    # on wrong input
    if self_input is not None:
        user_input = str(self_input)

    # list of float because division returns float. Only show menu under these two conditions.
    elif settings_counter / 3 in [1.0, 2.0, 3.0, 4.0, 5.0] or int(settings_counter) == 0:
        user_input = input("Hey, " + read_file('name.txt') + ''' what would you like me to do?
- Regularity: re
- Rename: rn
- Restart Program: rp
- Main Menu: m
''')

    # Without else, the program won't work.
    else:
        user_input = input("What do you want to do next?")

    # Shows week plan
    # Takes into account excess and deficient settings a user has
    if user_input == 're':
        regularity()

    # Shows settings a person has
    elif user_input == 'rn':
        show_balance()

    # Shows today's budget
    elif user_input == 'rp':
        restart_program()


    # Go back to main menu
    elif user_input == 'm':
        # Returning false breaks loop
        return False

    else:
        print("Try again")

    # Leave a line
    print('\n')
    
    # Loop manager
    return True
