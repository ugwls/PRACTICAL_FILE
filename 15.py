# Write a program to create a list by entering countries and respective
# capital and population. The program should accept the name of a country
# as an input and print the corresponding capital name and population as
# output. Otherwise, the program should print an appropriate message if
# the country is not found in the list. Also, display the details of the
# list in descending order.

country = {}


def add_country():
    n = int(input("Enter number of Country's: "))
    for i in range(n):
        name = input("Country Name: ")
        capital = input("Country Capital: ")
        population = int(input("Country Population: "))
        country[name] = [capital, population]


def Search_Country():
    name = input("Enter Country name: ")
    for keys, values in country.items():
        if keys == name:
            print(f'Capital: {values[0]}')
            print(f'Population: {values[1]}')


k = True
while k == True:
    print('''
1.Add Country Details
2.Search Country Details
3.See Country Details
4.Exit
    ''')
    option = int(input('Enter your option(1/4): '))
    if 0 < option <= 3:
        if option == 1:
            add_country()
        elif option == 2:
            Search_Country()
        elif option == 3:
            print(country)
    elif option == 4:
        k = False
    else:
        print("Invalid Option!")
