from os import getlogin

def message():
    print(f"Hello from {getlogin()}. I am an alien from the andromeda galaxy")


message()