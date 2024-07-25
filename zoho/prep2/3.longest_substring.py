# problem 4:

# given a string. find the longest continuous substring without repeated characters 

# sample input: aweeacwerjkl
# output: acwerjkl

# sample input:asdsdah 
# output: sdah

def longest_unique_substring(s):
    start = 0
    max_length = 0
    max_substr = ""
    char_index = {}

    for end in range(len(s)):
        if s[end] in char_index:
            start = max(start, char_index[s[end]] + 1)
        
        char_index[s[end]] = end
        current_length = end - start + 1
        
        if current_length > max_length:
            max_length = current_length
            max_substr = s[start:end + 1]

    return max_substr

# Sample Input 1
input1 = "aweeacwerjkl"
print(longest_unique_substring(input1))  # Output: "acwerjkl"

# Sample Input 2
input2 = "asdsdah"
print(longest_unique_substring(input2))  # Output: "sdah"
