#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.5 Value Errors A) - Predict And Run
Author: Sidak Singh
Date: 2024-10-28
Assignment: 2.5 Value Errors A) - Predict And Run
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
# Task - Predict Run

try:
    age = int(input("Please enter your age: "))
    # asks for you age
except ValueError:
    print("Hey, that wasn't a number!")
    # prints for invalid input
else:
    print("I see that you are ", age," years old.")
    # prints for valid input

'''
Test Cases
Please enter your age:
Hey, that wasn't a number!

Please enter your age:
I see that you are ", age," years old.
'''
