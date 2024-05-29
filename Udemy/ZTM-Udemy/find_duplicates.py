a = [1,2,2,3,4,2,3,4,5,6,7,8]
b = []

#taking element in a
for i in a:
    #counting the element in a , if it more than one.
    if a.count(i) > 1:
        #checking if the element is already in the b
        if i not in b:
            #appending the element in b
            b.append(i)

print (b)    #[2, 3, 4]

print(list(set(b)))   #[2, 3, 4]

