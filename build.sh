#!/bin/bash

# Loop through each subdirectory (one level down)
for dir in */; do
    # Extract the directory name without the trailing slash
    dirname=$(basename "$dir")

    # Check if Dockerfile exists in the subdirectory
    if [ -f "$dir/dockerfile" ]; then
        # Convert the directory name to lowercase
        lowercase_dirname=$(echo "$dirname" | tr '[:upper:]' '[:lower:]')

        # Build the image name based on the directory name
        image_name="converter-app/$lowercase_dirname:latest"  # Replace your-registry with your actual registry

        # Enter the subdirectory
        cd "$dir" || continue

        # Run docker build in the subdirectory with the dynamic image name
        docker build -t "$image_name" .

        # Return to the parent directory
        cd ..
    else
        # Echo a message if no Dockerfile is found
        echo "No Dockerfile found in $dirname"
    fi
done

docker-compose up
