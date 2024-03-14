# getting percentage

n = int(input("Enter the percentage value : "))

if n <= 100:
    if n >= 70:
        print(f"You are Eligible because {n}% is greater than 70%")
        name = input("Enter your Name : ")
        depart = input("Enter your Department : ")
        location = input("Enter your Location : ")
        print(f"Hello {name}, You are eligible for the following {depart} Department at {location}")
    else:
        print(f"You are Not Eligible because {n}% is less than 70%")
else:
    print("Invalid percentage")