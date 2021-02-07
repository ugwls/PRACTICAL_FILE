# Input a string and determine whether it is
# a palindrome or not; convert the case of characters in a string.


def is_palindrome(s):
    return s == s[::-1]


k = True
while k == True:
    s = input("Enter a string: ")
    if is_palindrome(s):
        print('Entered Srting is Palindrom string!')
        print(f'Converted case string is: {s.swapcase()}')
    else:
        print('Entered Srting is not Palindrom string!')
        print(f'Converted case string is: {s.swapcase()}')

    option = input('Do you want to check more no.(y/n): ').lower()
    if option == 'y':
        continue
    else:
        k = False
