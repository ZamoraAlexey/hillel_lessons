file_name = input('Create File: ')
file_use = open(file_name + '.txt', 'w')
while True:
    text_in_file = input()
    if text_in_file == '':
        break
    file_use.write(text_in_file + '\n')
file_use.close()
