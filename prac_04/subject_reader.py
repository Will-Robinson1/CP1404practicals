"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    imported_subject_data = load_data_from_file(FILENAME)
    details = prints_subject_details(imported_subject_data)
    print(details)

def load_data_from_file(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    records = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        records.append(parts)
    return records

def prints_subject_details(records):
    subject_details = [f"{subject} is taught by {lecturer} and has {students} students" for subject, lecturer, students in records]
    return "\n".join(subject_details)
main()