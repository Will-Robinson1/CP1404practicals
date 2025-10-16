"""
Word Occurrences
Estimate: 30 minutes
Actual:   25 minutes
"""

def main():
    counts = {}
    get_text = input("Text: ")
    word = get_text.lower().split()

    for word in word:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    width = max(len(word) for word in counts)
    for word in sorted(counts):
        print(f"{word:{width}} : {counts[word]}")

main()