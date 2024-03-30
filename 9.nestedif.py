num = int(input("Enter score : "))
if num < 100:
    if (num<35):
        print("Poor student")
    elif(num < 35 and num > 0):
        print("Average Student")
    elif(num < 70 and num >90):
        print("Good student")
    elif(num > 90):
        print("Excellent student")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")