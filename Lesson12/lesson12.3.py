import csv

result = []
with open('students.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        result.append(row)
    print(result)
