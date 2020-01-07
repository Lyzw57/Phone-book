# -phones.py *- coding: utf-8 -*-

import os
import csv

phones_list = []
name_index = 0
number_index = 1
phone_header = ["Name", "Phone Number"]

def is_choice_proper():
    choice = input("Which one")

def delete_phone():
    pass # TODO: Deleting phone number    

def edit_phone():
    pass # TODO: editing record

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
    pass # TODO: create a record

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
            delete_phone()
        elif choice == 's':
            show_phones()
        elif choice == 'e':
             edit_phone()
        else:
            print("Invalid choice.")
            
    save_phone_list()
    

# The following makes this program start running at main_loop()
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()
