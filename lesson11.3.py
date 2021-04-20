import re

entered_password = input("Enter your password")
password = True

while password:
    if len(entered_password) <= 8 or len(entered_password) > 16:
        break
    elif not re.search('[a-z]', entered_password):
        break
    elif not re.search("[0-9]", entered_password):
        break
    elif not re.search("[A-Z]", entered_password):
        break
    elif not re.search("[$#@]", entered_password):
        break
    elif re.search("\s", entered_password):
        break
    else:
        print("Valid Password")
        password = False
        break

if password:
    print("Not a Valid Password")