#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.5 Basic Exception Handling C) -Modify
Author: Sidak Singh
Date: 2024-10-25
Assignment: 2.5 Basic Exception Handling C) -Modify
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
# Task - Modify

# Adapt & complete the code below so that:

# It checks for a name error and displays a suitable error message.

# It checks for all other errors and displays a suitable error message

# It diplays a suitable message once the try/except has finished regardless of whether there has been an ArithmeticError

try:
  print(x)
except NameError:
  print("The Var is not defined")
except:
    print("something went wrong")
finally:
    print("done")
'''
Test Cases

'''
