#!/usr/bin/env bash

# Build image
docker build --tag=clickecho .

# List containers
docker image ls

# Run Container
docker run -it clickecho python app.py --name "Big John"