#count the number which are divisible by 3 and 5

################################################################################

a = 1
b = 100

c = 0
d = 0
e = 0
g = []
h = []
j= []

for i in range (a+1,b+1):
    if (i % 3 ==0  and i % 5 ==0):
        c +=1
        g.append(i)
    elif (i % 3 == 0 ):
        d +=1
        h.append(i)
    elif ( i % 5 == 0):
        e +=1
        j.append(i)

f = e + d

print(f"divisible by 3 = {d} {h}")

print(f"divisible by 5 = {e} {j}")

print(f"divisible by 3 and 5 = {c} {g}")

print(f"Total = {f}")

################################################################################

a = int(input("Enter value 1 : "))
b = int(input("Enter value 2 : "))


c = 0
d = 0
e = 0
g = []
h = []
j= []

for i in range (a+1,b+1):
    if (i % 3 ==0  and i % 5 ==0):
        c +=1
        g.append(i)
    elif (i % 3 == 0 ):
        d +=1
        h.append(i)
    elif ( i % 5 == 0):
        e +=1
        j.append(i)

f = e + d

print(f"divisible by 3 = {d} {h}")

print(f"divisible by 5 = {e} {j}")

print(f"divisible by 3 and 5 = {c} {g}")

print(f"Total = {f}")

################################################################################

#fully dynamic


a = int(input("Enter value 1 : "))
b = int(input("Enter value 2 : "))
k = int(input("Multiple value 1 : "))
m = int(input("Multiple value 2 : "))

c = 0
d = 0
e = 0
g = []
h = []
j= []

for i in range (a+1,b+1):
    if (i % k ==0  and i % m ==0):
        c +=1
        g.append(i)
    elif (i % k == 0 ):
        d +=1
        h.append(i)
    elif ( i % m == 0):
        e +=1
        j.append(i)

f = e + d

print(f"divisible by {k} = {d} {h}")

print(f"divisible by {m} = {e} {j}")

print(f"divisible by {k} and {m} = {c} {g}")

print(f"Total = {f}")