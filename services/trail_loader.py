import json
import os

DATA_PATH = os.path.join("data", "ohio_trails.geojson")

def load_trails():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_trail_by_id(trail_id):
    trails = load_trails().get("features", [])
    for feature in trails:
        props = feature.get("properties", {})
        if str(props.get("id")) == str(trail_id):
            return feature
    
    if trail_id.isdigit():
        index = int(trail_id)
        if 0 <= index < len(trails):
            return trails[index]
    
    return None
