# WAP using function merge(file1,file2) to merge two
# files and obtain a third file called “NEW.DAT”.
# The file1 and file2 are two files, which are pass
# as arguments. Also, display the content of third file.

import pickle


def merge(file1, file2, file3):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        data_1 = pickle.load(f1)
        data_2 = pickle.load(f2)
    with open(file3, 'ab') as f:
        pickle.dump(data_1, f)
        pickle.dump('\n', f)
        pickle.dump(data_2, f)


file1 = input('Enter file1 name(with extention): ')
file2 = input('Enter file2 name(with extention): ')
file3 = input('Enter New file name(with extention): ')
merge(file1, file2, file3)
