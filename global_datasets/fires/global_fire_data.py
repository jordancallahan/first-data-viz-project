import requests
import csv

from plotly.graph_objects import Layout, Figure
from datetime import datetime

CSV_URL = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/noaa-20-viirs-c2/csv/J1_VIIRS_C2_Global_7d.csv"

with requests.get(CSV_URL, stream=True) as r:
    lines = (line.decode("utf-8") for line in r.iter_lines())
    reader = csv.reader(lines)
    header_row = next(reader)

    # Get latitude, longitude, brightness from file.
    lats, lons, brights = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], "%Y-%m-%d")
        try:
            lat = float(row[0])
            lon = float(row[1])
            bright = float(row[2])
        except ValueError:
            print(f"Missing data for {current_date}.")
        else:
            lats.append(lat)
            lons.append(lon)
            brights.append(bright)

# Map the fires.
data = [{"type": "densitymapbox", "lat": lats, "lon": lons, "z": brights, "radius": 2}]
my_layout = Layout(title="Global Fires - Last 7 Days")

fig = Figure(data=data, layout=my_layout)
fig.update_layout(mapbox_style="stamen-terrain")
# fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Comment out below to create html files and images of the visualization.
# fig.write_image("global_fires_month.png")
# fig.write_html("global_fires_month.html")
fig.show()
