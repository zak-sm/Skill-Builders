from pathlib import Path
import json

numbers = [2,5,21,23,43,2,1,5,8,7,5]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)
