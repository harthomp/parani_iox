#!/bin/bash
printf "\n\n IF FIRST TIME: PRESS ENTER UNTIL IOXCLIENT CONFIG FINISHED!\n\n"
./ioxclient -v
apt-get update
apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common -y
apt-get update
apt-get install docker.io -y
