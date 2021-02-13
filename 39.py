# Write a menu-based program to perform the operation on queue in python.

queue = []


def Insert():
    n = int(input('Enter how many no. you want to insert: '))
    for _ in range(0, n):
        value = int(input('Enter no.: '))
        queue.append(value)


def Delete():
    queue.pop(0)
    print('Done')


def Show():
    print(queue)


k = True
while k == True:
    print('''
1. Push Values
2. Delete Values
3. See Values
4. Exit
    ''')
    option = int(input('Enter your option(1/4): '))
    if option == 1:
        Insert()
    elif option == 2:
        Delete()
    elif option == 3:
        Show()
    elif option == 4:
        k = False
    else:
        print("Invalid Option!")
        continue
