try:
    a = int(input("Enter Value 1 : "))
    b = int(input("Enter Value 2 : "))
    for i in range(a,b):
        if(i%2==0):
            print(i)
except ValueError :
    print("Invalid input. Please enter a valid numeric value.")