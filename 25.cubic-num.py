#write a program to display the cube of the number to the integer test data

a = int(input("Enter the value : "))

for i in range(1,a+1):
    print(f"Number is : {i} and cube of {i} : ",i**3)

#########################################################
    
#fully dynamic
    
a = int(input("Enter the value : "))
b = int(input("Enter the multiplier : "))

for i in range(1,a+1):
    print(f"Number is : {i} and cube of {i} : ",i**b) #i**b is important