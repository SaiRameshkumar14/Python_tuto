def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
