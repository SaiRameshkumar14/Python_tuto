def app(a,b):
   for i in a:
    if i not in b:
        b.append(i)
   return b

def sort(b):
   return sorted(b)

a = []
b = []

n = int(input("Enter the number of elements : "))
for i in range(n):
    a.append(int(input(f"Enter the element for list a {i}: ")))
for i in range(n):
    b.append(int(input(f"Enter the element for list b {i}: ")))
     


app(a,b)
print(b)