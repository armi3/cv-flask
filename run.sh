#!/bin/bash


echo "Corriendo mi contenedor"
docker container run -it \
    --rm -p 5000:5000 registry.gitlab.com/ufm/flasky-students:latest

