import csv

with open("favorites.csv",'r') as favorites:
    reader = csv.reader(favorites)
    next(reader)
    for row in reader:
        print(row[0],row[1],row[2])