import os

while not False:
    file_name = input('Create File: ')
    if file_name != 'STOP':
        file_use = open(file_name + '.txt', 'a')
    else:
        break
    while True:
        text_in_file = input()
        if text_in_file == '':
            break
        file_use.write(text_in_file + '\n')
    file_use.close()
print(os.listdir('.'))

