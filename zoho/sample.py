from numpy import *


# Correct list definition
a = array([
    [1, 2, 3],
    [4, 5, 6]
])

print (a)

for i in range(len(a)):
    for j in range(len(a[i])):
        print (a[i][j])

# Convert to numpy array and flatten

arr = a.reshape(3,2)

arr3 = matrix(arr)

print(arr3)

########################################################

c = matrix("1 2 ; 3 4 ; 5 6 ; 7 8")
print(c)

########################################################

def matrixe(row, column):
    arr5 = zeros((row, column), dtype=int)
    for i in range(row):
        for j in range(column):
            arr5[i,j] = int(input(f"Enter value ({i},{j}) : "))

    print(arr5)

row = int(input(f"Enter row value : "))

column = int(input(f"Enter column value : "))

matrixe(row, column)