#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.6 Writing/Appending To A File -C)Modify
Author: Sidak Singh
Date: 2024-10-29
Assignment: 2.6 Writing/Appending To A File -C)Modify
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#No Globals
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
myFile = open('Students.txt', 'a')
print('Enter Student Details: ')

while True:
    name = input('Student name: ')
    grade = input('Student grade: ')

    line = f"{name} - {grade}\n"
    myFile.write(line)

    while True:
        print("Enter another student: yes or no")
        choice = input().lower()
        if choice in ['yes', 'no']:
            break
        else:
            print("Invalid input type 'yes' or 'no'.")

    if choice == 'no':
        print('Goodbye!')
        break

myFile.close()

'''
Test casses

Enter Student Details:
Student name: Alice
Student grade: A
Enter another student: yes or no
yes
Student name: Bob
Student grade: B
Enter another student: yes or no
maybe
Invalid input type 'yes' or 'no'.
Enter another student: yes or no
no
Goodbye!

'''
