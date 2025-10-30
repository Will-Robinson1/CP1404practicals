"""
Wimbledon
Estimate: 30 minutes
Actual:   33 minutes
"""

FILENAME = "wimbledon.csv"

def load_data(filename):
    rows = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        header = in_file.readline()  # discard header
        for line in in_file:
            parts = line.strip().split(",")
            # Expecting columns like: Year,Country,Champion or similar per row
            rows.append(parts)
        return rows

def build_stats(rows):
    champion_to_wins = {}
    countries = set()

    for parts in rows:
        if len(parts) < 3:
            continue
        year, country, champion = parts[0], parts[1], parts[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1 # Count champion wins
        countries.add(country) # Collect country codes
    return champion_to_wins, countries

def display_results(champion_to_wins, countries):
    print("Wimbledon Campions:")
    for champion in champion_to_wins:
        print(f"{champion} {champion_to_wins[champion]}")

    print()
    sorted_countries = sorted(countries)
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))
def main():
    rows = load_data(FILENAME)
    champion_to_wins, countries = build_stats(rows)
    display_results(champion_to_wins, countries)


if __name__ == "__main__":
    main()