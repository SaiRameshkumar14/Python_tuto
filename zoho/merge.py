def app(a,b):
   for i in a:
    if i not in b:
        b.append(i)
   return b

def sort(b):
    n = len(b)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]

a = []
b = []

n = int(input("Enter the number of elements : "))
for i in range(n):
    a.append(int(input(f"Enter the element for list a {i}: ")))
for i in range(n):
    b.append(int(input(f"Enter the element for list b {i}: ")))
     


app(a,b)
print(b)

print("sorted b :", sort(b))