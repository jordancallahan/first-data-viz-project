import requests
import json

r = requests.get(
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson"
)

r = r.json()

readable_file = "data/readable_eq_data_month.json"
with open(readable_file, "w") as f:
    json.dump(r, f)
