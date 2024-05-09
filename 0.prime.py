
n = int(input("Enter Value : "))
flag = 0

for i in range(2,n):
    if n % i == 0:
        flag = 1
        break

if flag == 1:
    print("Not Prime")
else:  
    print("Prime")


# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def find_primes_between(num1, num2):
#     prime_numbers = []
#     for num in range(num1, num2):
#         if is_prime(num):
#             prime_numbers.append(num)
#     return prime_numbers

# # Example usage:
# num1 = 1
# num2 = 100
# prime_numbers_between_1_and_100 = find_primes_between(num1, num2)
# print("Prime numbers between 1 and 100:", prime_numbers_between_1_and_100)

