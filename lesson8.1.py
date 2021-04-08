# FIRST TASK

list_of_numbers: list[int] = []
for number in range(0, 100):
    list_of_numbers.append(number)


print(list(filter(lambda x: x % 3 == 0, list_of_numbers)))


# SECOND TASK
# Version - 1

some_list_of_numbers = map(lambda x, y: x ** y, [5, 6, 7, 8], [1, 2, 3, 4])
print(list(some_list_of_numbers))


# version - 2

list_of_numbers1 = [5, 6, 7, 8]
list_of_numbers2 = [1, 2, 3, 4]
print(list(map(lambda x, y: x ** y, list_of_numbers1, list_of_numbers2)))
