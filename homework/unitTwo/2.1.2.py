'''
This is a title comment:
Ms. Arora
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
my_label.pack() # this is one way to 'output' an object to the window


# Run the application
root.mainloop()

'''

EX1: how do we enter data into window? - Using Entry object!

Insert the following 5 lines of code just before the mainloop() line

code:

text_box=Entry()
#this created a variable of type Entry(aka textbox)
text_box.pack()
#this line displays the texbox in the window
# note that we can type into textbox but nothing happens, stay tuned for more


EX2: let's create a button, insert the following 4 lines of code just before the mainloop() line

code:

my_button= Button(text="Click me!")
#explain this line yourself:
my_button.pack()
#explain this line yourself:

EX3: we can set width of object after crearing them, using configure function:

1)place this line after packing the label
my_label.configure(width=5) #width is a parameter here
#width of label is now 5

2) change the with of textbox and button in same fashion


EX4: Now, let's learn a different way to layout or 'output' our graphics variables, instead of pack() we will use grid():

complete the following:

1) for label, replace line with pack() as follows:
my_label.grid(row=0, column=0)
2) for textbox, replace line with pack() as follows:
text_box.grid(row=1, column=1)
3) for button, replace line with pack() as follows:
my_button.grid(row=0, column=2)

Q1: describe what you notice when you run the code?
ANSWER:
Q2: what is parameter row for? what is smallest value it can be?
ANSWER:
Q3:what is parameter column for? what is smallest value for it?
ANSWER:

FINAL note: instead of pack() and grid() function, one can also use place(x,y) - reseach it

'''
