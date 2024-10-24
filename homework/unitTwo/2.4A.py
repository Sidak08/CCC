#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.4 Validation A) Predict and Run
Author: Sidak Singh
Date: 2024-10-24
Assignment: 2.4 Validation A) Predict and Run
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
correctUserName = "dave" #correct username option

userName = input("Please enter your username").lower() #asks to enter a username

while userName != correctUserName: # checks if the user name is correct or not
  userName = input("Username incorrect, please try again.") # ask for another username if the previous one is incorrect

print("Username accepted.") # print when the correct username has been entered

# Example 2

num1 = int(input("Enter a number between 1 and 10")) # asks to enter a number between 1 - 10

while num1 < 1 or num1 > 10: # check if the number is valid
  num1 = int(input("Invalid number, please try again")) # if the number is invalid it askes for another number

print("Input accepted.") #print when the correct number is inputted

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
