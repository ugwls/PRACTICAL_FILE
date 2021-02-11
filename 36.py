# Write a program to create a queue called Doctor to perform the
# basic operations on queue using list. The list contains two
# data fields: Docid and Docname. Write the following functions:
# InsertDoc() – To push the data values into the list  Docinfo
# DeleteDoc() – To remove the data value from the list  Docinfo
# ShowDoc(): - To display data value for all Docinfo.

# Queue
Doctor = []


def InsertDoc():
    n = int(input('Enter who many Doctor you want to insert: '))
    for _ in range(0, n):
        Docid = int(input('Enter Doctor ID: '))
        Docname = input('Enter Doctor: ')
        Docinfo = (Docid, Docname)
        Doctor.append(Docinfo)


def DeleteDoc():
    Doctor.pop()


def ShowDoc():
    print(Doctor)


k = True
while k == True:
    print('''
1. Push Docinfo
2. Delete Docinfo
3. See Doctor
4. Exit
    ''')
    option = int(input('Enter your option(1/4): '))
    if option == 1:
        InsertDoc()
    elif option == 2:
        DeleteDoc()
    elif option == 3:
        ShowDoc()
    elif option == 4:
        k = False
    else:
        print("Invalid Option!")
        continue
