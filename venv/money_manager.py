from other import *
from restart import restart
from edit_text_files import *
from data import textfile_array, month_to_days
from variables import *
from datetime import date
import datetime


def menu_show_frequency_controller():

    # We need to show the menu 1 in 3 times this function is called, otherwise, it gets annoying.
    # To do so, we look at the counter value
    if data_type(read_file('counter_menu.txt'), int):
        menu_counter = int(read_file('counter_menu.txt'))
        # Counter = counter + 1 since function is called
        write_file('counter_menu.txt', menu_counter + 1)
    else:
        write_file('counter_menu.txt', str(0))
    
def setup():

    # Makes sure that total.txt is empty. If it is empty, it asks for total money a user has and writes it in "total.txt"
    if len(list_file_data('total.txt')) == 0:
        totalfiller()

    # Makes sure that maximum_budget.txt is empty. If it is empty, it asks for max money a user can spend
    # Writes it in "maximum_budget.txt"
    if len(list_file_data('maximum_budget.txt')) == 0:
        maxfiller()

    # Makes sure that yearly_budget.txt is empty. If it is empty, it asks for money a user wants to spend in 365 days.
    # Writes it in "yearly_budget.txt"
    if len(list_file_data('yearly_budget.txt')) == 0:
        yearlyfiller()

    # Makes sure saving.txt is empty. If it is empty it automatically fills it with it's calculations
    if len(list_file_data('saving.txt')) == 0:
        savingfiller()

    menu_counter = 0

    


def totalfiller():

    element = input('''How much money do you have in 'TOTAL', in the form of cash or credit?
This information won't be used to make your budget. Enter a number.\n ''')

    # Checks for expected data type -> Int.
    if data_type(element, int):

        write_file('total.txt', int(element))

    else:

        print("Looks like you didn't give me the input I needed. ")
        delete_lastline('name.txt')
        money()


def maxfiller():
    element = input("Hey " + read_file('name.txt') + ", how much money can you realistically spend in the next 365 days 'at maximum' without getting into trouble?\n ")

    # Checks for expected data type -> Int.
    if data_type(element, int):
        write_file('maximum_budget.txt', int(element))

    else:
        print("Looks like you didn't give me the input I needed. ")
        # We have to delete data in the files we just wrote data in.
        # Although, restart_default would delete it anyway, since it deletes data in all files.
        delete_lastline('name.txt')
        delete_lastline('total.txt')
        money()


def yearlyfiller():

        element = input('''\nHow much money would you actually like to spend in the next 365 days?
This number will be used to design your budget primarily and will be your yearly budget.
If you don't overspend your budget, next days budget would increase.\n''')
        # Checks for expected data type -> Int.
        if data_type(element, int):

            write_file('yearly_budget.txt', int(element))

        else:

            print("Looks like you didn't give me the input I needed. ")
            # We have to delete data in the files we just wrote data in.
            # Although, restart_default would delete it anyway, since it deletes data in all files.
            delete_lastline('name.txt')
            delete_lastline('total.txt')
            delete_lastline('yearly_budget.txt')
            restart_default()


def savingfiller():

        write_file('saving.txt', int(read_file('total.txt')) - int(read_file('yearly_budget.txt')))

        if len(list_file_data('today_date.txt')) == 0:

            # Creates object now storing data about date and time
            today_date = datetime.datetime.now()
            write_file('today_date.txt', str(int(today_date.day) - 1))


def week_plan():

        # Daily is daily budget. It is equal to yearly budget divided by number of days left in an year.
        daily = int(int(read_file('yearly_budget.txt'))) / int(year_days_left)

        # exces is data in file excess.txt
        exces = list_file_data('excess.txt')
        element = 0

        # Add all elements in exces list
        for i in exces:
            element += int(i)

        excess = int(element)

        # Same method for deficient
        deficien = list_file_data('deficient.txt')

        y = 0

        for e in deficien:

            y += int(e)

        deficient = int(y)
        # We get total excess and total deficient
        # Find the difference and store it in a variable called excess
        excess = excess - deficient

        # If excess is excess
        if excess > 0:
            # Prints person's name
            print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")
            print("You have an additional $" + str(excess) + " that you have not spent from your past budget.")

        # If excess is negative, hence, deficient
        else:
            if excess < 0:
                # Prints person's name
                print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")
                print("You are short of $" + str(excess) + " be careful while spending.")

        # Money a user can spend in a week is daily amount times 7 in addition to excess times 7 divided by days
        # left in an year
        print("You can spend $" + str(int(7 * float(daily) + (int(excess)*7/year_days_left))) + " in the next 7 days")


