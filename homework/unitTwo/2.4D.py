#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.4 Validation D) Make challenge
Author: Sidak Singh
Date: 2024-10-24
Assignment: 2.4 Validation D) Make challenge
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
print("Choose a new password (must be 8 characters long)")

while True:
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Password too short. Please enter at least 8 characters.")
        continue

    confirm_password = input("Confirm your password: ")
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
    else:
        break

print("Password successfully set!")

'''
Test Cases

Choose a new password (must be 8 characters long)
Enter your password: sidak
Password too short. Please enter at least 8 characters.
Enter your password: sidakqwe
Confirm your password: sidaktyr
Passwords do not match. Please try again.
Enter your password: sidakque
Confirm your password: sidakque
Password successfully set!
'''
