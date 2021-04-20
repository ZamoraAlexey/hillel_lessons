invalid_attempts = 0

while invalid_attempts < 3:
    try:
        min_number = int(input("Enter your start number: "))
        max_number = int(input("Enter your finite number number: "))
        step = int(input('Enter step for your numbers: '))
    except ValueError:
        print("Its not a number! Try again.")

    invalid_attempts += 1
    for i in range(min_number, max_number + step, step):
        print(i)
