# write a program for binary search in python

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


k = True
while k == True:
    arr = list(map(int, input('Enter a list of numbers: ').split(',')))
    x = int(input('Enter a number: '))
    result = binary_search(arr, x)
    if result == -1:
        print(f'Element is present at index {result}')
    else:
        print("Element is not present in array")
    option = input('Do you want to try again.(y/n): ').lower()
    if option == 'y':
        continue
    else:
        k = False
