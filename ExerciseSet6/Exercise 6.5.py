#Exercise 6.5
'''Write a function that gets a list of integers as a parameter. The function returns a second list
that is otherwise the same as the original list except that all uneven numbers have been removed.
For testing, write a main program where you create a list, call the function,
and then print out both the original as well as the cut-down list.'''

#write a function that gets a list of integers as a paeameter
def numbers (original_list):
#make a new list, which is a copy of original list
#!if we don't use [:] we are going to change original list too
    even_numbers = original_list [:]
#remove uneven numbers from the list using a for loop
    for i in original_list:
        if (i%2 !=0):
            even_numbers.remove(i)
    return even_numbers

original_list = [1,2,3,4,5,6,7,8]
print("Original list of numbers is: ", original_list, ". Even numbers are: ", numbers(original_list))