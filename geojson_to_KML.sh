#!/bin/bash

#Load Timer
start=$SECONDS

# ZONE=10

# Directory containing GeoJSON files
geojson_dir="/mnt/bulldog/DOM/Scripts/TerraDSM/Outputs/WichitaFalls"

# Output directory for KML files
kml_dir="/mnt/bulldog/DOM/Scripts/TerraDSM/Outputs/WichitaFalls/KML_Output/"
#Start Timer

printf "Converting GeoJSONs to KMLs ." 
# printf "\nCurrently Running UTM Zone: $ZONE ....\n"

mkdir -p $kml_dir

# Iterate through GeoJSON files in the directory
for geojson_file in "$geojson_dir"/*.geojson; do
    # Get the base filename without extension
    base_filename=$(basename -- "$geojson_file" .geojson)
    # Construct the output KML filename
    kml_file="$kml_dir/$base_filename.kml"
    # Convert GeoJSON to KML using ogr2ogr
    ogr2ogr -f "KML" "$kml_file" "$geojson_file"
done

echo "Conversion complete."

end=$SECONDS

duration=$(((end - start)/60))

# Prints processing times
printf "Total time to process: %.2f minutes." "$duration"
printf "\n"
printf "Output Location: $kml_dir"
printf "\n---------------------\n"