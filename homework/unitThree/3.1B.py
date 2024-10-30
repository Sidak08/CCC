#-------------------------------------------------------------------------------------------------------------------
'''
Title: 3.1 subroutines With Input & Output
Author: Sidak Singh
Date: 2024-10-30
Assignment: 3.1 subroutines With Input & Output
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------

def maths1():
  num1 = 50
  num2 = 5
  return num1 + num2

def maths2():
  num1 = 50
  num2 = 5
  return num1 - num2

def maths3():
  num1 = 50
  num2 = 5
  return num1 * num2

outputNum = maths2()
print(outputNum)
# output 45 cause 50 - 4 is 45 and only math2 is called.

def multiplier():
  num1 = int(input("First Number"))
  num2 = int(input("Second Number"))
  return num1 * num2

outputNum = multiplier()
print(outputNum)
