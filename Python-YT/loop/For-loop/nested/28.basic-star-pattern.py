##################################################################

#basic star pattern without using nested loop

a = int(input("Enter the star value : "))
b = "*"

for i in range(1,a+1):
    print(i*b)


###################################################################
    
#basic star pattern using nested loop
    
f = int(input("Enter the star value : "))

for i in range(1,f+1):
    print()
    for i in range(1,i+1):
        print("*",end="")

####################################################################

def star(n):
    for i in range(n,0, -1):
        print("*" * i)

n = int(input())
star(n)
        