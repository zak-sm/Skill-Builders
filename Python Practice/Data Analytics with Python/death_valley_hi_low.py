from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import csv

path = Path('weather_data/death_valley_2021_full.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)

header_row = next(reader)

print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)


dates, highs, lows, tobs, rainfall = [], [], [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[6])
        low  = int(row[7])
        tob = int(row[8])
        rain = float(row[3])
    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        tobs.append(tob)
        rainfall.append(rain)


plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(dates, highs, c='red', label='Highs')
ax.plot(dates, lows, c='blue', label='Lows')
ax.plot(dates, tobs, c='green', label='Average Temperatures')
ax.plot(dates, rainfall, c='orange', label='Rainfall')
ax.fill_between(dates, highs, lows, facecolor='purple', alpha=0.1)
title = ('Daily High and Low Temperatures, 2021\nDeath Valley, CA')
ax.set_title(title, fontsize=20)
ax.set_xlabel('Day', fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)
fig.autofmt_xdate()
plt.show()


