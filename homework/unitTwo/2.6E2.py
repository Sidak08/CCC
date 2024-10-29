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
def WriteToFile():
    # Open a file in write mode ("w")
    myFile = open("Writing.txt", "w")
    # Write name "Bob"
    myFile.write("Bob")
    # Close the file
    myFile.close()

#function to append a name
def AppendToFile(name):
    # Open the file in append mode ("a")
    myFile = open("Appending.txt", "a")
    # Write the name and newline character.
    myFile.write(name + "\n")
    # Close file
    myFile.close()

# Call the function
WriteToFile()

# Check the second fuction with the name Dave
name = "Dave"
AppendToFile(name)

# Check the second fuction the name Freddie
name = "Freddie"
AppendToFile(name)

'''
Test casses
'''
