# WAP to take the number of students as input,
# then ask marks for five subjects as English,
# Physics, Chemistry, Maths and Computer. If
# the total marks for any student are less than
# 200, then print he failed or else print passed.
# Use the dictionary to store the student name
# as key and marks as value.


k = True
while k == True:
    n = int(input("Enter number of students: "))
    result = {}
    for i in range(n):
        name = input("Enter student name: ")
        english = float(input("Please enter English Marks: "))
        math = float(input("Please enter Math score: "))
        computers = float(input("Please enter Computer Marks: "))
        physics = float(input("Please enter Physics Marks: "))
        chemistry = float(input("Please enter Chemistry Marks: "))
        total = english + math + computers + physics + chemistry
        result[name] = [total]
    for i in result:
        if result[i][0] >= 200:
            print(result[i], ': Passed')
        else:
            print(result[i], ': Failed')
