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
while True:
  try:
    num = int(input("Enter a whole int: "))
  except ValueError:
    print("Not an valid integer!")
  except:
    print("something is broken")
  else:
    print(f"thank you your number is {num}")
    break
'''
Test Cases

Enter a whole int: 23.5
Not an valid integer!
Enter a whole int: 60
thank you your number is 60
'''
