"""
CP1404/CP5632 Practical
Project Management Program
Loads and manages a list of Project objects from a tab-delimited file.
"""

from datetime import datetime, date
from project import Project

def main():
    projects = load_projects("projects.txt")
    print("Loaded projects:")
    for p in projects:
        print(p)

def load_projects(filename):
    """Read projects from a tab-delimited file."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            name, start_str, priority, cost, completion = line.strip().split("\t")
            start_date = datetime.strptime(start_str, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority),
                                    float(cost), int(completion)))
    return projects

if __name__ == "__main__":
    main()