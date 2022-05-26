import json

# Explore the structure of the data.
filename = "data/readable_eq_data.json"
with open(filename) as f:
    all_eq_data = json.load(f)

# Look at just the earthquake dictionaries.
all_eq_dicts = all_eq_data["features"]

# Create list of each earthquake's magnitude.
mags = [eq_dict["properties"]["mag"] for eq_dict in all_eq_dicts]

# Extract the longitude and latitude of each earthquake.
lons = [eq_dict["geometry"]["coordinates"][0] for eq_dict in all_eq_dicts]
lats = [eq_dict["geometry"]["coordinates"][1] for eq_dict in all_eq_dicts]

print(mags[:10])
print(lons[:5])
print(lats[:5])
