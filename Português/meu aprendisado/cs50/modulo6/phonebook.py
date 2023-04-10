import csv
from sys import exit

with open("phonebook.csv", 'a') as file:
    if file == None:
        exit(1)
    peopel = [input("Your name: "), input("Your number: ")]
    write = csv.writer(file)
    write.writerow(peopel)
    
