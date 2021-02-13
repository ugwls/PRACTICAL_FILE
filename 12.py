# Input a list / tuple of elements, search
# for a given element in the list/tuple.


k = True
while k == True:
    arr = list(
        map(int, input('Enter a list of no.s(separated by commas): ').split(',')))
    x = int(input('Enter a no. to search: '))
    for i in range(0, len(arr) - 1):
        if arr[i] == x:
            print(f'Entered no. is in the list, At index number: {arr[i]}')
    option = input('Do you want to try again(y/n): ').lower()
    if option == 'y':
        continue
    else:
        k = False
