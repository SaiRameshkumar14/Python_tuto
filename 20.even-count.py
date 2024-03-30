# how many even numbers between 1 and 11

try:
    a = int(input("Enter Value 1 : "))
    b = int(input("Enter Value 2 : "))
    count= 0

    for i in range(a,b):
        if (i%2 == 0):
            #count = count +1
            count+=1
    print(f"Total even number between {a} and {b} is {count}")

except ValueError :
    print("Invalid input. Please enter a valid numeric value.")