import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    try:
        count = int(input("How many quick picks? "))
    except ValueError:
        print("Please enter an integer.")
        return

    for _ in range(count):
        pick = []
        while len(pick) < NUMBERS_PER_PICK:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in pick:  # ensure uniqueness
                pick.append(number)
        pick.sort()
        print(" ".join(f"{n:2d}" for n in pick))

main()