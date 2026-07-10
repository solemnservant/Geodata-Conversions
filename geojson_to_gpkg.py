import subprocess
from pathlib import Path

def convert_geojson_to_gpkg(input_dir, output_gpkg):
    """
    Converts all GeoJSON files in the input directory and its subdirectories to a GeoPackage.

    Parameters:
    input_dir (str): Path to the directory containing GeoJSON files.
    output_gpkg (str or Path): Path to the output GeoPackage file.
    """
    geojson_files = list(input_dir.rglob("*waterbodies*.geojson"))
    
    print (f"\nA total of {len(geojson_files)} will be added to the global GPKG file")
    print (f"the following files will be added: \n")
    for i in geojson_files: 
        print(f"{i.stem}")
    
    for geojson_file in geojson_files:
        print(f"{geojson_file.stem} has been added to the global database.")
        # Use the filename without extension as the layer name
        layer_name = geojson_file.stem
        # Construct the ogr2ogr command with the -append option to prevent overwriting
        command = [
            'ogr2ogr', 
            '-f', 'GPKG', 
            str(output_gpkg), 
            str(geojson_file), 
            '-nln', layer_name, 
            '-append'
        ]
        subprocess.run(command, check=True)

if __name__ == "__main__":
    # I/O
    input_dir = Path("/mnt/bulldog/Source_Vectors/OSM/2024/Hydro_Vectors")
    output_gpkg_file = Path("/mnt/bulldog/Source_Vectors/OSM/2024/Hydro_Vectors/global_waterbodies_multipolygons.gpkg")

    #calling function to convert geojsons to gpkg file
    convert_geojson_to_gpkg(input_dir, output_gpkg_file)