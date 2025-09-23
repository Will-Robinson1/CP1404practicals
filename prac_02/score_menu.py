def get_score():
    score = float(input("Enter score: "))
    while 0 > score or score >100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def print_score(score: float):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def show_stars(score: float):
        for i in range(0, int(score), 1):
            print("*", end="")
        print()

def main():
    menu = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print_score(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("See you later.")

main()