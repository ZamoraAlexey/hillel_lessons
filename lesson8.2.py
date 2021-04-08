list_of_authorized_users = ['Steve Jobs', 'Tem Cook', 'Steve Wozniak', 'Jonny Ive']
entered_user = input('Enter your name for authorize: ')


def decorator(checking):
    print('Authorize of user')
    checking()
    print('Successful')
    return checking


@decorator
def secret():
    if entered_user in list_of_authorized_users:
        print(entered_user)
    else:
        print('NOT')
