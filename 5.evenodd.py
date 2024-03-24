num = int(input("Enter value : "))

if (num%2 == 0):
    print("Even")
else:
    print("Odd")

####################################################

#Simple If-Else Statement:

def odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print(odd_even(number))


####################################################

#Using Ternary Operator:
# This is a concise way of writing the same logic using a ternary conditional operator.

def odd_even(num):
    return "Even" if num % 2 == 0 else "Odd"

number = int(input("Enter a number: "))
print(odd_even(number))


####################################################    

#Using Bitwise AND Operator:
# Utilizing bitwise AND operator &, you can determine the parity of a number.

def odd_even(num):
    return "Even" if (num & 1) == 0 else "Odd"

number = int(input("Enter a number: "))
print(odd_even(number))

######################################################

#Using Python's divmod() Function:
# The divmod() function returns a tuple containing the quotient and remainder. 
# We can use the remainder to determine if the number is odd or even.

def odd_even(num):
    _, remainder = divmod(num, 2)
    return "Even" if remainder == 0 else "Odd"

number = int(input("Enter a number: "))
print(odd_even(number))