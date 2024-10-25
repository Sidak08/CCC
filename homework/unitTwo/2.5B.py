#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.5 Basic Exception Handling A) -Predict And Run
Author: Sidak Singh
Date: 2024-10-25
Assignment: 2.5 Basic Exception Handling A) -Predict And Run
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
try:
  print(name)
except NameError:
  print("The variable is not defined")
except:
  print("Something else went wrong.")
else:
  print("Nothing went wrong")
finally:
  print("The try except has finished")

# What is the variable in the code?
# Name

# What purpose does the 'try' have in the code
# to check if an error occured

# What does 'NameError' mean on line 7?
# checks if everything is defined

# Why are there two 'except' commands?
# the first one checks for defination errors while the other checks for general errors

# What would happen if lines 10 and 12 were swapped?
# It would print nothing went wrong when a error occured

'''
Test Cases

'''
