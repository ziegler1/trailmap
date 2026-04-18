import requests
import json
import os

URL = "https://www.sciencebase.gov/catalog/items?filter=tags=National Digital Trails&format=geojson"

DATA_PATH = os.path.join("data", "ohio_trails.geojson")

def fetch_and_save_trails():
    print("Fetching USGS trail data...")
    r = requests.get(URL)
    r.raise_for_status()
    data = r.json()

    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("Saved:", DATA_PATH)

if __name__ == "__main__":
    fetch_and_save_trails()
