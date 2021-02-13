# Write a program using function called insertionSort(Num) to arrange a
# list of integer elements in ascending order using insertion sort technique.

def insertionSort(num):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = list(
    map(int, input('Enter a list of no.s(separated by commas): ').split(',')))
insertionSort(arr)
print(arr)
