#Rail Reservation booking using python

User_Data = {} #Dictionary


def userinput():
    User = int(input('WELCOME TO RAILWAY RESERVATION \n\n1) New User \n2) Old User \n\nEnter the option : '))

    if User == 1:
        name = input('Enter the Name :')
        age = int(input('Enter the Age :'))
        gender = input('Enter the Gender :')
        phone = int(input('Enter the phone :'))
        email = input('Enter the email :')
        User_Data[name] = {'Age' : age, 'Gender' : gender, 'Phone' : phone, 'Email': email}
        print (User_Data[name])
        userinput()


    elif User == 2:
        name = input('Enter the name : ')
        if name in User_Data:
            print(f'\nWelcome {name}')
            query = int(input(f'\nChoose option {name} :'))
            print ('\n',User_Data[name])
            userinput()
        else:
            print('User not found')
            userinput()


userinput()



