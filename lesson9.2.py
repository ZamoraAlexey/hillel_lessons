list_of_sportsmen = [
    ['Alex', 10, 130, 35],
    ['Maria', 11, 135, 39],
    ['Olga', 9, 140, 33],
    ['Dmytro', 10, 128, 30]
]

choice = input('Choice sort by name (1), age (2), weight (3), height (4): ')
choice = int(choice) - 1

list_of_sportsmen.sort(key=lambda index: index[choice])

for index in list_of_sportsmen:
    print(f'{index[0]}, {index[1]}, {index[2]}, {index[3]}')
