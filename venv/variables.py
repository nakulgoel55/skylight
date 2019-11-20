from data import textfile_array, month_to_days
from edit_text_files import *


# Without a start date, the program can't do some important calculations.
# Current date becomes the start date if 'start_date.txt' is start date.
# Data written to start_date.txt
if len(list_file_data('start_date.txt')) == 0:
    # Creates object 'now' storing data about date and time
    now = datetime.datetime.now()
    write_file('start_date.txt', str(now.year))
    append_file('start_date.txt', str(now.month))
    append_file('start_date.txt', str(now.day))


# Creates object 'now' storing data about date and time
now = datetime.datetime.now()

# Reads from start_date.txt, puts it in a list, and stores it in start date variable
start_date_ = list_file_data('start_date.txt')

# Setting today_date as current date
today_date = date(now.year, now.month, now.day)

# Setting d as beginning date
start_date = date(int(start_date_[0]), int(start_date_[1]), int(start_date_[2]))

# Delta is number of days one has followed the program for.
# It is not a string or integer. Example: 3 days, 0:00:00
# Convert Delta to a string and take first element by using string as a list.
delta = today_date - start_date

# Days since program has been running
total_days = delta.days

# Numbers of days left in a month
month_days_left = int(month_to_days[now.month]) - now.day

def calculate_number_of_days_left(total_days):
    if total_days == 365:
        return 365

    elif int(total_days) > 365:
        # Number of days left in a year
        year_number = delta/365
        days_left = 365 - (int(total_days) - 365*year_number)
        return days_left

    else:
        return 365 - total_days

year_days_left = calculate_number_of_days_left(total_days)

# Searches for user name
name = read_file('name.txt')

# Every time a user runs the program, the program writes the date in regularity.txt.
if len(list_file_data('regularity.txt')) == 0:

    write_file('regularity.txt', str(today_date))

else:

    append_file('regularity.txt', str(today_date))

