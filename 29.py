# Remove all the lines that contain the character
# `a' in a file and write it to another file.


with open("hp.txt", "w")as fo:
    fo.write("Harry Potter \n")
    fo.write("There is a difference in all harry potter books\n")
    fo.write('We can see it as harry grows\n')
    fo.write('the books were written by J.K rowling')

fo = open('hp.txt', 'r')
fi = open('writehp.txt', 'w')
l = fo.readlines()
for i in l:
    if 'a' in i:
        i = i.replace(i, '')
        fi.write(i)
    else:
        fi.write(i)
fi.close()
fo.close()
print('Done')
