#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.6 Reading From A File - B) Investigate And Modify
Author: Sidak Singh
Date: 2024-10-28
Assignment: 2.6 Reading From A File - B) Investigate And Modify
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
'''
What is the name of the variable used to store the file contents?
The variable is bandFile.

What does 'r' on line 5 do?
The 'r' stands for read-only mode.

How many variables are used in the code? What are they called?
There are two variables used.

What is the file extension of the file used?
the file extension is .txt.

'''
file_choice = input("Which file do you want to open? (bands or singers): ").lower()
file_name = file_choice + ".txt"
chosenFile = open(file_name, "r")
for line in chosenFile:
    print(line)
chosenFile.close()

'''
Test Cases

Which file do you want to open? (bands or singers): Bands
test
something random
something else

Which file do you want to open? (bands or singers): test
FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
'''
