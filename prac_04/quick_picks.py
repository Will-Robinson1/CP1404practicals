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
        picks = []
        while len(picks) < NUMBERS_PER_PICK:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in picks:  # ensure uniqueness
                picks.append(number)
        picks.sort()
        print(" ".join(f"{n:2d}" for n in picks))

main()