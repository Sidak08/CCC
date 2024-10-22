#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.3 Nesting - B) Investigate And Modify
Author: Sidak Singh
Date: 2024-10-22
Assignment: 2.3 Nesting - B) Investigate And Modify
'''
#-------------------------------------------------------------------------------------------------------------------
from tkinter import *
#-------------------------------------------------------------------------------------------------------------------
root = Tk()
my_label = Label(text="Result:", bg='yellow', fg='red', width=10)
my_label2 = Label(text="", bg='yellow', fg='red', width=10)
my_label3 = Label(text="Enter age:", bg='yellow', fg='red', width=10)
my_button = Button(text="Calculate", width=18)
my_text = Entry(width=10)
#-------------------------------------------------------------------------------------------------------------------
def function1():
    try:
        value = int(my_text.get())  # Convert input to an integer
        if value < 0 or value > 150:
            my_label2.configure(text="That's a funny age!")
        elif value < 2:
            my_label2.configure(text="infant")
        elif 2 <= value <= 3:
            my_label2.configure(text="toddler")
        elif 4 <= value <= 12:
            my_label2.configure(text="child")
        elif 13 <= value <= 17:
            my_label2.configure(text="teenager")
        elif 18 <= value <= 64:
            my_label2.configure(text="adult")
        else:  # value >= 65
            my_label2.configure(text="senior")
    except ValueError:
        my_label2.configure(text="Invalid input!")
#-------------------------------------------------------------------------------------------------------------------

# Main code
root.geometry("400x300")
root.configure(bg='lightblue')
my_label.grid(row=0, column=0)
my_label2.grid(row=0, column=1)
my_button.grid(row=1, column=0, columnspan=2)
my_label3.grid(row=2, column=0)
my_text.grid(row=2, column=1)

# Changing button's parameters
my_button.configure(command=function1)  # Executes function1 on button click

# Program execution
root.mainloop()

#Q2 It throws an error due to the negative value



'''
Test Cases
Input: 0
Expected Output: "That's a funny age!"
Input: 1
Expected Output: "infant"
Input: 2
Expected Output: "toddler"
Input: 3
Expected Output: "toddler"
Input: 4
Expected Output: "child"
Input: 10
Expected Output: "child"
Input: 13
Expected Output: "teenager"
Input: 17
Expected Output: "teenager"
Input: 18
Expected Output: "adult"
Input: 30
Expected Output: "adult"
Input: 65
Expected Output: "senior"
Input: 150
Expected Output: "That's a funny age!"
Input: 200
Expected Output: "That's a funny age!"

Invalid Inputs:
Input: -10
Expected Output: `"That's a funny age!"
Input: abc
Expected Output: "Invalid input!"
Input: 3.5
Expected Output: "Invalid input!"
Input: "" (empty input)
Expected Output: "Invalid input!"
'''
