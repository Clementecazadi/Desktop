import csv
from sys import argv, exit

def main():
    agatc = 0
    agatc1 = 0
    count = 0
    if len(argv) != 3:
        print("Usage: python dna.py database/large.csv sequences/nº.txt")
        exit(1)
    with open(argv[2], 'r') as data:
        dna = data.read()
        for start in range(0, len(dna), 8):
            print(dna[start: start + 8])
        
    print(agatc)
    with open(argv[1], "r") as people:
        list_people = csv.reader(people)
        next(list_people)
        for row in list_people:
            print(row)

main()