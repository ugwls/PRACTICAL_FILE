# Count and display the number of vowels,
# consonants, uppercase, lowercase characters in string


def countCharacterType(s):
    vowels = 0
    consonant = 0
    lowercase = 0
    uppercase = 0

    for i in range(0, len(s)):
        ch = s[i]
        if ((ch >= 'a' and ch <= 'z') or
                (ch >= 'A' and ch <= 'Z')):
            if ch.islower():
                lowercase += 1
            if ch.isupper():
                uppercase += 1
            ch = ch.lower()

            if (ch == 'a' or ch == 'e' or ch == 'i'
                    or ch == 'o' or ch == 'u'):
                vowels += 1
            else:
                consonant += 1

    print("Vowels:", vowels)
    print("Consonant:", consonant)
    print("LowerCase:", lowercase)
    print("UpperCase:", uppercase)


k = True
while k == True:
    s = input('Enter a string: ')
    countCharacterType(s)
    option = input('Do you want to try again.(y/n): ').lower()
    if option == 'y':
        continue
    else:
        k = False
