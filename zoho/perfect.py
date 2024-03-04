def perfect(n):
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_of_divisors == n

try:
    n = int(input("Enter the number: "))
    if perfect(n):
        print("Given number is a perfect number")
    else:
        print("Given number is not a perfect number")
except ValueError:
    print("Invalid input. Please enter a valid numeric value.")

########################################################################

def perfect(n):
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_of_divisors == n

user_input = input("Enter the number: ")

if user_input.isdigit():  # Check if input is a positive integer
    n = int(user_input)
    if n <= 0:
        print("Invalid input. Please enter a positive integer.")
    elif perfect(n):
        print("Given number is a perfect number")
    else:
        print("Given number is not a perfect number")
else:
    print("Invalid input. Please enter a valid numeric value.")
