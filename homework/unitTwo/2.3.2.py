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
# Get user input
name = input("Enter your name: ")
homeTown = input("Enter your hometown: ")

# Ignore case
name = name.lower()
homeTown = homeTown.lower()

# Combined selection statement
if name == "dave" and homeTown == "seattle":
    print("Hi there Dave from Seattle!")
elif name == "dave" or homeTown == "seattle":
    print("You're either called Dave or you're from Seattle!")
else:
    print("You're not Dave from Seattle!")

# What would the outputs be for Kurt From Seattle?
# "You're not Dave from Seattle!"
# You're either called Dave or you're from Seattle!

# What would the outputs be for Krist from Chicago?
# "You're not Dave from Seattle!"
# "You're not Dave, and you aren't from Seattle!"

# What would the effect be of changing the 'and' on line 8 to an 'or'?
# "Hi there Dave from Seattle!"

'''
TestCases
Enter your name: Dave
Enter your hometown: seattle
Hi there Dave from Seattle!

Enter your name: sidak
Enter your hometown: seattle
You're either called Dave or you're from Seattle!

Enter your name: sidak
Enter your hometown: delli
You're not Dave from Seattle!
'''
