# Display the terms of a Fibonacci series.

k = True
while k == True:
    nterms = int(input("How many terms: "))
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
        print("Please enter a positive integer")
        continue
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
    option = input('Do you want to try again.(y/n): ').lower()
    if option == 'y':
        continue
    else:
        k = False
