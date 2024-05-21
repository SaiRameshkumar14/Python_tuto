a = int(input("Enter value 1 : "))
b = int(input("Enter value 2 : "))

e_count = 0
o_count = 0

for i in range(a+1,b):
    if (i%2==0):
        e_count +=1
    else:
        o_count+=1

print(f"Even count = {e_count}")
print(f"Odd count = {o_count}")