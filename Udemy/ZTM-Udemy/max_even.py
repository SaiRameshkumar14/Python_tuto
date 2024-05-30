a = [1,34,56,24,12,37,89,88]

def highesT_even(a):
    highest = 0
    for i in a:
        if i % 2 == 0:
            if i > highest:
                highest = i
    return highest

print(highesT_even(a))

#using map()

def highest_even(a):
    highest = []
    for i in a:
        if i % 2 == 0:
            highest.append(i)
    return max(highest)

print(highest_even(a))



