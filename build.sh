#!/bin/bash
docker buildx build --platform linux/arm64 -t parani ./src
docker save -o ./src/rootfs.tar parani
./ioxclient package ./src
mv ./src/package.tar ..
