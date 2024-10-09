'''
This is a title comment:
Ms. Anjali
Oct, 2024
Our First Tkinter graphics program
'''

#import the graphics library called Tkinter
from tkinter import *
# Create the main window called root
root = Tk()
# Set the window pixel size
root.geometry("400x300")
# Change the background color using configure
root.configure(bg='lightblue')
# this line created a Label object called my_label
my_label=Label(text="Hello!", bg='yellow', fg='red')
my_label2=Label(text="some text", bg='grey', fg='cyan')
my_label3=Label(text="some text", bg='grey', fg='cyan')
my_label.pack() # this is one way to 'output' an object to the window
my_label2.pack()
my_label3.pack()


# Run the application
root.mainloop()


'''
EX1: In the code above, line #11 and line #17 are examples of creating a variable, meaning we produce a value and assign it to the name

root = Tk()
#Name is root, value assigned is object of type Tk

my_label=Label(text="Hello!", bg='yellow', fg='red')
#name is my_label and value assigned is object of type Label

Notice that there are other variables(next to = operator), such as  text , bg etc.

Q1: what type of data is variable text? How do you know?
ANSWER: Text contains string data type since it is hoalding an array of characters which make a string ("Hello!)

Q2: what type of data is variable bg in line #17?
ANSWER: Bg is a type string variable becuase it is taking in a string as a color option.

Q3: What is the difference between '' and "" in Python?
ANSWER: single quotes or '' are used in python when a you need to store quotations with in text .

EX2: create code as follows and paste it just before line with mainloop():

1) Create a variable of type Label called my_label2, with some text in it
2) Display it to the window
3) Change label's colors to : gray and cyan

Q4: where is this new label placed? Do yo you have any control of placement?
ANSWER: The new label is placed below label1 and you do not have any controll over its placement

EX3: repeat the steps of EX2,  for my_label3

Q5: what do you notice?
ANSWER:


'''
