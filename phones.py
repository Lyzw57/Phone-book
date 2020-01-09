# -phones.py *- coding: utf-8 -*-

import os
import csv

phones_list = []
name_index = 0
number_index = 1
phone_header = ["Name", "Phone Number"]

def is_choice_proper(which: str) -> bool:
    """Checking if selected index is valid.

    Arguments:
        which str -- choice of record's index in str but had to be digit
    
    Returns:
        bool -- True if argument is digit and index exist, False otherwise
    """
    if not which.isdigit():
        print(f"{which} need to be number of record!")
        return False
    which = int(which)
    if which < 1 or which > len(phones_list):
        print(f"{which} need to be number of record!")
        return False
    return True

def select_which() -> int:
    """Takes phone's index from user and check if it is correct.
    
    Returns:
        int -- index of the record to edit or delete.
    """
    which = input("Which: ")
    if not is_choice_proper(which):
        return
    return int(which)

def delete_phone():
    """Delete selected record from phones_list
    """
    which = select_which()
    del(phones_list[which-1])
    print(f"Phone #{which} has been deleted.")

def edit_phone():
    """Edit record's name nad phone number, user can input it or press only enter to leave it unchagned.
    """
    which = select_which()
    phone = phones_list[which-1]

    new_name = input(f"Name: {phones_list[name_index]} | New name: ")
    if new_name == "":
        new_name = phone[name_index]
    
    new_number = input(f"Phone: {phones_list[number_index]} | New phone: ")
    if new_number == "":
        new_number = phone[number_index]

    phone = [new_name, new_number]
    phones_list[which-1] = phone

def save_phone_list(phones_list):
    """Save phones_list into csv file.
    """
    with open("data/myphons.csv", "w") as outfile:
        for phone in phones_list:
            csv.writer(outfile).writerow(phone)

def load_phone_list() -> list:
    """
    If path exist load phone list from simple csv file and store it into list of lists.
    
    Retunrs:
        list -- list of lists with pair: name and phone number.
    """
    if os.access("data/myphones.csv",os.F_OK):
        infile = open("data/myphones.csv")
        read_phones = csv.reader(infile)
        for row in read_phones:
            phones_list.append(row)
        infile.close()
    return phones_list

def show_phones():
    """Printing out all the phone numbers with its owners' names.
    """
    show_phone(phone_header, "")
    index = 1
    for phone in phones_list:
        show_phone(phone, index)
        index += 1
    print()

def show_phone(phone, index):
    """
    Printing out formatted record with its index number.
    
    Arguments:
        phone list -- list contaning name and phone number
        index int -- index no. of the record
    """
    output_str = f"{index:>3} {phone[name_index]:<20} {phone[number_index]:>16}"
    print(output_str)

def create_phone():
    """Takes data from user and store it as new record in phones_list
    """
    print("Enter the data for a new phone:")
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    phone = [name, phone_number]
    phones_list.append(phone)

def menu_choice(choice_dict):
    """ Find out what the user wants to do next. """
    print("Choose one of the following options?")
    print("   s) Show")
    print("   n) New")
    print("   d) Delete")
    print("   e) Edit")
    print("   q) Quit")
    choice = input("Choice: ")    
    if choice.lower() in choice_dict.keys():
        return choice.lower()
    else:
        print(choice +"?" + " That is an invalid option!!!")
        return None


def main_loop():
    choice_dict = {
    'n': create_phone,
    'd': delete_phone,
    's': show_phones,
    'e': edit_phone,
    'q': "q"
    }

    phones_list = load_phone_list()
    
    while True:
        choice = menu_choice(choice_dict)
        if choice == "q":
            break
        choice_dict[choice]()

    save_phone_list(phones_list)
                

# The following makes this program start running at main_loop()
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()
