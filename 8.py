# Write a program to generate random numbers between
# 1 to 6 and check whether a user won a lottery or not.


def random_game():
    import random
    num = random.randint(1, 6)
    a = int(input("Enter a Random numbers between(1/6): "))
    if a == num:
        print("You won the Game!")
    else:
        print('Better luck next time..')


k = True
while k == True:
    random_game()
    option = input('Do you want to check more no.(y/n): ').lower()
    if option == 'y':
        continue
    else:
        k = False
