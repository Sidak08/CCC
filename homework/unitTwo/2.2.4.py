#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.2.4 - operators with Tkinter graphics
Author: Sidak Singh
Date: 2024-10-17
Assignment: 2.2.4 - operators with Tkinter graphics
 '''
#-------------------------------------------------------------------------------------------------------------------
import random
from tkinter import *
#-------------------------------------------------------------------------------------------------------------------
root = Tk()
#-------------------------------------------------------------------------------------------------------------------
#second label when button is clicked
def function2():
    try:
        # Evaluating the expression from the textbox and updating the label
        my_label2.configure(text=eval(my_text.get()))
    except Exception as e:
        my_label2.configure(text="Error")

# clear second label
def clear_label():
    my_label2.configure(text="0")
#-------------------------------------------------------------------------------------------------------------------
root.geometry("400x300")
root.configure(bg='lightblue')

# display word result
my_label = Label(text="Result", bg='yellow', fg='red')
my_label.pack()

# second label show answer
my_label2 = Label(text="0", bg='lightgreen', fg='black')
my_label2.pack()

# Creating a textbox for input
my_text = Entry(root)
my_text.pack()

# button which triggers the calculation
my_button = Button(text="Calculate")
my_button.pack()

# make the button to call function2
my_button.configure(command=function2)

# clear button
clear_button = Button(text="Clear", command=clear_label)
clear_button.pack()


# Running the main loopi loop
root.mainloop()
'''
TestCases and questions
1: What happens when you press the button?
ANSWER: The label2 will display "Error".

Q2: Now type something in the text box and click the button. What happens?
ANSWER: The label2 will show the result.

Q3: Test the code now! What happens?
ANSWER: The label2 displays the correct answer or the error.

Testcases and there results:
a) Result: 4
ANSWERS: 2 + 2

b) Result: 0
ANSWERS: 2 - 2

c) Result: 1/2
ANSWERS: 1 / 2

d) Result: -2
ANSWERS: -2
'''
