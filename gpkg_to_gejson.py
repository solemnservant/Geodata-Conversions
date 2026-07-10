import geopandas as gpd
from pathlib import Path
osm_path = Path('/mnt/bulldog/Source_Vectors/OSM/2024/Hydro_Vectors/africa_20240419')

gpkg_files = list(osm_path.rglob("*waterbodies*.gpkg"))

print (f"\nA total of {len(gpkg_files)} will be coverted to geojson file(s)")
print (f"\nThe following files will be added: \n")

for gpkg_file in gpkg_files:
    print(f"{gpkg_file.stem} has been generated.")    
    
    poly_file = gpd.read_file(gpkg_file)
    print (str(gpkg_file))
    print (poly_file)
    poly_out = poly_file.to_file(gpkg_file.parent.joinpath(gpkg_file.stem + "_multipolygons.geojson"), driver='GeoJSON', layer='multipolygons')
    