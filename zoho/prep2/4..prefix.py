def zoho(strs):
    if len(strs) == 0:
        return ""
    
    temp = strs[0]
    
    for i in range(1, len(strs)):
        while strs[i].find(temp) != 0:
            temp = temp[:-1]
            if temp == "":
                return ""
    
    return temp

# Example usage
strs = ["flower", "flow", "flight"]
print(zoho(strs))  # Output: "fl"


def zoho(strs):
    if len(strs) == 0:
        return ""
    
    # Find the minimum length of the strings
    min_length = len(strs[0])
    for s in strs:
        if len(s) < min_length:
            min_length = len(s)
    
    # Compare characters one by one
    for i in range(min_length):
        char = strs[0][i]
        for s in strs:
            if s[i] != char:
                return strs[0][:i]
    
    return strs[0][:min_length]

# Example usage
strs = ["flower", "flow", "flight"]
print(zoho(strs))  # Output: "fl"
