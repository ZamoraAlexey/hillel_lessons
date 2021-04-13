matrix = [[3, -2, 6, 4], [8, 1, 12, 2], [5, 4, -8, 0]]

def sort_of_numbers(list_of_numbers):
    for i in range(len(list_of_numbers)):
        start_index = i
        for j in range(i + 1, len(list_of_numbers)):
            if list_of_numbers[j] < list_of_numbers[start_index]:
                start_index = j
        list_of_numbers[i], list_of_numbers[start_index] = list_of_numbers[start_index], list_of_numbers[i]
    print(list_of_numbers)


sort_of_numbers(matrix[0])
for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()


