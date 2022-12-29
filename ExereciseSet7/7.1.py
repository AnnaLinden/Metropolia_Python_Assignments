#Tuple, set, and dictionary
''' Write a program that asks the user for a number of a month and then prints out the corresponding season
 (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program.
 We can define each season to last three months, December being the first month of winter.'''

# create a tuple with seasons
seasons = ("winter", "spring", "summer", "autumn")

# get input from the user, which is the number of the month
month = (input("Enter the number of the month: "))

#check if the input is a digit with ".isdigit()" method
def is_month_digit (month):
    return month.isdigit()

# if the input is a digit, check the value end print out the name of the season
if is_month_digit(month) == True:
    month = int(month)
    if (month == 1 or month == 2 or month == 12):
        print(f"It is {seasons[0]}")

    elif (month == 3 or month == 4 or month == 5):
        print(f"It is {seasons[1]}")

    elif (month == 6 or month == 7 or month == 8):
        print(f"It is {seasons[2]}")

    elif (month == 9 or month == 10 or month == 11):
        print(f"It is {seasons[3]}")

    else:
        print("Invalid input. Please enter a number 1-12.")


else:
    print("Invalid input. Please enter a number 1-12.")