def show_balance():
    # Prints person's name
        print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")
        # Show yearly budget
        print("You have $" + str(read_file('yearly_budget.txt')) + " left to spend in the next " + str(
                year_days_left) + " days.")
        # Show maximum budget
        print("At max,you can spend $" + str((read_file('maximum_budget.txt'))) + " in the next " + str(
                year_days_left) + " days.")
        # Show total budget
        print("You have a total of $" + str((read_file('total.txt'))) + " left.")
        # Show saving which is equal to total - yearly budget
        print("You are saving a total of $" + str((read_file('saving.txt'))) + ".")


def total_balance():

        # Follow same steps as week plan to find excess and deficient
        daily = int(int(read_file('yearly_budget.txt'))) / int(year_days_left)

        exces = list_file_data('excess.txt')
        element = 0

        for i in exces:
            element += int(i)

        excess = int(element)

        deficien = list_file_data('deficient.txt')

        y = 0

        for e in deficien:

            y += int(e)

        deficient = int(y)

        excess = excess - deficient

        # If excess > 0 print some statements
        if excess > 0:
            # Prints person's name
            print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")
            print("You have an additional $" + str(excess) + " that you have not spent from your past budget.")
            print("Today's budget is $" + str(int(round(daily)+(int(excess) / int(year_days_left)))))

        # # If excess < 0 print some other statements
        else:
            # Prints person's name
            print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")
            print("You are short of $" + str(deficient) + ". Be careful while spending.")
            print("Today's budget is $" + str(int(round(daily)-(int(deficient) / int(year_days_left)))))
            if excess + round(daily) < 0:
                print("You need to be earning money man, you don't have anything to spend.")

def record_expenditure():
    # Prints person's name
        print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")
        element = (input("How much money did you spend today? If you have already recorded expense today,"
                         "don't include that money again or your balance will go off $"))

        # Check data type
        if data_type(element, int):

            # Convert input to integer
            element = int(element)

            append_file('expenditure.txt', element)

            # Get date of the last time user recorded expenditure
            y = read_file('today_date.txt')

            # Find daily budget
            daily = int((int(read_file('yearly_budget.txt'))) / int(year_days_left))

            today_date = datetime.datetime.now()

            # If user has recorded expenditure today
            if int(y) == int(today_date.day):

                # Find all expenditure of a user today and add it.
                list1 = list_file_data('today_expenditure.txt')
                z = 0

                for i in list1:
                    z += int(i)

                # a is total money spent today other than the recently recorded expenditure named element
                a = int(z)
                append_file('today_expenditure.txt', element)

                # If user has spent less than daily budget, delete last line in excess
                if a <= daily:
                    delete_lastline('excess.txt')
                # If user has spent more than daily budget, delete last line in excess
                else:
                    delete_lastline('deficient.txt')

                # If user has spent less than daily budget, write to excess
                if (a + element) <= daily:
                    append_file('excess.txt', daily - (a + element))
                # If user has spent more than daily budget, write to deficient
                else:
                    append_file('deficient.txt', (a + element) - daily)
                # To check if user has recorded expenditure today
                write_file('today_date.txt', today_date.day)
                # Reduce money from yearly budget
                write_file('yearly_budget.txt', int(read_file('yearly_budget.txt')) - int(element))
                # Reduce money from total budget
                write_file('total.txt', int(read_file('total.txt')) - int(element))
                # Reduce money from maximum budget
                write_file('maximum_budget.txt', int(read_file('maximum_budget.txt')) - int(element))

            # If user has not recorded expenditure today
            else:
                # Add expenditure to file today_expenditure.txt
                write_file('today_expenditure.txt', element)
                # If expenditure is less than daily budget, write daily - expenditure to excess.txt
                if element <= daily:
                    append_file('excess.txt', daily - element)
                # If expenditure is greater than daily budget, write daily - expenditure to excess.txt
                else:
                    append_file('deficient.txt', element - daily)

                # To check if user has recorded expenditure today
                write_file('today_date.txt', today_date.day)
                # Reduce money from yearly budget
                write_file('yearly_budget.txt', int(read_file('yearly_budget.txt')) - int(element))
                # Reduce money from total budget
                write_file('total.txt', int(read_file('total.txt')) - int(element))
                # Reduce money from maximum budget
                write_file('maximum_budget.txt', int(read_file('maximum_budget.txt')) - int(element))
                if len(list_file_data('regularity_money.txt')) == 0:
                    write_file('regularity_money.txt', str(today_date))

                else:
                    append_file('regularity_money.txt', str(today_date))

            # Append data to log.txt
            append_file('log.txt', (str("$") + str(int(element))))
            # Append date to log.txt
            append_file('log.txt', str(today_date))
            expenditure_where = input("Where did you spend the money? type 'n' to not tell where. ")
            if expenditure_where == 'n':
                append_file('log.txt', str("Expenditure details not reported."))
            else:
                append_file('log.txt', str(expenditure_where))
            append_file('log.txt', str("------------------------------"))
            print("Okay, thanks for reporting data today.")

        else:
            money('re')

