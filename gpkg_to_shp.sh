#!/bin/bash

#Load Timer
start=$SECONDS

# ZONE=10

# Directory containing gpkg files
gpkg_dir="/mnt/Projects1/GGS/Source_Data/Vectors/OSM/DO6/DO6_ProdBlocks/B18_B25/RiverLines"

# Output directory for shp files
shp_dir="/mnt/Projects1/GGS/Source_Data/Vectors/OSM/DO6/DO6_ProdBlocks/B18_B25/RiverLines"
#Start Timer

printf "Converting gpkgs to shps..." 
# printf "\nCurrently Running UTM Zone: $ZONE ....\n"

mkdir -p $shp_dir

# Iterate through gpkg files in the directory
for gpkg_file in "$gpkg_dir"/*.gpkg; do
    # Get the base filename without extension
    base_filename=$(basename -- "$gpkg_file" .gpkg)
    # Construct the output shp filename
    shp_file="$shp_dir/$base_filename.shp"
    # Convert gpkg to shp using ogr2ogr
    ogr2ogr -f "ESRI Shapefile" "$shp_file" "$gpkg_file"
done

echo "Conversion complete."

end=$SECONDS

duration=$(((end - start)/60))

# Prints processing times
printf "Total time to process: %.2f minutes." "$duration"
printf "\n"
printf "Output Location: $shp_dir"
printf "\n---------------------\n"