#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.3 Numbers in a Range - A) Predict And Run
Author: Sidak Singh
Date: 2024-10-18
Assignment: 2.3 Numbers in a Range - A) Predict And Run
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
birthMonth = int(input("Enter the number of the month in which you were born."))
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
if birthMonth >= 1 and birthMonth <=12:
  print("Thanks")
  #if the month is higher or equall to 1 and lower than 12 it will print Thanks
else:
  print("That's not a month!")
  #if not it will print That's not a month!
'''
Test Cases

Enter the number of the month in which you were born.14
That's not a month!

Enter the number of the month in which you were born.12
Thanks
'''
