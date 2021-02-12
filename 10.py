# write a program for linear search in python


def linearsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


k = True
while k == True:
    arr = list(map(int, input('Enter a list of numbers: ').split(',')))
    x = int(input('Enter a number: '))
    print("element found at index "+str(linearsearch(arr, x)))
    option = input('Do you want to try again.(y/n): ').lower()
    if option == 'y':
        continue
    else:
        k = False
