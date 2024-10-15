#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.2.2 Random numbers - Make
Author: Sidak Singh
Date: 2024-10-15
Assignment: 2.2.2 Random numbers - Make
 '''
#-------------------------------------------------------------------------------------------------------------------
import random
#-------------------------------------------------------------------------------------------------------------------
# No global variables
#-------------------------------------------------------------------------------------------------------------------
# No Functions
#-------------------------------------------------------------------------------------------------------------------
# Task - Make

#Write a program that:

#Gets user input of two numbers.

num1 = int(input("Enter Your first number: "))
num2 = int(input("Enter Your Second number: "))

if (num2 <=num1):
    print("Please make sure you second number is bigger than your first number")
else:
    print("Your random number is", random.randint(num1, num2))


# Extra challenge - Build in a check for the input, if the second number is lower than or the same as the first number then output an error message. Else continue to the next steps.

#Generates a random number between the two numbers input.

# Outputs the random number generated.
#-------------------------------------------------------------------------------------------------------------------
# Place your test results below
'''

'''
