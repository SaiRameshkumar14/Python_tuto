a = [1,2,3,4,5,6,7]

b = [11,12,13,14,15,16,17]


a.append(1)
print (a)
a.insert(0,10)
print (a)
a.pop(6)
print (a)
a.extend(b)
print (a)

[1, 2, 3, 4, 5, 6, 7, 1]
[10, 1, 2, 3, 4, 5, 6, 7, 1]
[10, 1, 2, 3, 4, 5, 7, 1]
[10, 1, 2, 3, 4, 5, 7, 1, 11, 12, 13, 14, 15, 16, 17]


################################################################################################


a = [1,2,3,4,5,6]

#type
print(type(a)) # <class 'list'>

#print using index value - 0,1,2,3,4,5,6.......
print(a[0]) # 1
print(a[1]) # 2
print(a[2]) # 3
print(a[3]) # 4
print(a[4]) # 5

#print list
print(a)        # [1,2,3,4,5,6]

#append function - it will add element in end only
a.append(0)     # [1,2,3,4,5,6,0]
a.append("hi")  # [1,2,3,4,5,6,0,'hi']
a.append(True)  # [1,2,3,4,5,6,0,'hi',True]
a.append(6)     # [1,2,3,4,5,6,0,'hi',True,6]

print(a)        # output - [1,2,3,4,5,6,0,'hi',True,6]


#insert function - add value in given position.

b = [2,3,4,5,6]

b.insert(0,1)  # 0 is index value, 1 is integer value
print(b)        # output - [1,2,3,4,5,6]
b[0] = 10       # replace integer using the index value
print(b)        # output - [10,2,3,4,5,6]

#pop function - remove value from last and also remove using index value

b.pop()       # remove last value
print(b)        # output - [10,2,3,4,5]
b.pop(0)      # remove value at index 0
print(b)        # output - [2,3,4,5]

#extend function - merge two list

a.extend(b)   # a is 1, b is 2
print(a)
        
b.extend(a)   # b is 1, a is 2
print(b)
