#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.1.0 Input, Variable and Output review
Author: Sidak Singh
Date: 2024-10-05
Assignment: 2.1.0 Input, Variable and Output review - Pick 3 questions and answer them.
 '''
#-------------------------------------------------------------------------------------------------------------------
# No imports.
#-------------------------------------------------------------------------------------------------------------------
# No global variables
#-------------------------------------------------------------------------------------------------------------------
def add_numbers():
    num1 = float(input("Num 1:"))
    num2 = float(input("Num 2:"))
    num3 = float(input("Num 3:"))
    print("Total is", num1 + num2 + num3)

def find_average():
    num1 = float(input("Num 1:"))
    num2 = float(input("Num 2:"))
    num3 = float(input("Num 3:"))
    print("The average is", (num1 + num2 + num3) / 3)

def find_averageMark():
    num1 = float(input("Mark 1:"))
    num2 = float(input("Mark 2:"))
    num3 = float(input("Mark 3:"))
    num4 = float(input("Mark 4:"))
    print("The average is", (num1 + num2 + num3 + num4) / 4)


#-------------------------------------------------------------------------------------------------------------------
#Q1
add_numbers()
# This will add three numbers given by the user.
# No you dont need brackets since the answer would be the same without the order of operations.

#Q2
find_average()
# This will find the average of the three numbers.

#Q3
find_averageMark()
# This will find the average mark between 4 courses.

#-------------------------------------------------------------------------------------------------------------------
# Place your test results below
'''
Test cases and results:

Question 1:
Input
Num 1: 1
Num 2: 2
Num 3: 3
Output
('Total is', 6.0)

Test Case 2:
Input
Num 1: 1
Num 2: 40
Num 3: 2
Output
('The average is', 14.3333333333)

Test Case 3:
Input
Mark 1: 80
Mark 2: 98
Mark 3: 95
Mark 4: 93
Output
('The average is', 91.5)
'''
