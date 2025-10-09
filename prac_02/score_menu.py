MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""

def main():
    score = get_score()
    print(MENU)
    choice = input(">>> ").upper()


    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            result = print_score(score)
            print(result)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("See you later.")

def get_score():
    score = float(input("Enter score: "))
    while 0 > score or score >100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def print_score(score: float):
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

def show_stars(score: float):
        for i in range(0, int(score), 1):
            print("*", end="")
        print()

main()
