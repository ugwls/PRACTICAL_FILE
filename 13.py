# Input a list of numbers and test if a number is equal to the sum of
# the cubes of its digits. Find the smallest and largest such number
# from the given list of numbers.


def Armstrong(arr):
    for num in arr:
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10
        if num == sum:
            print(f'Armstrong no. is: {num}')
    arr.sort()
    smallest = arr[0]
    largest = arr[-1]
    print(f'smallest value is {smallest}')
    print(f'largest value is {largest}')


k = True
while k == True:
    arr = list(
        map(int, input('Enter a list of no.s(separated by commas): ').split(',')))
    Armstrong(arr)
    option = input('Do you want to try again.(y/n): ').lower()
    if option == 'y':
        continue
    else:
        k = False
