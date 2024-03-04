def palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")
if palindrome(string):
    print(f"{string} it's a palindrome!")
else:
    print(f"{string} it's not a palindrome.")