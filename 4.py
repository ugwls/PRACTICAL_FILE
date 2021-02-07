# Compute the greatest common divisor and least
# common multiple of two integers.


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    lcm = (x*y)//gcd(x, y)
    return lcm


k = True
while k == True:
    x = int(input('Enter a number: '))
    y = int(input('Enter a number: '))
    print(f'The GCD is {gcd(x, y)}')
    print(f'The LCM is {lcm(x, y)}')
    option = input('Do you want to check more no.(y/n): ').lower()
    if option == 'y':
        continue
    else:
        k = False
