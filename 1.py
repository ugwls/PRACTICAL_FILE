# Determine whether a number is a perfect number, an Armstrong number or a palindrome.

def perfect_number(n):
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        return True
    else:
        return False


def armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if n == sum:
        return True
    else:
        return False


def palindrome(n):
    temp = n
    rev = 0
    while(n > 0):
        dig = n % 10
        rev = rev*10+dig
        n = n//10
    if(temp == rev):
        return True
    else:
        return False


k = True
while k == True:
    n = int(input("Enter a number: "))
    if perfect_number(n) == True:
        print(n, " is a Perfect number!")
    if armstrong(n) == True:
        print(n, " is an Armstrong number!")
    if palindrome(n) == True:
        print("The number is a palindrome!")
    else:
        print("The number is a Unknow!")
    option = input('Do you want to try again.(y/n): ').lower()
    if option == 'y':
        continue
    else:
        k = False
