import subprocess
from pathlib import Path

# Directory of GPKG files
osm_dir = Path('/mnt/bulldog/Source_Vectors/OSM/2024/Hydro_Vectors')

# Output location for vector tile in mbtiles format
maptile_fp = Path("/mnt/bulldog/Source_Vectors/OSM/2024/Hydro_Vectors")

# Output location for vector tile in gpkg format
gpkg_maptile_fp = Path("/mnt/bulldog/Source_Vectors/OSM/2024/Hydro_Vectors")

# Query OSM directory and list all GeoJSON files to convert
geojson_files = list(osm_dir.rglob('*waterbodies*.geojson'))

# Build the Tippecanoe command
maptile_out = ["tippecanoe", "-o", str(maptile_fp.joinpath("OSM_global_waterbodies_multipolygons_maptiles.mbtiles"))] + [str(geojson_file) for geojson_file in geojson_files]

# Run the Tippecanoe command
subprocess.run(maptile_out)

# # Use ogr2ogr to convert .mbtiles to .gpkg
# gpkg_maptile_out = ['ogr2ogr', '-f', 'GPKG', str(gpkg_maptile_fp.joinpath("OSM_global_waterbodies_multipolygons_maptiles.gpkg")), str(maptile_fp.joinpath("OSM_global_maptiles.mbtiles"))]
# subprocess.run(gpkg_maptile_out)