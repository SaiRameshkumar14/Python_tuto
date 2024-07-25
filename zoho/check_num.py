# input = [2,252,22,232,42]
# target = 2

# output = [22,252,232]

# check the target number with each element in the array, and return which elements has higest consist of that target number

def length(n):
    count = 0
    for i in range(n):
        count += 1
    return count

def count(n,target):
    arr = []
    temp = 0
    for i in range(length(n)):
        for j in str(n[i]):
            if j == str(target):
                temp += 1
        if temp == 0:
            pass
        el

            

