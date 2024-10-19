#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.3 Boolean Operators- C) Make
Author: Sidak Singh
Date: 2024-10-18
Assignment: 2.3 Boolean Operators- C) Make
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
my_eye_color = "brown"
my_hair_color = "black"
my_num_pets = 0

correct_guesses = 0
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
user_eye_color = input("Guess my eye color: ").lower()
user_hair_color = input("Guess my hair color: ").lower()
user_num_pets = int(input("Guess how many pets I have: "))

if user_eye_color == my_eye_color:
    correct_guesses += 1
if user_hair_color == my_hair_color:
    correct_guesses += 1
if user_num_pets == my_num_pets:
    correct_guesses += 1

if correct_guesses == 3:
    print("You guessed them all!")
elif correct_guesses > 0:
    print("You got some, but not all correct.")
else:
    print("You didn't get any right.")

'''
Test Cases

Guess my eye color: brown
Guess my hair color: black
Guess how many pets I have: 0
You guessed them all!

Guess my eye color: blue
Guess my hair color: red
Guess how many pets I have: 0
You got some, but not all correct.

Guess my eye color: green
Guess my hair color: blue
Guess how many pets I have: 98
You didn't get any right.
'''
