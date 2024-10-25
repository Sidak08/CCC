#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.5 Basic Exception Handling A) -Predict And Run
Author: Sidak Singh
Date: 2024-10-25
Assignment: 2.5 Basic Exception Handling A) -Predict And Run
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
# Task - Add comments to the code to prdict how it will run.

# Run the code to check if you were correct.

def HelloWorld():
  print("Hello World")


def Greeting1():
  name = "Dave"
  print("Hello " + name)


def Greeting2(name):
  print("Hello " + name)


def ErrorMessage():
  print("There has been an error")


try:
  HelloWorld()
  #prints hello world
except:
  ErrorMessage()
  # does not print

try:
  Greeting1()
  #prints hello dave
except:
  ErrorMessage()
  #Does not print

try:
  Greeting2(name)
  #suppose to print hello (name argument value) but throws error
except:
  ErrorMessage()
  #print error
'''
Test Cases

'''
