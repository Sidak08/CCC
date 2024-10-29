#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.6 Writing/Appending To A File - A)Predict And Run
Author: Sidak Singh
Date: 2024-10-29
Assignment: 2.6 Writing/Appending To A File - A)Predict And Run
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
# Define function to write name

# Task - Investigate

# Answer the questions about the code below.

def saveStudent():
  myFile = open('Students.txt','a')  #Creates/Opens Students.txt with append permissions

  print('Enter Student Details: ')
  while True:
    name = input('Student name: ')
    line = name + '\n'
    myFile.write(line)

    print('Enter another student? Type quit or no to quit')
    choice = input()

    if choice.lower() == 'no' or choice.lower() == 'quit':
      print('Goodbye!')
      break


  myFile.close()

saveStudent()

# What permissions are set when the 'students.txt' file is opened?
# The file is opened with append permissions ('a'). Which lets it add items.

# Why are these permissions suitable?
# Because the program only wants to a name not rewite the file or view it

# What is the purpose of the '\n' code on line 11?
# it is to make sure the next name is a new line

# What is the purpose of the 'choice' variable?
# to ask the user if they want to add one more name or not

# EXTRA RESEARCH QUESTIONS - we've not been through these coding techniques, you'll need to research to help you answer these questions.

# How does a 'while True' loop work?
# it is a infinite loop which stops when a return or break is triggered

# What does 'break' on line 19 do?
# stop the infinite loop

'''
Test casses
'''
