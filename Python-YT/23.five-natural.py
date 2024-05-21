#write a program to compute the sum of first 5 natural numbers

a = int(input("Enter value 1 : "))
b = int(input("Enter value 2 : "))

sum = 0

for i in range (a,b+1):
    sum += i

print(sum)

