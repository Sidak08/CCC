#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.5 Basic Exception Handling C) -Modify
Author: Sidak Singh
Date: 2024-10-25
Assignment: 2.5 Basic Exception Handling C) -Modify
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
def userInput ():
    while True:
        try:
            num = int(input("Enter a whole int: "))
        except ValueError:
            print("Not an valid integer!")
        except:
            print("something is broken")
        else:
            return num

def adder(num1, num2):
    return num1 + num2
#-------------------------------------------------------------------------------------------------------------------
num1 = userInput()
num2 = userInput()
sum = adder(num1, num2)

print(f"Your sum is {sum}")

'''
Test Cases

Enter a whole int: 33
Enter a whole int: 235.4
Not an valid integer!
Enter a whole int: 23
Your sum is 56
'''
