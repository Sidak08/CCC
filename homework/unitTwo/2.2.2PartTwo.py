#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.2.1 Data types - MAKE
Author: Sidak Singh
Date: 2024-10-05
Assignment: 2.2.1 Data types - MAKE
 '''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
# No global variables
#-------------------------------------------------------------------------------------------------------------------
def calcAreaTriangle (base, height):
  return (base * height) / 2

def takeInput():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    print("The area of the triangle is", calcAreaTriangle(base, height))
#-------------------------------------------------------------------------------------------------------------------

takeInput()

#-------------------------------------------------------------------------------------------------------------------
# Place your test results below
'''
Enter the base of the triangle: 6
Enter the height of the triangle: 5
The area of the triangle is 15.0

Enter the base of the triangle: 50
Enter the height of the triangle: 29
The area of the triangle is 725.0

Enter the base of the triangle: 5.3
Enter the height of the triangle: 90.468
The area of the triangle is 239.7402
'''
