#Exercise 6.3
'''
Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
Write a main program that asks for a volume in gallons from the user and converts the value to liters.
 The conversion must be done by using the function. Conversions continue until the user inputs a negative value.
 '''

#create a function converting gallons to litres
def convert_gal_to_l (gall):
    litres = round((gall*3.78541),3)
    return litres

print("Exercise 6.3")
print("Enter the amount of gallons to converse to litres.")
print("If you want to finish the program enter a negative value.")

while True:
    gallons = float(input("Entere the amount of gallons: "))
    if (gallons <0):
        print("You entered a negative value")
        break
    print(gallons, "gal is equal to ", convert_gal_to_l(gallons), "litres.\nIf you want to finish the program "
                                                                  "enter a negative value.\n")

