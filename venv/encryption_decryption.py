from data import textfile_array, month_to_days
from edit_text_files import *


def encryption(phrase):

    # Makes empty chain
    encryption_chain = ""

    # For loop to edit each letter and add fake letters.
    for letter in phrase:

        # Array characters contains the fake characters
        characters = ["&", "^", "#", "~"]

        # If the character entered by the user is between A and z we get two paths.
        # If user has entered an alphabet

        # Converting one letter to another.
        # Alphabet to number
        alphabet_number = ord(letter)

        # Alphabet number to new number
        new_number = alphabet_number - 6

        # New number to new alphabet
        new_alphabet = chr(new_number)

        # Add new alphabet and fake alphabet to encryption chain
        encryption_chain += new_alphabet + str(random.choice(characters))

    # returns string "encryption_chain" contain encrypted text.
    return str(encryption_chain)


# Decrypts password in "password.txt" to compare it to the input user entered when asked for password. Called whenever user inputs a password.
def decryption_pass():

    string = list_file_data('password.txt')[0]
    decryption_chain = ""
    for letter in string:

        # For loop to edit each letter and delete fake letters.
        # Array characters contains the fake characters
        characters = ("&", "^", "#", "~")

        if letter not in characters:
            # Converting one letter to another.
            # Alphabet to number
            alphabet_number = ord(letter)

            # Alphabet number to old number
            old_number = alphabet_number + 6

            # Old number to old alphabet
            old_alphabet = chr(old_number)

            # Old alphabet to string
            old_alphabet = str(old_alphabet)

            # Add old alphabet to decryption chain
            decryption_chain = decryption_chain + old_alphabet

    # Returns decrypted password
    return decryption_chain


# Decrypter for thoughts that a user records and prints decrypted thoughts.
def decryption():

    # Create list that stores encrypted data
    encrypted_data_list = []
    # Initialize variable
    element = 0

    # Adds each element in thoughts.txt to encrypted_data_list according to line number
    while element < len(list_file_data('thoughts.txt')):
        element = element+1
        encrypted_data_list.append(element)

    # Create list that stores decrypted data
    decrypted_list = []

    for each_element_ in encrypted_data_list:
            decryption_chain = ""
            for letter in str(read_file_line('thoughts.txt', each_element_)):

                # For loop to edit each letter and delete fake letters.
                # Array characters contains the fake characters
                characters = ("&", "^", "#", "~")

                if letter not in characters:
                    # Converting one letter to another.
                    # Alphabet to number
                    alphabet_number = ord(letter)

                    # Alphabet number to old number
                    old_number = alphabet_number + 6

                    # Old number to old alphabet
                    old_alphabet = chr(old_number)

                    # Old alphabet to string
                    old_alphabet = str(old_alphabet)

                    # Add old alphabet to decryption chain
                    decryption_chain = decryption_chain + old_alphabet
            # Add decrypted chain to decrypted list
            decrypted_list.append(str(decryption_chain))

    # Prints out all decrypted data
    for string in decrypted_list:
        string = string.rstrip('\n')
        print(string)

