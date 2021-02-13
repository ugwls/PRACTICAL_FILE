# WAP to take the number of students as input,
# then ask marks for five subjects as English,
# Physics, Chemistry, Maths and Computer. If
# the total marks for any student are less than
# 200, then print he failed or else print passed.
# Use the dictionary to store the student name
# as key and marks as value.


n = int(input("Enter number of students: "))
result = {}
for i in range(n):
    name = input("Enter student name: ")
    english = int(input("Please enter English Marks: "))
    math = int(input("Please enter Math score: "))
    computers = int(input("Please enter Computer Marks: "))
    physics = int(input("Please enter Physics Marks: "))
    chemistry = int(input("Please enter Chemistry Marks: "))
    total = english + math + computers + physics + chemistry
    result[name] = total

for keys, values in result.items():
    if values >= 200:
        print(f'{keys}: Passed')
    else:
        print(f'{keys}: Failed')
