# getting percentage
try:
    n = int(input("Enter Your Percentage : "))

    if n <= 100:
        if n > 70:
            print(f"YOU ARE ELIGIBLE FOR SCHOLARSHIP\n--Because {n} is Greater than 70%--")
            name = input ("Enter Your Name : ")
            dept = input ("Enter Your Department : ")
            location = input(("Enter Your Location : "))
            print(f"Hi {name}, Your are from {location} and you booked {dept} for further education")
        else:
            print(f"You are not eligible because {n} is less than 70%")
    else:
        print(f"Invalid Percentage : {n}")
except ValueError:
    print("Invalid input. Please enter a valid numeric value.")
