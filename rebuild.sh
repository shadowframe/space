#!/bin/bash

docker build -t space .
docker kill $(docker ps -q)
docker system prune --force
docker run -d -p 80:80 space
