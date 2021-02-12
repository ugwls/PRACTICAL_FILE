# Write a menu driven program where you are getting product
# related details in a file product.txt. menu options are
# 1. Add Details
# 2. Search Details
# 3. Show Details
# 4. Exit

def add():
    id = int(input('Enter product id: '))
    name = input('Enter product name: ')
    temp = (id, name)
    with open('product.txt', "a") as f:
        f.write(f'{temp} \n')
    print('product added successfully')
    input('Press ENTER to continue...')


def see():
    with open("product.txt", "r") as f:
        d = f.readlines()
        d = [x.strip('\n') for x in d]
        for i in d:
            print(i)
    input('Press ENTER to continue...')


def Search():
    with open("product.txt", "r")as f:
        d = f.readlines()
        d = [eval(x.strip('\n')) for x in d]
    name = input('Enter product name to Search: ')
    for i in range(0, len(d) - 1):
        if d[i][1] == name:
            print(f'productinfo is {d[i]}')


k = True
while k == True:
    print('''
1. Add Details
2. Search Details
3. Show Details
4. Exit
    ''')
    option = int(input('Enter your option(1/4): '))
    if option == 1:
        add()
    elif option == 2:
        Search()
    elif option == 3:
        see()
    elif option == 4:
        k = False
    else:
        print("Invalid Option!")
        continue
