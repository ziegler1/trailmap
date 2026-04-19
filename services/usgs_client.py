raise SystemExit("USGS fetch disabled — using local file instead.")
import requests
import json
import os

OUTPUT_FILE = "data/ohio_trails.geojson"

# Ohio bounding box
params = {
    "f": "geojson",
    "where": "1=1",
    "geometryType": "esriGeometryEnvelope",
    "spatialRel": "esriSpatialRelIntersects",
    "geometry": json.dumps({
        "xmin": -84.82,
        "ymin": 38.40,
        "xmax": -80.52,
        "ymax": 41.98,
        "spatialReference": {"wkid": 4326}
    }),
    "outFields": "*",
    "returnGeometry": "true"
}

URL = "https://services.nationalmap.gov/arcgis/rest/services/USGSTrails/MapServer/0/query"

print("Fetching Ohio trails from USGS…")
response = requests.get(URL, params=params)

if response.status_code != 200:
    print("Error:", response.status_code, response.text)
    exit()

data = response.json()

os.makedirs("data", exist_ok=True)

with open(OUTPUT_FILE, "w") as f:
    json.dump(data, f)

print(f"Saved {len(data.get('features', []))} trails to {OUTPUT_FILE}")
