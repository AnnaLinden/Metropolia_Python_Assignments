#Exercise 7.2
'''Write a program that asks the user to enter names until he/she enters an empty string.
 After each name is read the program either prints out New name or Existing name depending on whether
 the name was entered for the first time. Finally, the program lists out the input names one by one,
 one below another in any order. Use the set data structure to store the names.'''

names = set()

while True:
    name = input("Enter a name: ")

    if name in names:
        print("Existing name. Press Enter to quit.")
    else:
        print("New name. Press Enter to quit.")

    if name == "":
        break
    names.add(name)

print(f"{names}")
