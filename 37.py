# Write two functions queins() to insert and quedel() to delete elements
# for customeer information, i.e. custno, cname using list

customer = []


def queins():
    n = int(input('Enter who many customer you want to insert: '))
    for _ in range(0, n):
        custno = int(input('Enter customer ID: '))
        cname = input('Enter customer Name: ')
        temp = [custno, cname]
        customer.append(temp)


def quedel():
    custno = int(input('Enter customer ID you want to delete: '))
    for i in range(0, len(customer)-1):
        if customer[i][0] == custno:
            del customer[i]


k = True
while k == True:
    print('''
1. Add Customer
2. Delete Customer
3. See Customer
4. Exit
    ''')
    option = int(input('Enter your option(1/4): '))
    if option == 1:
        queins()
    elif option == 2:
        quedel()
    elif option == 3:
        print(customer)
    elif option == 4:
        k = False
    else:
        print("Invalid Option!")
        continue
