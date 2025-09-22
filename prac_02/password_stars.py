passwordmin = 8

password = len(input("Enter a Password: "))

if password < passwordmin:
    print("Password is too short")
    password = input("Enter a Password: ")
elif password >= passwordmin:
    for i in range(0,password,1):
            print("*", end="")