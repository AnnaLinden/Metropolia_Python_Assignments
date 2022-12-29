#Exercise 6.6
'''Write a function that receives two parameters: the diameter of a round pizza in centimeters and
 the price of the pizza in euros. The function calculates and returns the unit price of the pizza per square meter.
 The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides
 better value for money (which of them has a lower unit price).
 You must use the function you wrote for calculating the unit prices.'''
import math

def price_per_meter(diameter, price):
    area = round((diameter* math.pi),4)
    unit_price = price/area
    print ("The price of this pizza per square meter is: " ,round(unit_price,4), "euro\n")
    return unit_price


first_pizza_diameter = int(input("Enter the diameter of the first pizza: "))
first_pizza_price = int(input("Enter the price of the first pizza: "))
first_pizza_value = price_per_meter(first_pizza_diameter,first_pizza_price)

second_pizza_diameter = int(input("Enter the diameter of the first pizza: "))
second_pizza_price = int(input("Enter the price of the first pizza: "))
second_pizza_value = price_per_meter(second_pizza_diameter,second_pizza_price)

if (first_pizza_value<second_pizza_value):
    print("The first pizza is cheaper than the second pizza.")
elif (first_pizza_value>second_pizza_value):
    print("The second pizza is cheaper than the first pizza.")
elif(first_pizza_value==second_pizza_value):
    print("The price is the same")