#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.2.3 Modulus - Make
Author: Sidak Singh
Date: 2024-10-16
Assignment: 2.2.3 Modulus - Make
 '''
#-------------------------------------------------------------------------------------------------------------------
# No Imports
#-------------------------------------------------------------------------------------------------------------------
nameOne = input("Enter the first name: ")
nameTwo = input("Enter the second name: ")

mod = (len(nameOne) + len(nameTwo)) % 3
#-------------------------------------------------------------------------------------------------------------------
# No functions
#-------------------------------------------------------------------------------------------------------------------
if (mod == 0) :
    print("You are very compatible")
elif (mod == 1):
    print("You might have a chance together")
else :
    print("You are not compatible.")
#-------------------------------------------------------------------------------------------------------------------
# Place your test results below
'''
Enter the first name: sidak
Enter the second name: test
You are very compatible

Enter the first name: Sidak
Enter the second name: Test1
You might have a chance together

Enter the first name: Sidak
Enter the second name: Test12
You are not compatible.
'''
