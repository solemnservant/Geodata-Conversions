import subprocess
from pathlib import Path

# Directory of GPKG files
osm_dir = Path('/mnt/bulldog/Source_Vectors/OSM/2024/Hydro_Vectors')

# Output location for vector tile in mbtiles format
maptile_fp = Path("/mnt/bulldog/Source_Vectors/OSM/2024/Hydro_Vectors")

# Output location for vector tile in gpkg format
gpkg_maptile_fp = Path("/mnt/bulldog/Source_Vectors/OSM/2024/Hydro_Vectors/")

# Query OSM directory and list all GPKG files to convert
gpkg_files = list(osm_dir.rglob('*waterbodies*.gpkg'))

# Function to get layers from a GPKG file
def get_layers(gpkg_file):
    command = ["ogrinfo", str(gpkg_file)]
    result = subprocess.run(command, capture_output=True, text=True)
    layers = []
    for line in result.stdout.splitlines():
        if line.strip().startswith("0: ") or line.strip().startswith("1: ") or line.strip().startswith("2: ")  or line.strip().startswith("3: ") or line.strip().startswith("4: ") or line.strip().startswith("5: "):
            layer_name = line.split()[1]
            layers.append(layer_name)
    return layers

# Loop through each GPKG file and convert it to GeoJSON
for gpkg_fp in gpkg_files:
    print(f"gpkg: {gpkg_fp}")
    layers = get_layers(gpkg_fp)
    for layer in layers:
        # Generate the output GeoJSON file name
        geojson_file = gpkg_fp.with_stem(gpkg_fp.stem + f"_{layer}").with_suffix('.geojson')
        print(f"geojson: {geojson_file}")

        # Convert to GeoJSON using ogr2ogr
        geojson_out = ["ogr2ogr", "-f", "GeoJSON", str(geojson_file), str(gpkg_fp), layer]
        result = subprocess.run(geojson_out, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error converting {layer} from {gpkg_fp} to GeoJSON: {result.stderr}")

# # Query OSM directory and list all GeoJSON files to convert
# geojson_files = list(osm_dir.rglob('*waterbodies*_multipolygons*.geojson'))

# # Build the Tippecanoe command
# maptile_out = ["tippecanoe", "-o", str(maptile_fp.joinpath("OSM_global_waterbodies_multipolygons_maptiles.mbtiles"))] + [str(geojson_file) for geojson_file in geojson_files]

# # Run the Tippecanoe command
# subprocess.run(maptile_out)

# # Use ogr2ogr to convert .mbtiles to .gpkg
# gpkg_maptile_out = ['ogr2ogr', '-f', 'GPKG', str(gpkg_maptile_fp.joinpath("OSM_global_waterbodies_multipolygons_maptiles.gpkg")), str(maptile_fp.joinpath("OSM_global_maptiles.mbtiles"))]
# subprocess.run(gpkg_maptile_out)
