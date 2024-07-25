n = 5
# Square Pattern
for i in range(n):
    for j in range(n):
        print('*',end='  ')
    print()
    
print()

# Increasing Pattern
for i in range(n):
    for j in range(i+1):
        print('*',end='  ')
    print()  

print()

# Decreasing Pattern
for i in range(n):
    for j in range(i,n):
        print('*',end='  ')
    print()

print()

# right angle Increase pattren
# 1) decreasing -' ' 2) increasing - *
for i in range(n):
    for j in range(i,n):
        print(' ', end='  ')
    for k in range(i+1):
        print('*', end='  ')
    print()
    
print()

# Decreasing right angle pattern
# 1) increasing 2) decresing
for i in range(n):
    for j in range(i+1):
        print(' ',end='  ')
    for k in range(i,n):
        print('*',end='  ')
    print()
    
print()

# pyramid pattern
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for k in range(i):
        print('*',end=' ')
    for h in range(i+1):
        print('*',end=' ')
    print()
    
print()

# Down pyramid pattern
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for k in range(i,n-1):
        print('*',end=' ')
    for h in range(i,n):
        print('*',end=' ')
    print()
    
print()

#Filled Diamond
for i in range(n-1):
    for j in range(i,n):
        print(' ',end=' ')
    for k in range(i):
        print('*',end=' ')
    for h in range(i+1):
        print('*',end=' ')
    print()
    
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for k in range(i,n-1):
        print('*',end=' ')
    for h in range(i,n):
        print('*',end=' ')
    print()

print()

# Unfilled Diamond
for i in range(n-1):
    for j in range(i,n):
        print('*',end=' ')
    for k in range(i):
        print(' ',end=' ')
    for h in range(i+1):
        print(' ',end=' ')
    for m in range(i,n):
        print('*', end=' ')
    print()
    
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    for k in range(i,n-1):
        print(' ',end=' ')
    for h in range(i,n):
        print(' ',end=' ')
    for m in range(i+1):
        print('*', end=' ')
    print()

print()

#box pattern
def box(row,col):
    for i in range(row):
        if i == 0 or i == row-1:
            print('*'*col)
        else:
            print('*'+' '*(col-2)+'*')

box(10,15)