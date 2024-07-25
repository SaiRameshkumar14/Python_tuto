# PROBLEM 2:
# patter printing:
# matrix= ["abc","def","ghi")

# sample inputl: 4 
# ••••
# •abc•
# •def•
# •ghi•
# ••••

# sample input2: 5

# •••••
# •••••
# •abc•
# •def•
# •ghi•
# •••••
# •••••

def print_pattern(matrix, n):    
    # Print the top border
    for i in range(n-3):
        for j in range(n):
            print('•', end='')
        print()

    # Print the matrix rows with border
    for row in matrix:
        for i in range(1):
            print('•', end='')
        print(row, end='')
        for i in range(1):
            print('•', end='')
        print()
    
    #        (OR)
    # Print the matrix rows with border
    # for row in matrix:
    #     print('•', end='')
    #     print(row, end='')
    #     print('•', end='')
    #     print()

    # Print the bottom border
    for i in range(n-3):
        for j in range(n):
            print('•', end='')
        print()

# Sample Input 1
matrix1 = ["abc", "def", "ghi"]
n1 = 4
n2 = 5
print_pattern(matrix1, n1)
