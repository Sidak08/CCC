#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.3 Boolean Operators -A) predict and run
Author: Sidak Singh
Date: 2024-10-17
Assignment: 2.3 Boolean Operators -A) predict and run
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Variables
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
num1 = 9

# False: num1 is not < 5
num1 < 5 and num1 < 10

# True: num1 is < 10 and < 20
num1 < 10 and num1 < 20

# True: num1 is not < 5 but is < 10
num1 < 5 or num1 < 10

# True: num1 is < 10 and < 20
num1 < 10 or num1 < 20

# True: num1 is not > 10
not(num1 > 10)

# False: num1 is 9
not(num1 == 9)

# False: num1 is equal to 9
not(num1 != 9)


name = "Dave"
homeTown = "Seattle"

# True: both conditions are met
if name == "Dave" and homeTown == "Seattle":
  print("Hi there Dave from Seattle!")
else:
  print("You're not Dave from Seattle!")

# True: at least one condition is met
if name == "Dave" or homeTown == "Seattle":
  print("You're either called Dave or you're from Seattle!")
else:
  print("You're not Dave, and you aren't from Seattle!")

'''
No TestCases
'''
