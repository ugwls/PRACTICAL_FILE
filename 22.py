# WAP to create a dictionary called Census with
# country name and population. Using two functions,
# perform the following:
# Search_Country() – Enter the country name and
# displays its respective population.
# Delete_Country() – Enter the country name and
# delete its respective population.


def Search_Country():
    name = input("Enter Country name: ")
    for i in country:
        if country[i] == name:
            print(f'Population of the Country is : {country[i][0]}')


def Delete_Country():
    name = input("Enter Country Name: ")
    del country[name]
    print('Country deleted')


k = True
while k == True:
    print('''
1.Add Country Details
2.Search Country Details
3.Delete Country Details
4.See Country Details
5.Exit
    ''')
    option = int(input('Enter your option(1/5): '))
    if 0 < option <= 4:
        if option == 1:
            n = int(input("Enter number of Country: "))
            country = {}
            for i in range(n):
                print("Enter Details of Country No.", i+1)
                name = input("Country Name: ")
                population = int(input("Country Population: "))
                country[name] = [population]
        elif option == 2:
            Search_Country()
        elif option == 3:
            Delete_Country()
        elif option == 4:
            print(country)
    elif option == 5:
        k = False
    else:
        print("Invalid Option!")
