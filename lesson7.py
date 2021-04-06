def calculate_of_numbers():

    first_number = int(input('Enter your first number: '))
    second_number = int(input('Enter your second number: '))
    choice_function = input('Choice your function (+, -, /, //, *, **, %): ')

    if choice_function == '+':
        print(f'{first_number} + {second_number} =', first_number + second_number)
    elif choice_function == '-':
        print(f'{first_number} - {second_number} =', first_number - second_number)
    elif choice_function == '**':
        print(f'{first_number} ** {second_number} =', first_number ** second_number)
    elif choice_function == '*':
        print(f'{first_number} * {second_number} =', first_number * second_number)
    elif choice_function == '//':
        print(f'{first_number} // {second_number} =', first_number // second_number)
    elif choice_function == '/':
        print(f'{first_number} / {second_number} =', first_number / second_number)
    elif choice_function == '%':
        print(f'{first_number} % {second_number} =', first_number % second_number)
    else:
        print('Invalid enter or function!')


calculate_of_numbers()