def increase_balance():
    # Prints person's name
        print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")

        input1 = input("How much money would you like to add? Enter an integer: $")

        # Making sure data is as expected
        if data_type(input1, int):
            # Change data in files
            write_file('yearly_budget.txt', int(read_file('yearly_budget.txt')) + int(input1))
            write_file('maximum_budget.txt', int(read_file('maximum_budget.txt')) + int(input1))
            write_file('total.txt', int(read_file('total.txt')) + int(input1))
            append_file("log.txt", str("Balance increased by $") + str(input1))
            question = input("Where did the money come from? Type 'n' if you don't want to answer?")
            if question == 'n':
                append_file("log.txt", str("No information provided"))
                append_file('log.txt', str("------------------------------"))
            else:
                append_file("log.txt", str(question))
                append_file('log.txt', str("------------------------------"))

        # If data is incorrect call function money, and come back to increase budget
        else:
            money(str(ib))

def decrease_balance():
    # Prints person's name
        print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")
        input1 = input("How much money would you like to subtract? Enter an integer: $")
        append_file("log.txt", str("Balance increased by $") + str(input1))
        question = input("Where did the money go? Type 'n' if you don't want to answer?")
        if question == 'n':
            append_file("log.txt", str("No information provided"))
            append_file('log.txt', str("------------------------------"))
        else:
            append_file("log.txt", str(question))
            append_file('log.txt', str("------------------------------"))

        # Making sure data is as expecteds
        if data_type(input1, int):
            # Change data in files
            write_file('yearly_budget.txt', int(read_file('yearly_budget.txt')) - int(input1))
            write_file('maximum_budget.txt', int(read_file('maximum_budget.txt')) - int(input1))
            write_file('total.txt', int(read_file('total.txt')) - int(input1))

        else:
            money(str(db))

# To save some percentage of remaining yearly budget to savings if user needs to save more money.
def saving():

    # Prints person's name
    print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")

    print("You are going to save some % of your allocated yearlybudget.")

    element = input("How much out of $" + read_file('yearly_budget.txt') + " do you want to save. " + '''
        No saving: 1
        20%: 2
        30%: 3
        40%: 4
        50%: 5
        60%: 6''')

    if element == str(1):

        print("Okay, going back to menu")

    elif 1 < int(element) < 6:

        write_file('saving.txt',
                   int(read_file('saving.txt')) + int(int(read_file('yearly_budget.txt')) * (int(element) / 10)))
        write_file('yearly_budget.txt', str(int(int(read_file('yearly_budget.txt')) * (1 - (int(element) / 10)))))

    else:
        print("Try again! Type 1, 2, 3, 4, 5 or 6")

