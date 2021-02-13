# Write a program to input five students name and their total marks
# in first semester. Find the highest mark and the name of the student.

student_list = {}
for _ in range(0, 5):
    name = input("Enter Your Name: ")
    marks = int(input('Enter your marks: '))
    student_list[marks] = name

highest = sorted(student_list.items())
print(f'{highest[-1][1]} has the highest mark: {highest[-1][0]}')
