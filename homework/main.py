#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.1.0 Input, Variable and Output review
Author: Sidak Singh
Date: 2024-10-05
Assignment: 2.1.0 Input, Variable and Output review - Pick 3 questions and answer them.
 '''
#-------------------------------------------------------------------------------------------------------------------
from tkinter import *
#-------------------------------------------------------------------------------------------------------------------
# No global variables
#-------------------------------------------------------------------------------------------------------------------
#No Fuctions
#-------------------------------------------------------------------------------------------------------------------

# Create the main window called root
root = Tk()

# Set the window pixel size
root.geometry("400x300")

root.configure(bg='lightblue')

my_label=Label(text="Hello!", bg='lightgreen', fg='magenta') # this line created a Label object called my_label
my_label.pack() # this is one way to 'output' an object to the window
#note if you delete the previous line, label will not be displayed - try!

# Run the application
root.mainloop()


#Q1: what does bg do? Change it to lightgreen
#answer: The bg argument changes the background color for the text.
#Q2: what does fg do? Change it to magenta
#answer: The fg argument changes the text color.


#-------------------------------------------------------------------------------------------------------------------
# Place your test results below
'''
Test cases and results:
No test cases
'''
