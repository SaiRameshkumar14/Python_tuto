# num = int(input("Enter value : "))

# if (num%2 == 0):
#     print("Even")
# else:
#     print("Odd")

score= int(input("Enter score : "))

if (score<35):
    print("Poor Student")

elif(score > 35 and score < 70):
    print("Average Student")

elif (score > 70 and score < 90):
    print("Good Student")

else:
    print("Perfect Student")