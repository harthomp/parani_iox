#!/bin/bash
docker build -t parani .
docker save -o rootfs.tar parani
./ioxclient package .
