#Exercise 6.4
'''Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers
 in the list. For testing, write a main program where you create a list, call the function,
  and print out the value it returned.'''

#make a function that gets a list of integers as a parameter
def numbers(list_of_integers):
    sum = 0
#for loop for calculating sum of numbers
    for i in list_of_integers:
        sum+= i
    return sum

#make a program to create a list, call the function and print out the value
list = [1,2,3,4,5, 10, 20]
print("The numbers in the list are: ",list, ". The sum equals: ", numbers(list), ".")



