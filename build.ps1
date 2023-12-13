# Function to build Docker image and tag it
function BuilDockeImage($directory) {
    $imageName = "albh/" + $directory.ToLower() + ":latest"
    
    # Check if Dockerfile exists in the specified directory
    $dockerfilePath = Join-Path $rootDirectory $directory
    if (Test-Path "$dockerfilePath\Dockerfile") {
        Write-Host "Building Docker image for $directory..."
        
        # Run docker build and tag the image
        docker build -t $imageName $dockerfilePath
        
        Write-Host "Docker image built and tagged: $imageName"
    }
    else {
        Write-Host "No Dockerfile found in $directory."
    }
}

# Main script
$rootDirectory = Get-Location

# Get all subdirectories
$subdirectories = Get-ChildItem -Directory -Path $rootDirectory | Select-Object -ExpandProperty Name

# Iterate through each subdirectory
foreach ($subdirectory in $subdirectories) {
    # Call the function to build Docker image for each subdirectory
    BuilDockeImage $subdirectory
}

# docker-compose up