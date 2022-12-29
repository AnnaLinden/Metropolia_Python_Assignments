# Exercise Set 3 Conditional Statements

# Exercise 1
"""Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill
the size limit, the program instructs
to release the fish back into the lake and notifies the user of how many centimeters below the size limit
the caught fish was. A zander must be 42 centimeters or longer to meet the size limit. """
'''
length =  int (input("Enter the length of a zander: "))
if length < 42:
    difference = 42 - length
    print("The fish back into the lake. The fish you caught is" , difference, "centimeters below the size limit")
else:
    print ("You can keep the fish")
    '''


# Exercise 2
"""Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written 
description according to the list below. You must use an if/elif/else structure in your solution.

LUX: upper-deck cabin with a balcony.
A: above the car deck, equipped with a window.
B: windowless cabin above the car deck.
B: windowless cabin below the car deck.
If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class."""


"""cabinclassinput = input ("Enter the cabin class: ")
cabinclass = cabinclassinput.lower()
if cabinclass == "lux":
    print("Above the car deck, equipped with a window.")
elif cabinclass == "b":
    print("Windowless cabin above the car deck")
elif cabinclass == "c":
    print("Windowless cabin below the car deck")
else:
    print("Invalid cabin class")"""

# Exercise 3
"""Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if
 the hemoglobin value is low, normal or high.

A normal hemoglobin value for adult females is between 117-155 g/l.
A normal hemoglobin value for adult males is between 134-167 g/l."""

"""genderinput = input("Enter your gender (male or female): ")
hemogl = int(input("Enter your hemoglobin value: "))
gender = genderinput.lower()
if gender == "male":
    if 134<=hemogl<=157:
        print("You have normal hemoglobin value")
    elif 0<=hemogl<134:
        print(("You have low hemoglobin value"))
    else:
        print("You have high hemoglobin value")

if gender == "female":
    if 117<=hemogl<=155:
        print("You have normal hemoglobin value")
    elif 0<=hemogl<117:
        print(("You have low hemoglobin value"))
    else:
        print("You have high hemoglobin value")"""

#Exercise 4
"""Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year. 
A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also
 divisible by 400."""
'''
year = int(input("Enter a year: "))
if year%100 ==0 and year%400 == 0:
    print(year,"is a leap year")

if year%400 ==0:
    print("It is a leap year")

elif year%4 == 0 and year%100!=0:
    print("It is a leap year")

else:
    print("It is not a leap year")
    
'''