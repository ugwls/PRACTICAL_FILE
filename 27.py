# Create a binary file with name and roll number.
# Search for a given roll number and display the name,
# if not found display appropriate message.

import pickle


def Add_data():
    data = []
    with open("tele.dat", 'ab') as f:
        a = int(input('Enter how many record to add: '))
        for _ in range(0, a):
            roll = int(input("Enter Student Roll no.: "))
            name = input("Enter Student Name: ")
            temp = (roll, name)
            data.append(temp)
        pickle.dump(data, f)


def Show_data():
    k = True
    with open("tele.dat", 'rb') as f:
        data = pickle.load(f)
        tele = int(input('Enter Student Roll no.: '))
        for i in data:
            if i[0] == tele:
                print(f'Name corresponds to {i[0]} is {i[1]}')
                k = False
        if k:
            print('Data not found!!')


while True:
    print('''
1. Add data.
2. To Search data.
3. Exit.
    ''')
    options = int(input('Enter a option(1-3):'))
    if options == 1:
        Add_data()
    elif options == 2:
        Show_data()
    else:
        break
