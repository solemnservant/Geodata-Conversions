import geopandas as gpd
from pathlib import Path
osm_path = Path('/mnt/bulldog/Source_Vectors/OSM/2024/Urban_Vectors/buffered_vectors')

gpkg_files = list(osm_path.rglob("*runways*.gpkg"))

all_water = [] 

print (f"\nA total of {len(gpkg_files)} will be added to the global GPKG file")
print (f"\nThe following files will be added: \n")

for gpkg_file in gpkg_files:
    print(f"{gpkg_file.stem} has added to global GPKG.")    
    
    water = gpd.read_file(gpkg_file) 
    all_water.append(water)

all_water_gdf = gpd.pd.concat(all_water, ignore_index=True)
outfile = all_water_gdf.to_file(gpkg_file.parent.joinpath("OSM_global_runways_90m_buffer.gpkg"), driver='GPKG', layer='multipolygons')
    