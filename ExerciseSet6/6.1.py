#6. Functions
#Exercise 1
# Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6.
# The main program should print out the result of each roll.

from random import randint
print("Exercise 6.1")

#create a function "dice_roll" without any parameters until it is 6
# initiate an empty list "roll_results" and a"num" equal 0
#make a while loop which works until the result is 6
def dice_roll ():
    roll_results = []
    num = 0
    while (num!=6):
        num = randint(1,6)
        roll_results.append(num)
    return roll_results

print (dice_roll())
print("The dice was rolled until the result was 6.\n")

print ("Exercise 6.1. Another way.")

def dice_roll_2 ():
    num = randint (1,6)
    return num

while True:
    num2 = dice_roll_2()
    if (num2) == 6:
        print(f"You got 6: {num2}")
        break
    elif (num2 != 6):
        print(num2)


