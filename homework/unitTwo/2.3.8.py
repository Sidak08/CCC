#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.3 Nesting - B) Investigate And Modify
Author: Sidak Singh
Date: 2024-10-22
Assignment: 2.3 Nesting - B) Investigate And Modify
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
name = input("Enter your name: ").strip()
homeTown = input("Enter your hometown: ").strip()
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
# Ignore case for user input
if name.lower() == "dave":
    print("Hi there Dave, where are you from?")

    if homeTown.lower() == "seattle":
        occupation = input("What is your occupation? ").strip()
        if occupation.lower() == "drummer":
            print("Didn't you used to be in Nirvana?")
        else:
            print("Thought you were Dave Grohl there for a minute!")
    else:
        print("Hi Dave, shame you're not from Seattle.")

else:
    print("You're not Dave, where are you from?")

    if homeTown.lower() == "seattle":
        print("Well you might not be Dave, but at least you're from Seattle")
    else:
        print("You're not Dave, and you're not from Seattle!")


# How many selection statements are there in the code?
# There are 4 selection statements.

# How many of them are nested, and how can you tell?
# There are two nested statements. You can tell because the second if is indented under the first if.

# What would be the impact of swapping lines 9 and 12?
# If you swap lines 9 and 12 it would first checks if homeTown is "Seattle"
# before checking the name "Dave". This would show incorrect results

'''
No Test Cases
'''
