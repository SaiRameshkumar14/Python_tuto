#write a program to read 10 numbers from the keyboard and find their sum and average

a = []
b = 0
for i in range(10):
    num = int(input(f"Enter the {i} value : "))
    a.append(num)
print(a)

for i in a:
    b += i
print(f"Total = {b}")
print("Avg =",float(b/10))

################################################################

# fully dynamic


a = []
b = 0
c = int(input("Enter length of list : "))

print(f"\nENTER THE {c} VALUES\n")

for i in range(1,c+1):
    num = int(input(f"Enter {i} value : ")) # or num = int(input(Enter value : "+str(i+1)))
    a.append(num)
print(a)

for i in a:
    b += i
print(f"Total = {b}")
print("Avg =",float(b/c))
