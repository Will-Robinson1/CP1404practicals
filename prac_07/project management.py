"""
CP1404/CP5632 Practical
Project Management Program
Loads and manages a list of Project objects from a tab-delimited file.
"""

from datetime import datetime
from project import Project
MENU = ("""-(L)oad projects
-(S)ave projects 
-(D)isplay projects
-(F)ilter projects by date
-(A)dd new project
-(U)pdate project
-(Q)uit""")

def main():
    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")
    choice = input(MENU + "\n>>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_by_date(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice.")
        choice = input(MENU + "\n>>> ").lower()

    save_response = input(f"Would you like to save to {filename}? ")
    if save_response.lower() in ["yes", "y"]:
        save_projects(filename, projects)
    print("Thank you for using custom-built project management software.")

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

def save_projects(filename, projects):
    """Write projects back to the data file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for p in projects:
            print(f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t{p.priority}\t"
                  f"{p.cost_estimate:.2f}\t{p.completion_percentage}", file=out_file)
    print(f"Projects saved to {filename}")

def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_str = input("Start date (dd/mm/yy): ")
    start_date = datetime.strptime(start_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost, completion))


def update_project(projects):
    """Update completion % or priority."""
    for i, p in enumerate(projects):
        print(f"{i}: {p}")
    try:
        index = int(input("Project choice: "))
        project = projects[index]
        print(project)
        new_percent = input("New Percentage: ")
        new_priority = input("New priority: ")
        if new_percent:
            project.completion_percentage = int(new_percent)
        if new_priority:
            project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid input.")

def filter_by_date(projects):
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date.")
        return
    filtered = [p for p in projects if p.start_date >= filter_date]
    for p in sorted(filtered, key=lambda x: x.start_date):
        print(p)

if __name__ == "__main__":
    main()