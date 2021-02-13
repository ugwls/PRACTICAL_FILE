# Write a program to create a stack called Product to perform
# the basic operations on stack using list. The list contains
# two data fields: ProductId and ProductName. Write the following functions:
# InsertProd() – To push the data values into the list  Docinfo
# DeleteProd() – To remove the data value from the list  Docinfo
# ShowProd(): - To display data value for all Docinfo.

# stack
product = []


def InsertProd():
    n = int(input('Enter who many products you want to insert: '))
    for _ in range(0, n):
        pro_id = int(input('Enter product ID: '))
        pro_name = input('Enter product: ')
        Docinfo = (pro_id, pro_name)
        product.append(Docinfo)


def DeleteProd():
    product.pop()
    print('Done')


def ShowProd():
    print(product)


k = True
while k == True:
    print('''
1. Push Docinfo
2. Delete Docinfo
3. See Product
4. Exit
    ''')
    option = int(input('Enter your option(1/4): '))
    if option == 1:
        InsertProd()
    elif option == 2:
        DeleteProd()
    elif option == 3:
        ShowProd()
    elif option == 4:
        k = False
    else:
        print("Invalid Option!")
        continue
