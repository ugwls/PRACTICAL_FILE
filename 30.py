# Write a python program to search and display the
# record of the student from a binary file “Student.dat”
# containing students records (Rollno, Name and Marks).
# The user will enter roll number of the student to be searched.


import pickle


def set_data():
    rollno = int(input('Enter roll number: '))
    name = input('Enter name: ')
    test_marks = int(input('Enter test marks: '))
    print()
    student = {}
    student['rollno'] = rollno
    student['name'] = name
    student['test_marks'] = test_marks
    return student


def display_data(student):
    print('Roll number:', student['rollno'])
    print('Name:', student['name'])
    print('Test marks:', student['test_marks'])
    print()


def write_record():
    outfile = open('student.dat', 'ab')
    pickle.dump(set_data(), outfile)
    outfile.close()


def read_records():
    infile = open('student.dat', 'rb')
    while True:
        try:
            student = pickle.load(infile)
            display_data(student)
        except EOFError:
            break
    infile.close()


def search_record():
    infile = open('student.dat', 'rb')
    rollno = int(input('Enter rollno to search: '))
    flag = False
    while True:
        try:
            student = pickle.load(infile)
            if student['rollno'] == rollno:
                display_data(student)
                flag = True
                break
        except EOFError:
            break

    if flag == False:
        print('Record not Found')
        print()
    infile.close()


while(True):
    print('''
        Menu
1. Add Record
2. Display Records
3. Search a Record
4. Exit
    ''')
    choice = input('Enter choice(1-4): ')
    print()
    if choice == '1':
        write_record()
    elif choice == '2':
        read_records()
    elif choice == '3':
        search_record()
    elif choice == '4':
        break
    else:
        print('Invalid input')
