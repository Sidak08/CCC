#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.4 Validation c) Make
Author: Sidak Singh
Date: 2024-10-24
Assignment: 2.4 Validation c) Make
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
print("Choose a new password!")
password = input("Enter your password: ")
confirm_password = input("Confirm your password: ")

while password != confirm_password:
    print("Passwords do not match. Please try again.")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

print("Password successfully set!")

'''
Test Cases

Choose a new password:
Enter your password: Sidak
Confirm your password: sidfak
Passwords do not match. Please try again.
Enter your password: Sidak
Confirm your password: Sidak
Password successfully set!
'''
