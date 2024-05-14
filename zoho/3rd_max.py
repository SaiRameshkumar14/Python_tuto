def largest(n):
    sort = sorted(n, reverse=True)
    print(sort)
    e = int(input("Enter the largest number : "))

    if len(sort) >= e:
        return f"The {e}rd largest number is",sort[e-1]
    else:
        print ("List is not have morethan 2 numbers")


a = []
list_len = int(input("Enter List Length : "))
for i in range(list_len):
    a.append(int(input(f"Enter Value {i}: ")))

print(largest(a))

# Enter List Length : 5
# Enter Value 0: 12
# Enter Value 1: 13
# Enter Value 2: 14
# Enter Value 3: 178
# Enter Value 4: 89
# [12, 13, 14, 178, 89]
# [178, 89, 14, 13, 12]
# Enter the largest number : 3
# ('The 3rd largest number is', 14)

########################################################################

def third_largest_number(nums):
    if len(nums) < 3:
        return "List does not have at least three elements"
    
    first_largest = second_largest = third_largest = float('-inf')  # Initialize variables with negative infinity
    
    for num in nums:
        if num > first_largest:
            third_largest = second_largest
            second_largest = first_largest
            first_largest = num
        elif second_largest < num < first_largest:
            third_largest = second_largest
            second_largest = num
        elif third_largest < num < second_largest:
            third_largest = num
    
    return third_largest

# Example usage
my_list = []
list_len = int(input("Enter List Length : "))
for i in range(list_len):
   my_list.append(int(input(f"Enter Value {i}: ")))

print("Third largest number:", third_largest_number(my_list))
