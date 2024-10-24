#-------------------------------------------------------------------------------------------------------------------
'''
Title: 2.7 Intro to OOP
Author: Sidak Singh
Date: 2024-10-23
Assignment: 2.7 Intro to OOP
'''
#-------------------------------------------------------------------------------------------------------------------
#No Imports
#-------------------------------------------------------------------------------------------------------------------
#Not listed here due to formation limitations
#-------------------------------------------------------------------------------------------------------------------
#Not listed here due to formation limitations
#-------------------------------------------------------------------------------------------------------------------
#Questions answers

# -What is Object Oriented Programming (OOP)?
# Object Oriented Programming is a style of programming which provides a means of structuring programs so that properties and behaviors are bundled into individual objects which can be later used.

# -How to define a class in Python?
# You can define a class by having the class keyword followed by the the name; starting with a capital letter
# eg: class Example:
    #def __init__(self, text):
        #self.text = text
    #def printExample(self):
        #print(self.text)

# test = Example("Testing")
# print(test.printExample)
# Testing
#This example shows how you can make the class called Example initialize text value with your argument and then print the value by calling the printExample method

# -How to instantiate an object in Python
# call the class name by writing its name then putting all the required parameters in the brackets
# eg: test = Example("Testing")
# sidenote: you can also store the it's memory address by assigning it to a variable letting you use it latter.

# - How to Inherit from another Python class?
# you use the super() keyword to view methods and items from the parent class
# This new inherited class now lets you reuse your code from the example class
# eg:
# class ExtendedExample(Example):
#     def __init__(self, text, additional_text):
#         super().__init__(text)
#         self.additional_text = additional_text

#     def print_extended_example(self):
#         print(f"{self.text} - {self.additional_text}")

#Article follow through
class Employee:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)
print(miles.name)
print(miles.age)
print(buddy.name)
print(buddy.age)

# Miles
# 4
# Buddy
# 9

buddy.age = 10
print(buddy.age)
#10

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4)
print(miles.description())
#Miles is 4 years old

print(miles.speak("Woof Woof"))
#'Miles says Woof Woof'

print(miles.speak("Bow Wow"))
#'Miles says Bow Wow'

print(miles)
#<__main__.Dog object at 0x102e1bdc0>

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    def __str__(self):
            return f"{self.name} is {self.age} years old"

miles = Dog("Miles", 4)
print(miles)
#Miles is 4 years old

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage:,} miles"

# Creating two Car objects
blue_car = Car("blue", 20000)
red_car = Car("red", 30000)

print(blue_car)
print(red_car)
# The blue car has 20,000 miles
# The red car has 30,000 miles

for car in (blue_car, red_car):
    print(car)

# The blue car has 20,000 miles
# The red car has 30,000 miles

class Parent:
    speaks = ["English"]

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("German")

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(buddy.speak("Yap"))
#'Buddy says Yap'

print(jim.speak("Woof"))
#'Jim says Woof'

print(jack.speak("Woof"))
#'Jack says Woof'

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.species)
#'Canis familiaris'

print(buddy.name)
#'Buddy'

print(jack)
#Jack is 3 years old

print(jim.speak("Woof"))
#'Jim says Woof'

print(type(miles))
#<class '__main__.JackRussellTerrier'>

isinstance(miles, Dog)
#True

isinstance(miles, Bulldog)
#False

isinstance(jack, Dachshund)
#False

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

miles = JackRussellTerrier("Miles", 4)
print(miles.speak())
#'Miles says Arf'

print(miles.speak("Grrr"))
#'Miles says Grrr'

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
           return f"{self.name} barks: {sound}"

jim = Bulldog("Jim", 5)
print(jim.speak("Woof"))
#Jim says Woof

miles = JackRussellTerrier("Miles", 4)
print(miles.speak())
#'Miles says Arf'

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

miles = JackRussellTerrier("Miles", 4)
print(miles.speak())
#'Miles barks: Arf'

#challange one
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class Golden_retriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)



'''
All log values placed in order

Miles
4
Buddy
9
10
Miles is 4 years old
Miles says Woof Woof
Miles says Bow Wow
<__main__.Dog object at 0x10443f910>
Miles is 4 years old
The blue car has 20,000 miles
The red car has 30,000 miles
The blue car has 20,000 miles
The red car has 30,000 miles
Buddy says Yap
Jim says Woof
Jack says Woof
Canis familiaris
Buddy
Jack is 3 years old
Jim says Woof
<class '__main__.JackRussellTerrier'>
Miles says Arf
Miles says Grrr
Jim says Woof
Miles says Arf
Miles barks: Arf
'''
