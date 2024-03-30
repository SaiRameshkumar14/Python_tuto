# Even odd count

a = int(input("Enter value 1 : "))
b = int(input("Enter value 2 : "))
count1 = 0
count2 = 0

for i in range(a+1,b):
    if (i%2 == 0):
        count1 +=1
    else:
        count2 +=1

print(f"Even count = {count1}")
print(f"Odd count = {count2}")