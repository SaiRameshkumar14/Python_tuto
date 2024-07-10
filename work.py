def find_elements_with_max_digit_presence(n, arr, d):
    d = str(d)
    max_count = 0
    result = []
    
    # Convert all elements to strings to handle leading zeros
    str_arr = []
    for num in arr:
        str_arr.append(str(num))
    
    # Find the maximum count of digit d in any element
    for num in str_arr:
        count = num.count(d)
        if count > max_count:
            max_count = count
    
    # Collect elements with the maximum count of digit d
    for num in str_arr:
        if num.count(d) == max_count:
            result.append(num)
    
    return result

# Test case
n = 5
arr = [22,234,252,255,282]
d = 2

output = find_elements_with_max_digit_presence(n, arr, d)
print(*output, end='')
