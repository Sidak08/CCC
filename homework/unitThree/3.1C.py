#-------------------------------------------------------------------------------------------------------------------
'''
Title: 3.1 Homework Task - Calculator
Author: Sidak Singh
Date: 2024-10-30
Assignment: 3.1 Homework Task - Calculator
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
def add(num1,num2):
  return(num1 + num2)

def subtract(num1,num2):
  return(num1 - num2)

def multiply(num1,num2):
  return(num1 * num2)

def divide(num1,num2):
  return(num1 / num2)
#-------------------------------------------------------------------------------------------------------------------

userNum1 = int(input("Enter a number"))
userNum2 = int(input("Enter another number"))

choice = int(input("Enter 1 to add, 2 to subtract, 3 to multiply or 4 to divide"))

if choice == 1:
  outputNum = add(userNum1, userNum2)
elif choice == 2:
  outputNum = subtract(userNum1, userNum2)
elif choice == 3:
  outputNum = multiply(userNum1, userNum2)
else:
  outputNum = divide(userNum1, userNum2)

print(outputNum)
