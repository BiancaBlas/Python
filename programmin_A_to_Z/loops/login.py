def login(username: str, password: str) -> bool:
    is_authenticated = False

    if username == "admin" and password == "1234":
        is_authenticated = True
    return is_authenticated

user = input("Username: ")
passw = input("Password: ")

logged_in = login(user, passw)

"""
message = "Login failed, check your credentials"

if logged_in:
    message = "Login succesful"

print(message)
"""
# or code below for more compact code

print("Login succesful" if logged_in else "Login failed, check your credentials")


