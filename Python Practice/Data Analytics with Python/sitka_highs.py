from pathlib import Path
import csv

path = Path('Python Practice/Data Analytics with Python/weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

# Assuming the first line contains the column names
reader = csv.reader(lines)
header_row = next(reader)

print(header_row)