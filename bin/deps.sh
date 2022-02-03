#!/bin/bash

sudo add-apt-repository -y ppa:deadsnakes/ppa 
sudo apt-get update

sudo apt-get install -y build-essential tzdat musl-dev jpeg-dev zlib-dev libssl-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
sudo apt-get install -y python3 python3-distutils python3-setuptools python3-venv python3-dev
sudo apt-get install gcc-arm*