#Exercise 7.3
'''Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport,
 fetch the information of an existing airport or quit. If the user chooses to enter a new airport,
the program asks the user to enter the ICAO code and name of the airport.
If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport
and prints out the corresponding name. If the user chooses to quit, the program execution ends.
The user can choose a new option as many times they want until they choose to quit.
(The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of
Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)'''

airports = {"EGKK":"London Gatwick Airport",
            "EFHK":"Helsinki-Vantaa",
            "ESSA": "Stockholm Arlanda Airport",
            "LSGG":"Geneva Airport"}
            #"ZBAA":"Beijing Capital International Airport"
            # Frankfurt Airport, EDDF

while True:
    value = input("If you want to enter a new airport, enter A."
                  "\nIf you want to fetch the information of an existing airport, enter B."
                  "\nIf you want to quit, enter C."
                  "\nEnter A,B or C: ").upper()
    if value == "A":
        name = input("Enter the name of the airport: ")
        icao = input("Enter the ICAO code of the airport: ")
        airports[name] = icao
        print("The new list of the airports is: \n", airports,"\n")
    elif value == "B":
        icao = input("Enter the ICAO code of the airport: ")

        if icao in airports:
            print(f"\n{icao} code corresponds to {airports[icao]}.\n")
    elif value == "C":
        break
    else:
        print("\nInvalid input. Please, enter A, B or C.\n")