#!/bin/bash
docker build -t parani ./src
docker save -o ./src/rootfs.tar parani
./ioxclient package ./src 
