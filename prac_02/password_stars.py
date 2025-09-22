def main():
    passwordmin = 8

    password = get_password(passwordmin)
    mak_asterisks(password)


def mak_asterisks(password: int):
    for i in range(0, password, 1):
        print("*", end="")


def get_password(passwordmin: int) -> int:
    password = len(input("Enter a Password: "))

    if password < passwordmin:
        print("Password is too short")
        password = input("Enter a Password: ")
    return password


main()