#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.5 Basic Exception Handling D) - Make
Author: Sidak Singh
Date: 2024-10-25
Assignment: 2.5 Basic Exception Handling D) - Make
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
# Task - Make

# Write a program that:

# Assigns a number into a suitable variable
# Checks that the variable has been assigned before printing it out.
# Displays an error message if the variable has not been assigned.
# Displays a success message if the program works correctly.

x = "hi"

try:
  print("success")
except NameError:
  print("The Var is not defined")
except:
    print("something went wrong")

'''
Test Cases
success

The Var is not defined
'''
