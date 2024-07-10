n = 5

def rightangke(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end = ' ')
        print()

rightangke(n)



def box(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

        # * * * * * 
        # * * * * *
        # * * * * *
        # * * * * *
        # * * * * *

def uparrow(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()
        
    #     *
    #    ***
    #   *****
    #  *******
    # *********