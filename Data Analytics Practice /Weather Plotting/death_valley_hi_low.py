from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import csv

# Define the path to the CSV data file
path = Path('weather_data/death_valley_2021_full.csv')

# Read the file and split into lines
lines = path.read_text().splitlines()

# Create a CSV reader object
reader = csv.reader(lines)

# Read the header row
header_row = next(reader)

# Print the header row for reference
print(header_row)

# Print each column's index and name for reference
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Initialize lists to store data
dates, highs, lows, tobs, rainfall = [], [], [], [], []

# Loop through each row in the CSV file
for row in reader:
    # Parse the date from the third column (index 2)
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        # Extract high, low, average temperature, and rainfall from the row
        high = int(row[6])      # High temperature (index 6)
        low  = int(row[7])      # Low temperature (index 7)
        tob = int(row[8])       # Average temperature (index 8)
        rain = float(row[3])    # Rainfall (index 3)
    except ValueError:
        # Handle missing or invalid data
        print(f'Missing data for {current_date}')
    else:
        # Append valid data to respective lists
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        tobs.append(tob)
        rainfall.append(rain)

# Set the plot style
plt.style.use('ggplot')

# Create a figure and axis object with a specific size
fig, ax = plt.subplots(figsize=(10,6))

# Plot high temperatures
ax.plot(dates, highs, c='red', label='Highs')
# Plot low temperatures
ax.plot(dates, lows, c='blue', label='Lows')
# Plot average temperatures
ax.plot(dates, tobs, c='green', label='Average Temperatures')
# Plot rainfall
ax.plot(dates, rainfall, c='orange', label='Rainfall')

# Fill the area between highs and lows
ax.fill_between(dates, highs, lows, facecolor='purple', alpha=0.1)

# Set the title and axis labels
title = ('Daily High and Low Temperatures, 2021\nDeath Valley, CA')
ax.set_title(title, fontsize=20)
ax.set_xlabel('Day', fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)

# Format the date labels on the x-axis
fig.autofmt_xdate()

# Add a legend to the plot
ax.legend()

# Display the plot
plt.show()
