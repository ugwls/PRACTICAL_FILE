# Write a Python program to compute the sum of
# all the elements of each tuple stored inside
# a list of tuples.

# Original list of tuples:
# [(1, 2), (2, 3), (3, 4)]

# Sum of all the elements of each tuple stored
# inside the said list of tuples:
# [3, 5, 7]


def test(lst):
    result = map(sum, lst)
    print(list(result))


lst = [(1, 2), (2, 3), (3, 4)]
test(lst)
