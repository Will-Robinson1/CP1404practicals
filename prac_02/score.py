"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    score = get_score()
    result = determine_result(score)
    print(result)
    score = random.randint(0, 100)
    result = determine_result(score)
    print("Random number: ", score)
    print(result)


def get_score() -> float:
    score = float(input("Enter score: "))
    return score


def determine_result(score: float):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()