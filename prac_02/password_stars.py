passwordmin = 8
def main():


    password = get_password(passwordmin)
    make_asterisks(password)


def make_asterisks(password: int):
    for i in range(0, password, 1):
        print("*", end="")


def get_password(passwordmin: int) -> int:
    password = len(input("Enter a Password: "))

    while password < passwordmin:
        print("Password is too short")
        password = input("Enter a Password: ")
    return password


main()