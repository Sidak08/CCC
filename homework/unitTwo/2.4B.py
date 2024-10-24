#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.4 Validation B) Investigate and Modify
Author: Sidak Singh
Date: 2024-10-24
Assignment: 2.4 Validation B) Investigate and Modify
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
'''
Where is the iteration in the code?
it is the while loop. it checks if num1 is between 50 and 100 and if not it keep asking for a valid input

How many conditions are there in the code? What are they?
The two main conditions are:
num1 < 50 too small
num1 > 100 too large

Where is the nesting in the code?
in the if statement inside the while loop.

Why are lines 12 and 15 indented?
they are part of the while loop.

Why is line 13 indented twice?
it is inside the if statement which is inside the while loop.

What would be the impact of swapping the 'or' on line 10 for an 'and'?
the loop would want a number which is smaller than 50 and bigger than 100; which is not possible so it will not run.
'''

print("Enter the number of the month you were born (1-12):")
month = int(input())


while month < 1 or month > 12:
    if month < 1:
        print("Invalid number, too small, try again.")
    elif month > 12:
        print("Invalid number, too large, try again.")
    month = int(input())

print("You entered a valid month:", month)

'''
Test Cases

Please enter your usernamesidak
Username incorrect, please try again.dave
Username accepted.
Enter a number between 1 and 1090
Invalid number, please try again-92
Invalid number, please try again5
Input accepted.
'''
