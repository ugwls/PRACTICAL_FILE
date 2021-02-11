# Write a Python program to check whether an element
# exists within a tuple.

arr = tuple(
    map(str, input('Enter a list of numbers(separate by comma): ').split(',')))
element = input('Enter element to check: ')
print(element in arr)
