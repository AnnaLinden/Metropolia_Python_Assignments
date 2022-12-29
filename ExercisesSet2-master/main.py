#print ("Hello, Anna!")


# Exercise 1

"""user = input("What is your name? ")
print("Hello, " + user + "!") """

# Exercise 2

""" import math
radius = float (input(" What is the radius of the circle? "))

area = (math.pi * radius**2)
print (area) """

# Exercise 3

""" length = float (input ("What is the length of the rectangle? "))
width = float (input ("What is the width of the rectangle? "))
perimeter = 2 * (length + width)
area = length * width
print("The perimeter of the rectangle is: ",  perimeter)
print("The area of the rectangle is: ", area) """

# Exercise 4


"""num1 = int (input ("Enter number 1: "))
num2 = int (input ("Enter number 2: "))
num3 = int (input ("Enter number 2: "))

sum = num1 + num2 + num3
avg = sum/3
product = num1*num2*num3
print ("The sum of the numbers is: ", sum)
print ("The average of the numbers is: ", avg)
print ("The product of the numbers is: ", product)"""

# Exercise 5

"""talents = float (input("Enter talents:\n"))
pounds = float (input("Enter pounds:\n"))
lots = float (input("Enter lots:\n"))

conv_to_grams = lots* 13.3 + pounds* 32*13.3 + talents * 20*32*13.3
kilos = int (conv_to_grams//1000)
grams = ("{:.2f}".format(conv_to_grams%1000))
print ("The weight in modern units\n", kilos, " kilograms and " ,grams ," grams.")"""

# Exercise 6
from random import seed
from random import randint
#seed (1)

dig1 = randint (0,10)
dig2 = randint (0,10)
dig3 = randint (0,10)
print("3-digit code is: ", dig1,dig2,dig3)

dig4 = randint (1,6)
dig5 = randint (1,6)
dig6 = randint (1,6)
dig7 = randint (1,6)

print("4-digit code is: ", dig4,dig5,dig6,dig7)