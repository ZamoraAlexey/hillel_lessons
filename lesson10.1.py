# FIRST TASK

def fibonacci(number):
    if number in (1, 2):
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(4))


# SECOND TASK

check_palindrome = input("Enter your palindrome word/phrase: ").replace(' ', '').lower()
string_of_input = len(check_palindrome)
index = 0
for i in range(string_of_input):
    if check_palindrome[i] == check_palindrome[-(i+1)]:
        index = index + 1
if index == string_of_input:
    print("Its a palindrome")
else:
    print("Its not a palindrome")
