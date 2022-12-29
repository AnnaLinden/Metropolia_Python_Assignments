# List structures and iterative loops (for)
#Exercise 1
"""
Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the the
sum of the numbers. Use a for loop.
"""
import random

print("Task 5.1")
#Ask from the user input the amount of dice rolls,
#cast the input to integer
rolls = int(input("Enter the amount of dice rolls: "))
#define an empty string called values
values = []
#declara a variable 'sum' and assign it to '0'
sum = 0

#create a while loop, which works while the amount of rolls defined from the user's input is more than 0
#each time the amount of rolls decreases by 1
#with each roll there's generated a new variable 'value' with the help of imported function "random"
#each value is appended to the list "values"
#all the values are printed to check that the loop works correctly
while rolls!=0:
    rolls-=1
    value = random.randint (1,6)
    values.append(value)
print(values)


#Using for loop we sum up all the values in list "values" and their sum is printed out
for x in values:
    sum = sum + x

print (f"The sum of the numbers: {sum}\n")



#Exercise 2
'''Write a program that asks the user to enter numbers until they input an empty string to quit.
 At the end, the program prints out the five greatest numbers sorted in descending order. 
 Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.'''

#initialise a variable called num and make it 0
#create an empty list called "numbers"
print("Task 5.2")
num = 0
numbers = []

#create a while loop which breaks out if the user enter an empty string
#the loop asks input from the user and then appends the lest "numbers"
while True:
    if num=="":
        break
    num = input("If you want to quit, press enter. But firstly enter at least 5 numbers: ")
    numbers.append(num)

# numbers list is sorted and reversed by the defalt method in python
# then the first 6 numbers are printed out
numbers.sort(reverse=True)
print(f"These are 5 of the numbers you entered. Sorted and reversed. {numbers[0:5]}\n")


#Exercise 3
"""Write a program that asks the user for an integer and tells if the number is a prime number. 
Prime numbers are number that are only divisible by one or the number itself.
For example, number 13 is a prime number as can only be divided by 1 or 13 so that the result is an integer.
On the other hand, number 21 for example is not a prime number as it can be also be divided by numbers 3 and 7."""

print("Task 5.3")

num = int(input("Enter a number: "))

# define a flag variable
flag = True

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")


#Exercise 4
'''Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names)
 and stores them into a list structure. Finally, the program prints out the names of the cities one by one,
  one city per line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop 
  to iterate through the list. '''

print("Task 5.4")
#create an empty list of cities
cities = []

#create a for loop to read 5 names of cities from the user.
for value in range (1,6):
    city = (input("Enter the name of a city: "))
    #add input to the list of cities
    cities.append(city)

#use for in loop to iterate through the list
#city is a temporary variable
for city in cities:
    print(city)

