print("Welcome to the Mini calculations")

a = int(input("Enter the Value 1 : "))
b = int(input("Enter the Value 2 : "))

print(f"\nYour value are {a} and {b}")

c=a+b
d=a-b
e=a*b
f=a/b

print("\nSelect the calculation to calculate")

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

choice = input("\nEnter the number : ")
if choice == "1":
    print(f"addition = {c}")
elif(choice == "2"):
    print(f"Subtraction = {d}")
elif(choice == "3"):
    print(f"Multiplication = {e}")
elif (choice == "4"):
    print(f"Division = {f}")
else:
    print("Invalid Input")