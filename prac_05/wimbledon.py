"""
estimated time to create this question : 1 hour 30 minutes
actual time : 2 hours 15 minutes
"""
from fileinput import filename

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)

def load_records(filename):
    """load records from list form"""
    records = []
    with open(filename,'r', encoding ="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records

def process_records(records):
    """process records from list form"""
    champion_to_count ={}
    countries = set()
    for record in records :
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries

def display_results(champion_to_count, countries):
    """Display champions and countries."""
    print("Wimbledon Champions: ")
    for champion, count in champion_to_count.items():
        print(champion, count)
    print()
    print(f"these {len(countries)} countries have won wimbledon :")
    print(','.join(sorted(countries)))


main()