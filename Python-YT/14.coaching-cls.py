try:
    a = int(input("Enter Mark 1 : "))
    b = int(input("Enter Mark 2 : "))
    c = int(input("Enter Mark 3 : "))
    d = int(input("Enter Mark 4 : "))
    e = int(input("Enter Mark 5 : "))
    total = a+b+c+d+e
    print(f"\nTotal Mark = {total}")
    avg = float(total)/5
    print(f"\nYour Average mark\n{total}/5 = {avg}")

    if avg <35:
        print("\nAdditional class is needed")
    else:
        print("\nYou are good to go -->")
    #print(f"\nAverage Mark is {((a+b+c+d+e)/5):.2f}") 
    # :.2f means float value , output 3.12 / :.3f output is 3.123

except ValueError :
    print("Invalid input. Please enter a valid numeric value.")