# Run build script
./build.ps1

# Docker Hub credentials (replace with your credentials)
# $dockerHubUsername = "your_docker_hub_username"
# $dockerHubPassword = "your_docker_hub_password"

# Docker Images
$frontendImage = "albh/converter_frontend"
$serviceImage = "albh/converter_service"

# # Kubernetes Deployment Name
$k8sDeploymentName1 = "converter-deployment"
$k8sDeploymentName2 = "frontend-deployment"

# # Authenticate with Docker Hub
# echo $dockerHubPassword | docker login --username $dockerHubUsername --password-stdin

# Tag and Push Frontend Image
# docker tag $frontendImage ":latest"
docker push $frontendImage

# Tag and Push Service Image
# docker tag $serviceImage ":latest"
docker push $serviceImage

Start-Sleep -Seconds 2

kubectl apply -f converter-frontend.yml
kubectl apply -f converter-service.yml

# Restart Kubernetes Deployment
kubectl rollout restart deployment/$k8sDeploymentName1
kubectl rollout restart deployment/$k8sDeploymentName2
