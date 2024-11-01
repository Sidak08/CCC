#-------------------------------------------------------------------------------------------------------------------
'''
Title: 3.3 A) Output From Lists - Solution
Author: Sidak Singh
Date: 2024-11-01
Assignment: 3.3 A) Output From Lists - Solution
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
countries = ["UK", "USA", "Chad", "Australia", "Thailand"]

# chnanges Australia with Mexico
countries[3] = "Mexico"
# chnanges UK with Iceland
countries[0] = "Iceland"
# chnanges USA with Thailand
countries[1] = countries[4]
squareNumbers = [1,4,9,16,25,36]
#-------------------------------------------------------------------------------------------------------------------
#No Functions
#-------------------------------------------------------------------------------------------------------------------
#Iceland, Thailand, Chad, Mexico, Thailand
print(countries)
#Check - Iceland, Thailand, Chad, Mexico, Thailand

# changes 36 with 49
squareNumbers[5] = 49

# makes one two
squareNumbers[0] +=1

# calc 16 - 2
total = squareNumbers[3] - squareNumbers[1]

print (total)
# 2,4,9,16,25,42
print(squareNumbers)
#check - 2,4,9,16,25,42
