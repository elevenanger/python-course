import json
from json import JSONDecodeError


def get_stored_user():
    filename = 'username.json'
    try:
        with open(filename, 'r') as file:
            username = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        return None
    else:
        return username


def get_new_username():
    username = input("你的名字是：")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)


def greet_user():
    username = get_stored_user()
    if username:
        print(f"你好：{username}")
    else:
        get_new_username()


greet_user()
