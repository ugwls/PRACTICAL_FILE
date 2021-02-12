# Write a program to create a library
# in python and import it in a program.

import example

k = True
while k == True:
    example.hello()
    option = input('Do you want to try again.(y/n): ').lower()
    if option == 'y':
        continue
    else:
        k = False
