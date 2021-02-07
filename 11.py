# Write a program for bubble sort


def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


k = True
while k == True:
    arr = list(map(int, input('Enter a list of numbers: ').split(',')))
    bubbleSort(arr)
    for i in range(len(arr)):
        print(f'{arr[i]},', end='')
    print()
    option = input('Do you want to to try again(y/n): ').lower()
    if option == 'y':
        continue
    else:
        k = False
