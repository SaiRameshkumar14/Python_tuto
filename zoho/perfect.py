def is_perfect_number(n):
    if n < 2:
        return False
    
    sum_of_divisors = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:
                sum_of_divisors += n // i
                
    return sum_of_divisors == n

# Example usage
numbers = [6, 28, 496, 8128, 12, 15]
for number in numbers:
    if is_perfect_number(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")

################################################################

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
