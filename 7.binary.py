# AND = *

# True * True = True
# True * False = False
# False * True = False
# False * False = False


# OR = +

# True + True = True
# True + False = True
# False + True = True
# False + False = False


# NOT 

# True = False
# False = True

get = int(input("Enter Value : "))

if (get%3 == 0 and get%5 == 0):
    print ("Value divide by both 3 and 5")
elif (get%3 == 0):
    print("Value divisible by 3, not divisible by 5")
elif(get%5 == 0):
    print("Value divisible by 5, not divisible by 3")
else:
    print("Value not divisible by both 3 or 5")

################################

score= int(input("Enter score : "))

if (score<35):
    print("Poor Student")

if(score > 35 and score < 70):
    print("Average Student")

if (score > 70 and score < 90):
    print("Good Student")

else:
    print("Perfect Student")