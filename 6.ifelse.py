if(True):
    print("Yes")
else:
    print("No")

################################################################
    
num = int(input("Enter value : "))

if (num%2 == 0):
    print("Even")
else:
    print("Odd")

################################################################
    
mark = int(input("Enter mark : "))

if (mark>35):
    print("pass")
elif(mark<35):
    print("fail")
else:
    print("Invalid")

################################################################

print("Select one option")
print("a. megna\nb. sana")

get = input("Enter : ")

if (get == "a"):
    print("You love Megna")
elif (get == "b"):
    print("You Love Sana")
else:
    ("Invalid input")

################################################################
    
score= int(input("Enter score : "))

if (score<35):
    print("Poor Student")

if(score > 35 and score < 70):          # using if only
    print("Average Student")

if (score > 70 and score < 90):
    print("Good Student")

else:
    print("Perfect Student")


score= int(input("Enter score : "))

if (score<35):
    print("Poor Student")

elif(score > 35 and score < 70):        # using elif
    print("Average Student")

elif (score > 70 and score < 90):
    print("Good Student")

else:
    print("Perfect Student")

################################################################
    
