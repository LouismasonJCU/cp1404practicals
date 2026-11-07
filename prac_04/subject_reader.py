"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject = []
    input_file = open(filename)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        parts[2] = int(parts[2])
        # print(parts)  # See if that worked
        # print("----------")
        subject.append(parts)
    input_file.close()
    return subject

def display_subjects(subjects):
    for subject in subjects:
        # print(subject)
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:4} students.")




main()
