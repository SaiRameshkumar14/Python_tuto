def palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")
if palindrome(string):
    print(f"{string} is a palindrome!")
else:
    print(f"{string} is not a palindrome.")