import os
import geopandas as gpd
from shapely.geometry import LineString
from shapely.ops import unary_union

OUTPUT_PATH = os.path.join("dev1", "data", "ohio_trails.geojson")

# TODO: point this to your source trails dataset
SOURCE_PATH = r"/path/to/source_trails_file.geojson"

print("Loading source data...")
gdf = gpd.read_file(SOURCE_PATH)

# Basic trail filtering (adjust to your schema)
if "FTYPE" in gdf.columns:
    trails = gdf[gdf["FTYPE"].astype(str).str.contains("trail", case=False, na=False)]
else:
    trails = gdf

def clean_name(row):
    raw = str(row.get("NAME") or "").strip()
    park = str(row.get("PARK_NAME") or "").strip()

    garbage = {"trail 001", "unnamed trail", "footpath", "bike path", "multi-use trail"}
    if not raw or raw.lower() in garbage:
        if park:
            return f"{park} Trail"
        return "Unnamed Trail"
    return raw

trails["name"] = trails.apply(clean_name, axis=1)

merged_records = []
for name, group in trails.groupby("name"):
    geom = unary_union(group.geometry)
    if isinstance(geom, LineString):
        merged_geom = geom
    else:
        lines = [g for g in getattr(geom, "geoms", []) if isinstance(g, LineString)]
        if not lines:
            continue
        merged_geom = max(lines, key=lambda g: g.length)

    merged_records.append({"name": name, "geometry": merged_geom})

merged = gpd.GeoDataFrame(merged_records, crs=trails.crs)

merged = merged.to_crs(epsg=3857)
merged["length_miles"] = merged.geometry.length / 1609.34
merged = merged.to_crs(epsg=4326)

def region_from_lat(lat):
    if lat > 41.0:
        return "north"
    elif lat < 39.0:
        return "south"
    return "central"

merged["region"] = merged.geometry.apply(
    lambda g: region_from_lat(g.coords[0][1]) if isinstance(g, LineString) else "central"
)

merged["id"] = range(1, len(merged) + 1)

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
print(f"Writing {OUTPUT_PATH} ...")
merged.to_file(OUTPUT_PATH, driver="GeoJSON")
print("Done.")
