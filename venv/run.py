from main_manager import manager
from edit_text_files import write_file

filename_list = ['counter_thoughts.txt', 'counter_goals.txt', 'counter_money.txt']
for each_file in filename_list:
    write_file(each_file, '')

write_file('counter_menu.txt', 0)

# While loop to show main menu on loop, till user wants to quit.
# Not sure if this is the best method to make things loop, but, it works perfectly.
while True:

    print("\n")

    # If not True, break
    if not manager():
        break

    else:
        continue
