#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.6 Writing/Appending To A File -d) Make
Author: Sidak Singh
Date: 2024-10-29
Assignment: 2.6 Writing/Appending To A File -d) Make
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
def add_singer(singer):
    with open('singers.txt', 'a') as file:
        file.write(singer + '\n')

def add_band(band):
    with open('bands.txt', 'a') as file:
        file.write(band + '\n')

def read_singers():
    print("\nSingers List:")
    with open('singers.txt', 'r') as file:
        content = file.readlines()
        for line in content:
            print(line.strip())


def read_bands():
    print("\nBands List:")
    with open('bands.txt', 'r') as file:
        content = file.readlines()
        for line in content:
            print(line.strip())
#-------------------------------------------------------------------------------------------------------------------
while True:
    read_singers()
    read_bands()

    choice = input("\nwant to add a singer (1) or a band (2)? ").strip()

    if choice == '1':
        singer = input("Enter name: ").strip()
        add_singer(singer)
        print(f"Added singer: {singer}")
    elif choice == '2':
        band = input("Enter name: ").strip()
        add_band(band)
        print(f"Added band: {band}")
    else:
        print("Invalid input.")
        continue
    continue_choice = input("want to continue (c) or quit (q)? ").strip().lower()
    if continue_choice == 'q':
        print("Goodbye!")
        break
    elif continue_choice != 'c':
        print("Invalid input. Please type 'c' to continue or 'q' to quit.")

'''
Test casses
Singers List:
Bands List:
want to add a singer (1) or a band (2)? 1
Enter name: Alice
Added singer: Alice
want to continue (c) or quit (q)? c
want to add a singer (1) or a band (2)? 1
Enter name: Bob
Added singer: Bob
want to add a singer (1) or a band (2)? 1
Enter name: Bob
Added singer: Bob
want to continue (c) or quit (q)? c

want to add a singer (1) or a band (2)? 2
Enter name: The Rockers
Added band: The Rockers
want to continue (c) or quit (q)? c
'''
