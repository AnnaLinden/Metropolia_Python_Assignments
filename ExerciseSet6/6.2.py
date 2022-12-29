
#Exercise 2
'''Modify the function above so that it gets the number of sides on the dice as a parameter. 
With the modified function you can for example roll a 21-sided role-playing dice.
 The difference to the last exercise is that the dice rolling in the main program continues 
 until the program gets the maximum number on the dice, which is asked from the user at the beginning'''

import random
#ask the amount of sides from the user
sides = int(input("Enter the maximum amount of the sides: "))

#create a function which gives a random number up to the amount given by the user
def roll(sides):
    num = random.randint(1, sides)
    return num

#main program prints out numbers until it's equal the input given in the beginning
while True:
    num = roll(sides)
    print(num)
    if num == sides:
         break
