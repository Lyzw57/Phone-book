"""
A SMALL DATABASE APPLICATION USING WHAT WE'VE LEARNED.

The following uses a CSV file to store the data for a small telephone directory.
It is menu driven. That is, it presents a menu of choices. These choices are
to show the whole directory, create a new entry for the directory, delete an
entry from the directory, and edit an entry in the directory.
"""

# -phones.py *- coding: utf-8 -*-
"""
This was written as a basic program that did little at first.  Additional
features were added until it was finished.
Here is a first version.
phones.py
Version 1 -- builds the menu -- functions are empty
"""
import os
import csv

phones_list = []
name_index = 0
number_index = 1
phone_header = ["Name", "Phone Number"]

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
    pass # TODO: display all phone number with its owners' names

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
    print(phones_list)
    
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
