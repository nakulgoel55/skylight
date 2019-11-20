from edit_text_files import *
from other import *
from encryption_decryption import *
from data import textfile_array, month_to_days
from datetime import date
import datetime
from variables import *


# Thoughts manager
def talk():

    # To avoid showing thoughts menu on losop
    menu_counter = int(read_file('counter_menu.txt'))
    # Change counter value
    write_file('counter_menu.txt', str(int(menu_counter) + 1))
    # Set person's name to variable named person
    person = read_file('name.txt')


    # If thought_counter/ 2 is an integer or thought_counter is 0, show menu
    if menu_counter / 2 in range(1,100) or int(menu_counter) == 0:

        user_input = input("Hey, " + person + '''
                           
                           Record happy feelings: hf
                           Record sad feelings: sf
                           Record angry feelings: af
                           Record confused feelings: cf
                           Talk generally: tg
                           Main Menu: m
                           
                           ''')
    # Else is necessary to make it work
    else:
        user_input = input("What do you want to do next?")

    if user_input == 'hf':

        # Prints person's name
        print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")
        print("Let's record this")

        # If use has never set a password, ask for password
        if len(list_file_data('password.txt')) == 0:

            password = input("Enter your password: ")

            # Encrypt password and write it to a file
            element = encryption(password)
            write_file('password.txt', element)

        # Ask user to record thoughts only if user has never recorded thoughts
        if len(list_file_data('happy.txt')) == 0:

            lines = []

            # When user types 'done', loop breaks
            print("Write 'done' in a new line when you are done recording your thoughts")

            # Keep asking for input unless user types 'done'
            while True:
                line = input()

                if line != 'done':
                    # Encrypt input and append to list
                    encrypted_text = encryption(line)
                    lines.append(encrypted_text)

                # break out of loop when user types done
                else:
                    break

            # Join all input
            text = '\n'.join(lines)

            # Write to files
            write_file('happy.txt', encryption(str(today_date)))
            append_file('happy.txt', text)


        # If user has previously recorded thoughts
        else:
            # Same as above
            lines = []

            print("Write 'done' in a new line when you are done recording your thoughts")

            while True:

                line = input()

                if line != 'done':
                    line = encryption(line)
                    lines.append(line)

                else:
                    break

            text = '\n'.join(lines)

            append_file('happy.txt', encryption(str(today_date)))
            append_file('happy.txt', text)

        # Print encryption text
        print("Here's the super secret encrypted text because it's really cool to look at. \n\n")
        for each in list_file_data('thoughts.txt')[-(len(lines))-1:]:
            print(str(each))

        # Leave a line
        print('\n')

    # Show a person's thoughts
    elif user_input == 'st':
            # Prints person's name
            print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")

            # If there are no thoughts
            if len(list_file_data('thoughts.txt')) == 0:
                print("No thoughts recorded yet")

            # If there are thoughts, show them if input matches password
            else:
                # Ask for input
                user_pass = str(input("Password: "))
                # Check if input matches password
                string = decryption_pass()
                string = string.rstrip('\n')
                if user_pass == string:
                    print('\n'*2)

                    # Decryption returns all decrypted thoughts
                    decryption()

                    print('\n'*2)

    # Go back to menu, returning false breaks the while loop
    elif user_input == 'm':
        return_to_menu()

    # If input was not expected
    else:
        print("Try again. ")
    # Leave a lne
    print('\n')
    return True
