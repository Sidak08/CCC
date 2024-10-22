#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.3 Numbers in a Range - C)Make
Author: Sidak Singh
Date: 2024-10-21
Assignment: 2.3 Numbers in a Range - C)Make
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
percentage = input("Enter your test percentage: ")
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
try:
    percentage = float(percentage)
    if percentage < 0 or percentage > 100:
        print(f"{percentage} is not a valid percentage!")
    else:
        print("Thanks")
        if 71 <= percentage <= 100:
            print("high pass")
        elif 31 <= percentage <= 70:
            print("low pass")
        else:
            print("fail")

except ValueError:
    print(f"{percentage} is not a valid percentage!")

'''
Test Cases

Enter your test percentage: 40
Thanks
low pass

Enter your test percentage: 20
Thanks
fail

Enter your test percentage: 110
110.0 is not a valid percentage!

Enter your test percentage: 80
Thanks
high pass
'''
