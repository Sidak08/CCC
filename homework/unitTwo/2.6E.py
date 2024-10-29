#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.6 Reading From A File -C) Make
Author: Sidak Singh
Date: 2024-10-29
Assignment: 2.6 Reading From A File -C) Make
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
first_names_file = "first_names.txt"
surnames_file = "surnames.txt"
print(f" files to choose: first_names, surnames")
chosen_file = f"{input("Please enter the file to read: ").strip().lower()}.txt"

if chosen_file != first_names_file and chosen_file != surnames_file:
    print("Invalid file name.")
try:
    with open(chosen_file, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file not found")

'''
Test casses
Files to choose: first_names, surnames
Please enter the file to read: first_names
alice
bob
charlie
diana
ethan

Files to choose: first_names, surnames
Please enter the file to read: pets
Invalid file name.
'''
