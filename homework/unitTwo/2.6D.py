#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.6 Reading From A File -A)Predict And Run
Author: Sidak Singh
Date: 2024-10-28
Assignment: 2.6 Reading From A File -A)Predict And Run
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------

myFile = open("singers.txt", "r") #It lets the program acces the elemenets inside the file
for line in myFile: # Goes through each line
  print(line) # Prints every line
myFile.close() # Removes acces to the file

'''
Test Cases
'''
