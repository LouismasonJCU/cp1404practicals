"""
estimated time to create this question : 1 hour 30 minutes
actual time :
"""
from fileinput import filename

FILENAME = "wimbledon.csv"

def main():
    records = load_records(FILENAME)
    print(records)

def load_records(filename):
    """load records from list form"""
    records = []
    with open(filename,'r', encoding ="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records

main()