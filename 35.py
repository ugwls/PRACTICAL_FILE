# Write a menu driven program to add and manipulate data
# from customer.csv file. Give function to do the following:
# 1.	Add Customer Details
# 2.	Search Customer Details
# 3.	Remove Customer Details
# 4.	Display all the Customer Details
# 5.	Exit

# csv_rowlist = [["SN", "Movie", "Protagonist"], [1, "Lord of the Rings", "Frodo Baggins"],[2, "Harry Potter", "Harry Potter"]]
import csv


def add():
    with open('customer.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Cus_no", "C_name"])
        n = int(input('Enter how many Customer you want to insert: '))
        for _ in range(0, n):
            cus_no = int(input('Enter Customer ID: '))
            cus_name = input('Enter Customer Name: ')
            info = [cus_no, cus_name]
            writer.writerow(info)


def display():
    with open('customer.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def search():
    data = []
    with open('customer.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    name = input('Enter customer name to search info: ')
    for i in range(1, len(data) - 1):
        if data[i][1] == name:
            print(f'Customer no. {data[i][0]} and Name is {data[i][1]}')


def remove():
    data = []
    with open('customer.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    name = input('Enter customer name to delete info: ')
    for i in range(1, len(data) - 1):
        if data[i][1] == name:
            data.pop(i)
            with open('customer.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)


k = True
while k == True:
    print('''
1.Add Customer Details
2.Search Customer Details
3.Remove Customer Details
4.Display all the Customer Details
5.Exit
    ''')
    option = int(input('Enter your option(1/5): '))
    if option == 1:
        add()
    elif option == 2:
        search()
    elif option == 3:
        remove()
    elif option == 4:
        display()
    elif option == 5:
        k = False
    else:
        print("Invalid Option!")
        continue
