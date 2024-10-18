#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.2.3 Modulus - Make
Author: Sidak Singh
Date: 2024-10-05
Assignment: 2.2.3 Modulus - Make
 '''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
# No global variables
#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
# Task - Make - The Love Calculator

# Write a program that:

# Gets two users to input their names.
# Calulates the number of characters in each name and adds them together.
# Calculates the modulus of the total characters in both names divided by 3.
# If the modulus is 0, output a message saying that the couple are very compatible.
# If the modulus is 1, output a message saying that the couple are might have a chance together.
# If the modulus is 2, output a message saying that the couple aren't compatible.

nameOne = input("Enter the first name: ")
nameTwo = input("Enter the second name: ")

mod = (len(nameOne) + len(nameTwo)) % 3

if (mod == 0) :
    print("You are very compatible")
elif (mod == 1):
    print("You might have a chance together")
else :
    print("You are not compatible.")
#-------------------------------------------------------------------------------------------------------------------
# Place your test results below
'''

'''
