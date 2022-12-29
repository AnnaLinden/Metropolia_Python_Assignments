# EXERCISE SET 4 WHILE LOOPS

# Exercise 1
'''Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.'''

'''number = 1

while number<=1000:
    if number%3==0:
        print(number)
    number= number+1'''

# Exercise 2
'''Write a program that converts inches to centimeters until the user inputs a negative value. 
Then the program ends.'''
'''
inches = 1
while inches>=0:
   inches = int(input("Enter the amount of inches: "))
   cent = inches * 2.54
   print (cent)
'''

# Exercise3
'''Write a program that asks the user to enter numbers until they enter an empty string to quit. 
Finally, the program prints out the smallest and largest number from the numbers it received.'''

"""smallest = None
largest = None

while True:
    num = input("Enter a number: ")
    if num == " ":
        break
    num1 = int (num)
    if smallest is None or num1< smallest:
        smallest = num1
    if largest is None  or largest < num1:
        largest = num1

print("The smallest number is:", smallest, ".\n The largest number is: ", largest, ".") """

# Exercise 4
""" Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number 
until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. 
Notice that the computer must not change the number between guesses."""
'''
from random import randint
from random import seed

seed (1)

num = randint(1,10)
guess = 0

while guess!=  num:
    guess = int(input("The number is between 1 and 10. Guess the number: "))
    if num > guess:
        print("Too low")
    elif num< guess:
        print("Too high")
if guess== num:
    print("Correct")
else:
    print("Invalid input")
'''
# Exercise 5
"""Write a program that asks the user for a username and password. If either or both are incorrect, 
the program ask the user to enter the username and password again. This continues until the login information is correct
 or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. 
 After five failed attempts the program prints out Access denied. The correct username is python and password rules."""

username = "python"
password = "rules"

num = 0
while num < 5:
    num = num + 1
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")
    if entered_username == username and entered_password == password:
        print("Welcome!")
        break
    elif num == 5:
        print("Access denied")
    else:
        print("Enter the username and password again.")

# Exercise 6
"""
Monte Carlo estimation 
. Generate random point x. 
3. Generate random point y. 
4. Calculate d = x*x + y*y. 
5. If d <= 1, increment circle_points. 
6. Increment square_points. 
7. Increment interval. 
8. If increment < NO_OF_ITERATIONS, repeat from 2. 
9. Calculate pi = 4*(circle_points/square_points). 
10. Terminate.
 """

import random

points = float(input("Enter the amount of random points: "))
circle_points = 0
square_points = 0
done_points = 0

while done_points < points:
    done_points += 1
    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)

    # Distance between (x, y) from the origin
    origin_dist = rand_x * rand_x + rand_y * rand_y

    # Checking if (x, y) lies inside the circle
    if origin_dist < 1:
        circle_points += 1
    else:
        square_points += 1

pi = 4 * circle_points / square_points
print(pi)