def show_total_expenditure():
    today_date = datetime.datetime.now()
    day = today_date.day
    sum_of_numbers = 0
    if len(list_file_data('expenditure.txt'))>31:
            for each_element in list_file_data('expenditure.txt')[-day,:]:
                sum_of_numbers += int(each_element)
    else:
            for each_element in list_file_data('expenditure.txt'):
                sum_of_numbers += int(each_element)
    print("Your total expenditure this month recorded this far is " + str(sum_of_numbers))


def show_logs():
        print("Here are your logs")
        if len(list_file_data("log.txt")) < 50:
            for each_element in list_file_data('log.txt'):
                print(each_element)
        else:
            for each_element in list_file_data('log.txt')[-50, :]:
                print(each_element)
        question = input("Do you want to see all recorded logs? Yes: y, No: n")
        if question == "y":
            for each_element in list_file_data('log.txt'):
                print(each_element)

def saving_to_yearly():
# Prints person's name
        print(str(random_greeting()) + " " + str(read_file('name.txt')) + ", ")

        # Tell person information about his/ her balances
        print("You have $" + str(read_file('saving.txt')) + " in your savings right now and $" + str(
            read_file('yearly_budget.txt')) + " in your yearly  budget.")

        # Question
        element = input('How much money do you want to move from saving to yearly budget? $')

        # If data type is as expected
        if data_type(element, int):
            # Move money from saving to yearly budget
            write_file('saving.txt', str(int(read_file('saving.txt')) - int(element)))
            write_file('yearly_budget.txt', str(int(read_file('yearly_budget.txt')) + int(element)))
        else:
            money(str(syb))


def first_time(called):
    x = -1
    return x+1



# Money Manager menu
# money function is called again and self_input is used instead user_input to call a function inside money().
def money(self_input=None):

    setup()


    menu_counter = int(read_file('counter_menu.txt'))

    write_file('counter_menu.txt', str(int(menu_counter) + 1))
    
    # Shows menu once in 3 times
    menu_show_frequency_controller()

    # self_input becomes important when a user types some unexpected data type. We don't want to break out of loop
    # on wrong input
    if self_input is not None:
        user_input = str(self_input)

    # list of float because division returns float. Only show menu under these two conditions.
    elif menu_counter / 3 in range(1,100) or int(menu_counter) == 0:
        user_input = input("Hey, " + read_file('name.txt') + ''' what would you like me to do?
Show week plan: wp
Show balance: sb 
Show today's budget: tb
Record Expenditure: re
Increase balance: ib
Decrease balance: db
Move money from yearly budget to savings: s
Move money from savings to yearly budget: syb
Show logs: sl
Show total expenditure: ste
Main: m

''')

    # Without else, the program won't work.
    else:
        user_input = input("What do you want to do next?")

    # Shows week plan
    # Takes into account excess and deficient money a user has
    if user_input == 'wp':
        week_plan()

    # Shows money a person has
    elif user_input == 'sb':
        show_balance()

    # Shows today's budget
    elif user_input == 'tb':
        total_balance()

    # Record expenditure
    elif user_input == 're':
        record_expenditure()

     # Increase budget by adding to budgets. Useful if someone has some income
    elif user_input == 'ib':
        increase_balance()

    # Increase budget by adding to budgets. Useful if someone has some income
    elif user_input == 'db':
        decrease_balance()

    # If person wants to save money call saving function
    elif user_input == 's':
        saving()

    elif user_input == 'sl':
        show_logs()

    elif user_input == 'ste':
        show_total_expenditure()

    # Move money from saving to yearly budget
    elif user_input == 'syb':
        saving_to_yearly()

    # Go back to main menu
    elif user_input == 'm':
        return_to_menu()

    else:
        print("Try again")

    # Leave a line
    print('\n')
    
    # Loop manager
    return True

