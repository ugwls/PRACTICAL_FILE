# WAP to delete the file(s), which you want, should
# no longer exist in your computer. The file name
# should be entered at the time of program execution.
# If the entered file name not exist, display
# a proper message on screen

import os

file_name = input("Enter file name(with file extention): ")

if os.path.exists(file_name):
    os.remove(file_name)
else:
    print('File not found')
