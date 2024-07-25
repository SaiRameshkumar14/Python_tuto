def binarysearch(arr,target):
    left = 0
    right = len(arr)
    
    while left <= right:
        mid = round((left+right) /2)
        
        if arr[mid] == target:
            return mid
            
        elif arr[mid] < target:
            left = mid +1
            
        else:
            right = mid-1
            
    return print("Target is not in array")
            
arr = [1, 2, 3, 4, 10, 12]
    
print(binarysearch(arr,7))

def count(number, target):
    """Count the occurrences of the target digit in the given number."""
    count = 0
    while number > 0:
        digit = number % 10
        if digit == target:
            count += 1
        number = number // 10
    return count

def contains(number, target):
    """Check if the number contains the target digit."""
    while number > 0:
        digit = number % 10
        if digit == target:
            return True
        number = number // 10
    return False

input_list = [2, 252, 22, 232, 42]
target = 2

# Filter the list to include only numbers that contain the target digit
arr = []
for num in input_list:
    if contains(num, target):
        arr.append(num)

# Sort the filtered list based on the count of the target digit in descending order
for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if count(arr[j], target) < count(arr[j + 1], target):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
