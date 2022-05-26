import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = "data/NYC_central_park_2021_full.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, highs, and lows from the file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[7])
        highs.append(high)
        low = int(row[8])
        lows.append(low)

# Plot the data.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format the plot.
ax.set_title("Daily high and low temperatures, NYC, 2021", fontsize=24)
ax.set_xlabel("", fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="both", labelsize=16)

plt.tight_layout()
plt.show()
