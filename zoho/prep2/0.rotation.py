def rotate_string(s, r, n):
    length = len(s)
    result = [''] * length

    # Left Rotation
    if r == "L-ROTATION":
        for i in range(length):
            new_pos = (i - n) % length
            result[new_pos] = s[i]
    
    # Right Rotation
    elif r == "R-ROTATION":
        for i in range(length):
            new_pos = (i + n) % length
            result[new_pos] = s[i]
    
    return ''.join(result)

# Sample Input 1
s1 = "ZOHOCORPORATION"
r1 = "L-ROTATION"
n1 = 4
print(rotate_string(s1, r1, n1))  # Output: "CORPORATIONZOHO"

# Sample Input 2
s2 = "HELLO"
r2 = "R-ROTATION"
n2 = 4
print(rotate_string(s2, r2, n2))  # Output: "ELLOH"
