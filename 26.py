# Read a text file line by line and display each
# word separated by a #. Read a text file and display
# the number of vowels/ consonants/ uppercase/ lowercase
# characters in the file.


def word_separator():
    with open("26a.txt", "r") as f:
        doc = f.readlines()
        for i in doc:
            words = i.split()
            for a in words:
                print(a + "#", end=' ')
            print()


word_separator()


def countCharacterType():
    vowels = 0
    consonant = 0
    lowercase = 0
    uppercase = 0
    with open('26a.txt', "r") as f:
        s = f.read().split()
        for i in range(0, len(s)):
            ch = s[i]
            if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
                if ch.islower():
                    lowercase += 1
                else:
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


countCharacterType()
