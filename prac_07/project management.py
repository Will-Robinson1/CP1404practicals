"""
CP1404/CP5632 Practical
Project Management Program
Loads and manages a list of Project objects from a tab-delimited file.
"""

from datetime import datetime
from project import Project
MENU = "(D)isplay projects\n(Q)uit"
def main():
    projects = load_projects("projects.txt")
    choice = input(MENU + "\n>>> ").lower()
    while choice != "q":
        if choice == "d":
            display_projects(projects)
        else:
            print("Invalid choice.")
        choice = input(MENU + "\n>>> ").lower()
    print("Goodbye!")

def load_projects(filename):
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()
        for line in in_file:
            name, start_str, priority, cost, completion = line.strip().split("\t")
            start_date = datetime.strptime(start_str, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority),
                                    float(cost), int(completion)))
    return projects


def display_projects(projects):
    """Show incomplete and completed projects sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()],
                        key=lambda x: x.priority)
    complete = sorted([p for p in projects if p.is_complete()],
                      key=lambda x: x.priority)
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")

if __name__ == "__main__":
    main()