#!/bin/bash

# Load Timer
start=$SECONDS

# Parent directory containing subdirectories with GeoJSON files
parent_dir="/mnt/mastiff/SUMMIT/Production/DO2S/china/n50/A3/input/aoi/geojson"

# Print conversion status
printf "Converting 2km buffered GeoJSONs to KMLs.\n"

# Check if ogr2ogr is installed
if ! command -v ogr2ogr &> /dev/null; then
    echo "Error: ogr2ogr could not be found. Please install GDAL."
    exit 1
fi

# Iterate through each subdirectory in the parent directory
for sub_dir in "$parent_dir"/*/; do
    # Ensure it's a directory
    if [ -d "$sub_dir" ]; then
        # Output directory for KML files
        kml_dir="${sub_dir}KML_Output"
        # Create output directory if it doesn't exist
        mkdir -p "$kml_dir"
        
        # Print current subdirectory being processed
        printf "Processing directory: $sub_dir\n"

        # Iterate through GeoJSON files in the subdirectory
        for geojson_file in "$sub_dir"*.geojson; do
            # Check if any GeoJSON files are found
            if [ ! -e "$geojson_file" ]; then
                echo "No GeoJSON files found in $sub_dir."
                break
            fi
            
            # Get the base filename without extension
            base_filename=$(basename -- "$geojson_file" .geojson)
            # Construct the output KML filename
            kml_file="$kml_dir/$base_filename.kml"
            # Convert GeoJSON to KML using ogr2ogr
            ogr2ogr -f "KML" "$kml_file" "$geojson_file"
        done
    fi
done

# Print completion message
echo "Conversion complete."

# Calculate and print processing time
end=$SECONDS
duration=$((end - start))
minutes=$((duration / 60))
seconds=$((duration % 60))

printf "Total time to process: %d minutes and %d seconds." "$minutes" "$seconds"
printf "\n---------------------\n"
