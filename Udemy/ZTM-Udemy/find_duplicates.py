a = [1,2,2,3,4,2,3,4,5,6,7,8]
b = []

for i in a:
    if a.count(i) > 1:
        b.append(i)


print(list(set(b)))

#[2, 3, 4]