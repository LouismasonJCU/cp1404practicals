from fileinput import filename

from prac_07.guitar import Guitar

FILENAME = "guitars.txt"

def main():
    """load and display guitars"""
    guitars = load_guitars(FILENAME)
    print(guitars)

def load_guitars(FILENAME):
    """LOAD OBJECTS FROM THE FILES"""
    guitars = []
    return guitars


main()