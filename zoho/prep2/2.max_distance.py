# PROBLEM 3:

# given a string, find the maximum distance between the same two characters 

# sample inputl: abacdeefghdei
# sample output: 5

# sample input: abcbda 
# sample output: 4

def max_distance(s):
    # Create dictionaries to store the first and last occurrence of each character
    first_occurrence = {}
    last_occurrence = {}
    
    # Iterate through the string to fill the dictionaries
    for i in range(len(s)):
        if s[i] not in first_occurrence:
            first_occurrence[s[i]] = i
        last_occurrence[s[i]] = i
    
    # Initialize the maximum distance to zero
    max_dist = 0
    
    # Iterate through the characters in the first_occurrence dictionary
    for char in first_occurrence:
        # Calculate the distance between the first and last occurrence of the character
        dist = last_occurrence[char] - first_occurrence[char]
        # Update the maximum distance if the current distance is larger
        if dist > max_dist:
            max_dist = dist-1
    
    return max_dist

# Sample Input 1
input1 = "abacdeefghdei"
print(max_distance(input1))  # Output: 5

# Sample Input 2
input2 = "abcbda"
print(max_distance(input2))  # Output: 4

