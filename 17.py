# WAP to create a matrix with m number of rows and n number
# of columns. Display the elements in a matrix format.
# Note: The number of rows and columns will be decided at
# runtime of the program.

row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col] = row*col

print(multi_list)
