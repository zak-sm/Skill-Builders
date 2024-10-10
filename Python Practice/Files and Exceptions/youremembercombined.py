from pathlib import Path
import json



def get_stored_user(path):
    if path.exists():
        content = path.read_text()
        username = json.loads(content)
        return username
    else: return None

def greet_user():
    path = Path('username.json')
    username = get_stored_user(path)
    if username:
        print(f'Hey there {username}! It\'s good to see you agign.')
    else: new_user(path)

def new_user(path):
    username = input(f'Hey! What\'s your name?')
    content = json.dumps(username)
    path.write_text(content)
    print(f'Awesome! Well I will make sure to remember that from now on {username}. See you next time! :)')

greet_user()