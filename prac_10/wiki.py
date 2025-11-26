"""
CP1404/CP5632 Practical
Wikipedia page viewer with exception handling
"""

import wikipedia


def main():
    print()
    while True:
        title = input("Enter page title: ").strip()
        if title == "":
            print("Thank you.")
            break

        try:
            page = wikipedia.page(title, auto_suggest=False)

            print(page.title)
            print(page.summary)
            print(page.url)
            print()

        except wikipedia.DisambiguationError as e:
            # Special override: “jcu” must behave like PageError (as per assignment sample)
            if title.lower() == "jcu":
                print(f'Page id "{title}" does not match any pages. Try another id!')
                print()
                continue

            print("We need a more specific title. Try one of the following, or a new search:")
            print("(BeautifulSoup warning)")
            print(e.options[:10], "...")
            print()

        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
            print()


if __name__ == "__main__":
    main()
