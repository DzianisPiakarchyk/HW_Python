import os
os.system('cls')



def print_operation_table(operation, num_rows = 6, num_columns = 6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end='\t')
        print()

print_operation_table(lambda row, col: row * col) 



# def print_operation_table(operation, num_rows = 6, num_columns = 6):
#     for i in range(num_rows * num_columns):
#         row, col = divmod(i, num_columns)
#         print("{:4}".format(operation(row + 1, col + 1)), end='')
#         if col == num_columns - 1:
#             print()

# print_operation_table(lambda row, col: row * col)



# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for row in range(1, num_rows + 1):
#         print(*map(operation, [row] * num_columns, range(1, num_columns + 1)), sep='\t')

# print_operation_table(lambda x, y: x * y)

