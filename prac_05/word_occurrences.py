"""
Word Occurrences
Estimate: 30 minutes
Actual:   25 minutes
"""

def main():
    letter_to_count = {}
    get_text = input("Text: ")
    word = get_text.lower().split()

    for word in word:
        if word in letter_to_count:
            letter_to_count[word] += 1
        else:
            letter_to_count[word] = 1

    width = max(len(word) for word in letter_to_count)
    for word in sorted(letter_to_count):
        print(f"{word:{width}} : {letter_to_count[word]}")

main()