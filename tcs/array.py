a = []

for _ in range(4):
    b = int(input("Enter Value: "))
    a.append(b)
print("Original List:", a)

# Iterate over the indices of the list
for i in range(len(a)):
    if a[i] % 3 == 0 and a[i] % 5 == 0:
        a[i] = "ThreeFive"
    elif a[i] % 3 == 0:
        a[i] = "Three"
    elif a[i] % 5 == 0:
        a[i] = "Five"

print("Modified List:", a)

#######################################################################################

a = []
modified_a = []

for i in range(4):
    b = int(input("Enter Value : "))
    a.append(b)
print (a)

for i in a:
    if i % 3 == 0 and i % 5 == 0:
        modified_a.append("ThreeFive")
    elif i % 3 == 0:
        modified_a.append("Three")
    elif i % 5 == 0:
        modified_a.append("Five")
    else:
        modified_a.append(i)

print (modified_a)

# Enter Value : 10
# Enter Value : 15
# Enter Value : 12
# Enter Value : 7
# [10, 15, 12, 7]
# ['Five', 'ThreeFive', 'Three', 7]

####################################################################################

# a = [1,2,3,4,5,6,7]

# b = [11,12,13,14,15,16,17]


# a.append(1)
# print (a)
# a.insert(0,10)
# print (a)
# a.pop(6)
# print (a)
# a.extend(b)
# print (a)

# [1, 2, 3, 4, 5, 6, 7, 1]
# [10, 1, 2, 3, 4, 5, 6, 7, 1]
# [10, 1, 2, 3, 4, 5, 7, 1]
# [10, 1, 2, 3, 4, 5, 7, 1, 11, 12, 13, 14, 15, 16, 17]