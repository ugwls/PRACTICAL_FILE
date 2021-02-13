# A file emp.dat contains data attributes like : ecode, name and salary.
# Give function definitions to do the following
# a) Write the data of an employee.
# b) Read the employee data and display all the
# objects on the screen where salary is between 20000 and 30000.

import pickle

global global_flag, data_1
global_flag = False
data_1 = []


def Add_data():
    data_2 = []
    with open("emp.dat", 'ab+') as f:
        if global_flag == True:
            f.truncate(0)
        a = int(input('Enter how many record to add: '))
        for _ in range(0, a):
            ecode = int(input('Enter ecode: '))
            name = input("Enter Name: ")
            salary = int(input("Enter Salary: "))
            temp = [ecode, name, salary]
            data_1.append(temp)
        data_2.append(data_1)
        pickle.dump(data_2, f)
    f.close()


def Show_data():
    flag = True
    with open("emp.dat", 'rb') as f:
        data = pickle.load(f)
        for j in range(0, len(data)):
            for i in range(0, len(data[j])):
                if 20000 <= data[j][i][2] <= 30000:
                    print(f'Ecode = {data[j][i][0]}')
                    print(f'Name = {data[j][i][1]}')
                    print(f'Salary = {data[j][i][2]}')
                    flag = False
        if flag == True:
            print('No Entry Found!!!')


while True:
    print('''
    1. Add data.
    2. To show data.
    3. Exit.
    ''')
    options = int(input('Enter a option(1-3):'))
    if options == 1:
        Add_data()
        global_flag = True
    elif options == 2:
        Show_data()
    else:
        break
