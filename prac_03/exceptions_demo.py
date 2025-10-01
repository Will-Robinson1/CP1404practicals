"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When either the numerator or denominator are not valid numbers
2. When will a ZeroDivisionError occur?
When the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Use an if loop to keep asking until the denominator isn't a 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")