from pathlib import Path
import json

path = Path('username.json')
content = path.read_text()
username = json.loads(content)


print(f' Hey again {username}! It\'s good to see you again :)')