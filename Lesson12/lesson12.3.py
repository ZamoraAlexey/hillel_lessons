import csv

with open('students.csv') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)
        row = dict(row)


