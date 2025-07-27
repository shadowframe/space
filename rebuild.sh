#!/bin/bash

# Build a Docker image with the tag "space" from the current directory
docker build -t space . 

# Kill all running Docker containers
docker kill $(docker ps -q)

# Remove all unused Docker objects (containers, networks, images, etc.) to free up space
docker system prune --force

# Run a new container from the "space" image in detached mode (-d) and map port 80 of the host to port 80 of the container
docker run -d -p 80:80 space
