from pathlib import Path
import json

username = input("Hey there! What's your name?   ")

path = Path('username.json')
content = json.dumps(username)
path.write_text(content)

print(f'Awesome! I\'ll remember that for later. See you later {username}.')