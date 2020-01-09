# -phones.py *- coding: utf-8 -*-

import os
import csv

phones_list = []
name_index = 0
number_index = 1
phone_header = ["Name", "Phone Number"]

def is_choice_proper(which: str):
    """Checking if selected index is valid.

    Arguments:
        which {str} -- choice of record's index in str but had to be digit
    
    Returns:
        {bool} -- True if argument is digit and index exist, False otherwise
    """
    # FIXME: i don't like it. I'd like to change this funcion and remove changing to int eery time aswell.
    if not which.isdigit():
        print(f"{which} need to be number of record!")
        return False
    which = int(which)
    if which < 1 or which > len(phones_list):
        print(f"{which} need to be number of record!")
        return False
    return True

def delete_phone(which: str):
    """delete selected record from phones_list
    
    Arguments:
        which {str} -- record's index choice
    """
    if not is_choice_proper(which):
        return
    which = int(which) # FIXME: to change, it should be done in function.
    del(phones_list[which-1])
    print(f"Phone #{which} has been deleted.")

def edit_phone(which: str):
    """Edit record's name nad phone number, user can input it or press only enter to leave it unchagned.
    
    Arguments:
        which {str} -- index of record to edit
    """
    if not is_choice_proper(which):
        return
    which = int(which) # FIXME: to change, it should be done in function.

    phone = phones_list[which-1]

    new_name = input(f"Name: {phones_list[name_index]} | New name: ")
    if new_name == "":
        new_name = phone[name_index]
    
    new_number = input(f"Phone: {phones_list[number_index]} | New phone: ")
    if new_number == "":
        new_number = phone[number_index]

    phone = [new_name, new_number]
    phones_list[which-1] = phone

def save_phone_list():
    pass # TODO: save phone list

def load_phone_list():
    """
    If path exist load phone list from simple csv file and store it into list of lists.
    """
    if os.access("data/myphones.csv",os.F_OK):
        infile = open("data/myphones.csv")
        read_phones = csv.reader(infile)
        for row in read_phones:
            phones_list.append(row)
        infile.close() 

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
        phone {list} -- list contaning name and phone number
        index {int} -- index no. of the record
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

def menu_choice():
    """ Find out what the user wants to do next. """
    print("Choose one of the following options?")
    print("   s) Show")
    print("   n) New")
    print("   d) Delete")
    print("   e) Edit")
    print("   q) Quit")
    choice = input("Choice: ")    
    if choice.lower() in ['n','d', 's','e', 'q']:
        return choice.lower()
    else:
        print(choice +"?" + " That is an invalid option!!!")
        return None


def main_loop():
    
    load_phone_list()
    
    while True:
        choice = menu_choice()
        if choice == None:
            continue
        if choice == 'q':
            print( "Exiting...")
            break     # jump out of while loop
        elif choice == 'n':
            create_phone()
        elif choice == 'd':
            which = input("Which phone do you want to delete? ")# FIXME: it should be in function
            delete_phone(which)
        elif choice == 's':
            show_phones()
        elif choice == 'e':
            which = input("Which phone do you want to edit? ") # FIXME: it should be in function
            edit_phone(which)
        else:
            print("Invalid choice.")
            
    save_phone_list()
    

# The following makes this program start running at main_loop()
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()
