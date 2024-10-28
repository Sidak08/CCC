#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.4 E) Loops and graphics -Solution
Author: Sidak Singh
Date: 2024-10-25
Assignment: 2.4 E) Loops and graphics -Solution
'''
#-------------------------------------------------------------------------------------------------------------------
from tkinter import *
import time
#-------------------------------------------------------------------------------------------------------------------
window = Tk()
C = Canvas(window, bg="cyan", height=300, width=300)
btn = Button(window, text = "Click to draw!" ,fg = "Yellow", bg="black")
btn2 = Button(window, text = "Click to erase!" ,fg = "Yellow", bg="black")
#-------------------------------------------------------------------------------------------------------------------
def my_first_drawing():
  global C

  my_first_oval = C.create_oval(0, 0, 100,
                     200,fill="yellow")

  my_first_arc = C.create_arc(150, 0, 100,
                   200,start=270,
                   extent=90, fill="red")

def clear_canvas():
  global C
  C.configure(bg="cyan")
  C.delete('all')
def draw_line():
  global C
  global window
  for i in range(0,600):
    C.create_line(i,0,0,i, fill="lightgreen")
    time.sleep(i/100000)
    window.update()
def draw_other_line():
  global C
  global window
  for i in range(0,600):
    C.create_line(300-i,0,300,i, fill="red")
    time.sleep(i/100000)
    window.update()
def draw_vertical_line():
  global C
  global window
  for i in range(0, 300):
    C.create_line(i,0,i,300, fill="orange")
    time.sleep(i/100000)# pause
    window.update()
def draw_square_pattern():
  global C
  global window
  for i in range(0, 150):
    C.create_rectangle(150-i,150-i,150+i,150+i, fill="blue")
    time.sleep(i/10000)# pause
    window.update()


def refresh_window():
  global window
  window.configure(bg="blue")
#-------------------------------------------------------------------------------------------------------------------
window.geometry("600x600")
window.configure(bg="grey")
C.place(x=300, y=300)
btn.place(x=0, y=100)
btn2.place(x=100, y=100)
btn.configure(command=draw_square_pattern)
btn2.configure(command=clear_canvas)
mainloop()
'''
No Test Casses
'''
