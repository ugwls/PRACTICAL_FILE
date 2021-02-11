# WAP to input employee number and name for ‘N’
# employees and display all information in ascending
# order of their employee number

n = int(input("Enter number of Employee: "))
emp = {}
for i in range(n):
    print("Enter Details of Employee No.", i+1)
    Empno = int(input("Employee No: "))
    name = input("Name: ")
    emp[Empno] = [name]
ascending = list((emp.items()))
ascending.sort()
print(ascending)
