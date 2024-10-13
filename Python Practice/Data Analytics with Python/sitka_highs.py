from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Create the path to the CSV file and read the file content
path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()


#Build a reader object for the CSV file
#The reader will remain in its current position, its like an auto parser that reads each line as you go
reader = csv.reader(lines)
header_row = next(reader)

print(header_row)

#extrat dates and high temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(current_date)
    highs.append(int(row[4]))
    lows.append(int(row[5]))


#plot the high temperatures
#initialize the plot
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
#Fills the space between the high and low values, alpha is the transparency of the fill
#Fn takes one x value and two y values and fills the space between them
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


#set title and labels
ax.set_title('Daily High and Low Temperaturess, 2021', fontsize=20)
ax.set_xlabel('Day', fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)
fig.autofmt_xdate()
ax.tick_params(labelsize=10)

plt.show()

