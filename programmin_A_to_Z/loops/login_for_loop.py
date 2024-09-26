def login(username: str, password: str) -> bool:
    is_authenticated = False

    if username == "admin" and password == "1234":
        is_authenticated = True

    return is_authenticated

user = input("Username: ")
passw = input("Password: ")

is_authencated = False

for attempt in range(4):
    if login(user, passw) == True:
        is_authencated = True
        break
    else:
        print("Login failed, re-enter your credentials.")
        user = input("Username: ")
        passw = input("Password: ")

print("Login succesful" if is_authencated else "Your account has ben temporarily locked.")