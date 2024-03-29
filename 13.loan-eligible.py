salary =int(input("Enter Your Salary : "))
age = int(input("Enter Your Age : "))

if salary >= 20000 or age <= 25 :
    print("YOU ARE ELIGIBLE")
    loan = int(input("How Much Loan amount is Required : "))
    if loan <= 50000:
        print(f"{loan} is eligible for loan process")
    else:
        print(f"{loan} is not eligible for loan process\n---Because Loan Amount Limit is 50000---")
else:
    print("YOU ARE NOT ELIGIBLE")