from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import csv

path = Path('weather_data/sitka_weather_2021_simple-original.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)

header_row = next(reader)

print(header_row)

indicies = {}
for index, column_header in enumerate(header_row):
    indicies[column_header] = index
print(indicies)


dates, highs, lows, = [], [], [],
for row in reader:
    current_date = datetime.strptime(row[indicies['DATE']], '%Y-%m-%d')
    try:
        high = int(row[indicies['TMAX']])
        low  = int(row[indicies['TMIN']])

    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)



plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(dates, highs, c='red', label='Highs')
ax.plot(dates, lows, c='blue', label='Lows')

ax.fill_between(dates, highs, lows, facecolor='purple', alpha=0.1)
title = ('Daily High and Low Temperatures, of selected locations')
ax.set_title(title, fontsize=20)
ax.set_xlabel('Day', fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)
fig.autofmt_xdate()
plt.show()


