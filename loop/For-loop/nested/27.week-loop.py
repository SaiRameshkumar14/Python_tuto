for i in range(1,2+1):
    print(f"\nWeek : {i}\n")
    for j in range(1,3+1):
        print(f"    Day : {j}")


########################################################
        
#fully dynamic
        
week = int(input("How many week : "))

for i in range(1,week+1):
    print(f"Week : {i}")
    for j in range(1,8):
        if j == 1:
            print(f"    Day : {j} Monday")
        elif j == 2:
            print(f"    Day : {j} Tuesday")
        elif j == 3:
            print(f"    Day : {j} Wednesday")
        elif j == 4:
            print(f"    Day : {j} Thursday")
        elif j == 5:
            print(f"    Day : {j} Friday")
        elif j == 6:
            print(f"    Day : {j} Saturday")
        elif j == 7:
            print(f"    Day : {j} Sunday")