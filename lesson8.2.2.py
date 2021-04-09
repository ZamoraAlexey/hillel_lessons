list_of_authorized_users = ['Jobs', 'Cook', 'Wozniak']
authorization = input('Enter your name for authorization: ')


def logging(func):
    def wrapper():
        if authorization in list_of_authorized_users:
            func()
        else:
            print(authorization, ', its not for you!')
    return wrapper()


def secret():
    print('Im glad to see you,', authorization)


logging(secret)
