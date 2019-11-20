from other import *

def setup():
    # Checks if it is the first time user is using goals
    if len(list_file_data('goals.txt')) == 0:

        # Prints person's name
        print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")
        # Set up goals
        print("Hi, we need to set your goals up first.")
        print('''
The key to being happy in life is giving the body what it wants.
You have to drink the required amount of water and food. Other than that
you have to meet your work target and reading target to keep yourself mentally healthy.
Set your goals now and see how you meet them.
the weekly report is usually shocking, because you see how much you have really been able to accomplish.''')

        # Ask questions
        water_inp = input("How many bottles of water do you want to drink in a day? ")
        write_file('goals.txt', int(water_inp))

        study_inp = input("How many hours do you want to study or work in a day? ")
        append_file('goals.txt', int(study_inp))

        reading_inp = input("How many pages do you want to read in a day? ")
        append_file('goals.txt', int(reading_inp))

        food_inp = input("How many meals should you have in a day? ")
        append_file('goals.txt', int(food_inp))

def show_report():
    # If any data has ever been recorded
        if len(list_file_data('water.txt')) != 0:
            # Prints person's name
            print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")
            # text
            print("Here is how you did this today.")
            # Compares perforamnce to expectations
            print("Water " + str(read_file_line('water.txt', 0)) + " out of " + str(read_file_line('goals.txt', 1)))
            print("Study " + str(read_file_line('study.txt', 0)) + " out of " + str(read_file_line('goals.txt', 2)))
            print("Reading " + str(read_file_line('reading.txt', 0)) + " out of " + str(read_file_line('goals.txt', 3)))
            print("Food " + str(read_file_line('food.txt', 0)) + " out of " + str(read_file_line('goals.txt', 4)))

            # If multiple times data have been recorded, add only the last seven of each to show week's performance
            if len(list_file_data('water.txt')) >= 7:

                print("Here's how you've done this week")
                print("Water " + str(add_last_seven_elements('water.txt')) + " out of " + \
                      str(int(read_file_line('goals.txt', 1)) * 7))
                print("Study " + str(add_last_seven_elements('study.txt')) + " out of " + \
                      str(int(read_file_line('goals.txt', 2)) * 7))
                print("Reading " + str(add_last_seven_elements('reading.txt')) + " out of " +\
                      str(int(read_file_line('goals.txt', 3)) * 7))
                print("Food " + str(add_last_seven_elements('food.txt')) + " out of " + \
                      str(int(read_file_line('goals.txt', 4)) * 7))

        # If no data has ever been recorded
        else:
            # Prints person's name
            print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")
            print("there's nothing you've recorded yet.")


def record_day():

        # Record that user is regular on current date
        if len(list_file_data('regularity_goals.txt')) == 0:
            write_file('regularity_goals.txt', str(today_date))

        else:
            append_file('regularity_goals.txt', str(today_date))

        # Prints person's name
        print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")
        print("let's record your day and see how you did today")

        # Ask questions and check if data type is correct. Write to file and append to files accordingly.
        water = input("How many bottles of water did you drink today? You are supposed to drink "
                      + str(read_file_line('goals.txt', 1)) + " bottles of water in a day. ")

        if data_type(water, int):

            if len(list_file_data('water.txt')) == 0:
                write_file('water.txt', water)

            else:
                append_file('water.txt', water)

        # Go back to recording things
        else:
            goals(str(r))

        study = input("How many hours did you study today? You are supposed to study "
                    + str(read_file_line('goals.txt', 2)) + " hours in a day. ")

        if data_type(study, int):

            if len(list_file_data('study.txt')) == 0:
                write_file('study.txt', study)

            else:
                append_file('study.txt', study)

        # Go back to recording things
        else:

            goals(str(r))

            delete_lastline('water.txt')

        reading = input("How many pages did you read today, you are supposed to read "
                        + str(read_file_line('goals.txt', 3)) + " pages in a day. ")

        if data_type(reading, int):

            if len(list_file_data('reading.txt')) == 0:
                write_file('reading.txt', reading)

            else:
                append_file('reading.txt', reading)

        # Go back to recording things
        else:
            goals(str(r))
            delete_lastline('water.txt')
            delete_lastline('study.txt')

        food = input("How many meals did you have today? You are supposed to have "
                    + str(read_file_line('goals.txt', 4)) + " meals in a day. ")

        if data_type(food, int):

            if len(list_file_data('food.txt')) == 0:
                write_file('food.txt', food)

            else:

                append_file('food.txt', food)

        # Go back to recording things
        else:
            goals(str(r))
            delete_lastline('water.txt')
            delete_lastline('study.txt')
            delete_lastline('reading.txt')

def update_goals():
        # Prints person's name
        print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")
        # Ask user what he/ she wants to update
        user_input = int(input('''what goal would you like to edit?
            
            Water = 1
            Study Hours = 2
            Reading Pages = 3
            food = 4
            
            '''))

        # Different conditionals are required for different text but the method remains same
        if user_input == 1:

            print("Your current water goal is " + str(read_file_line('goals.txt', user_input)) + " bottles.")
            new = input("What do you want your new goal to be? ")

            # goals.txt has data in 4 seperate lines. We can replace data in some line number to avoid
            # using multiple data files
            if data_type(new, int):
                replace_line('goals.txt', int(user_input)-1, str(new))

            else:
                goals(str(u))

        elif user_input == 2:

            print("Your current study goal is " + str(read_file_line('goals.txt', user_input)) + " hours.")
            new = input("What do you want your new goal to be? ")

            if data_type(new, int):
                replace_line('goals.txt', int(user_input)-1, str(new))

            else:
                goals(str(u))

        elif user_input == 3:

            print("Your current reading goal is " + str(read_file_line('goals.txt', user_input)) + " pages.")
            new = input("What do you want your new goal to be? ")

            if data_type(new, int):
                replace_line('goals.txt', int(user_input)-1, str(new))

            else:
                goals(str(u))

        elif user_input == 4:
            print("Your current food goal is " + str(read_file_line('goals.txt', user_input)) + " meals.")
            new = input("What do you want your new goal to be? ")

            if data_type(new, int):
                replace_line('goals.txt', int(user_input) - 1, str(new))

            else:
                goals(str(u))

        # Last checkpoint
        else:
            print("Try again.")
            goals(str(u))


# Goals Manager
def goals(self_input=None):

    # Counter works the same way it works for thoughts and money manager

    setup()

    menu_counter = int(read_file('counter_menu.txt'))

    write_file('counter_menu.txt', str(int(menu_counter) + 1))


    # If a user made some mistake in this menu earlier while giving input, go back to last point user was at.
    if self_input is not None:
        user_input = str(self_input)

    # Show menu only under these conditions
    elif menu_counter / 3 in range(1,100) or int(menu_counter) == 0:
        user_input = input("Hey, " + read_file('name.txt') + ''' what would you like me to do?
                               Show Report: sr
                               Record Day: r
                               Main Menu: m
                               Update Goals: u
                               ''')

    # Question
    else:
        user_input = input("What do you want to do next?")

    # Shows report of user performance
    if user_input == 'sr':
        show_report()

    # Record data
    elif user_input == 'r':
        record_day()

    # Update goals
    elif user_input == 'u':
        update_goals()

    # Go back to main menu
    elif user_input == 'm':
        return_to_menu()

    else:
        print('try again')

    print('\n')

    # Make menu loop
    return True

