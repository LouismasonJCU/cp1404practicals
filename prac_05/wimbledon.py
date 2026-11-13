"""
estimated time to create this question : 1 hour 30 minutes
actual time :
"""
FILENAME = "wimbledon.csv"

def main():
    records = load_records(FILENAME)

def load_records(FILENAME):
    """load records from list form"""
    records = []
    with open(FILENAME,'r', encoding ="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.split(",")
            records.append(parts)
    print(records)

main()