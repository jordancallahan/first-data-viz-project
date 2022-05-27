from plotly.graph_objects import Layout, Figure

import json

# Explore the structure of the data.
filename = "data/readable_eq_data_month.json"
with open(filename) as f:
    all_eq_data = json.load(f)

# Look at just the earthquake dictionaries.
all_eq_dicts = all_eq_data["features"]

# Create list of each earthquake's magnitude.
mags = [eq_dict["properties"]["mag"] for eq_dict in all_eq_dicts]
hover_texts = [eq_dict["properties"]["title"] for eq_dict in all_eq_dicts]

# Extract the longitude and latitude of each earthquake.
lons = [eq_dict["geometry"]["coordinates"][0] for eq_dict in all_eq_dicts]
lats = [eq_dict["geometry"]["coordinates"][1] for eq_dict in all_eq_dicts]

# Map the earthquakes.
data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_texts,
        "marker": {
            "size": [4 * mag for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]
my_layout = Layout(title="Global Earthquakes - Last 30 Days")

fig = Figure(data=data, layout=my_layout)

# Comment out below to create html files and images of the visualization.
# fig.write_image("global_earthquakes_month.png")
# fig.write_html("global_earthquakes_month.html")
fig.show()
