def even(n):
    n = n/2
    positive(int(n))

def odd(n):
    n = (3*n)+1
    positive(int(n))

def evenodd(n):
    if n == 1:
        print(a)
    elif n%2 == 0:
        even(n)
    elif n%2 != 0:
        odd(n)

def positive(n):
    a.append(n)
    evenodd(n)


a = []

n = int(input("Enter value : "))
if n >=1:
    a.append(n)
    evenodd(n)
else:
    print("Error!")

# Enter value : 5
# [5, 16, 8, 4, 2, 1]

# Enter value : 16
# [16, 8, 4, 2, 1]

# Enter value : 7
# [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

