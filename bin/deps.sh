#!/bin/bash

sudo apt-get install build-essential
sudo apt-get install -y python3.9
sudo apt-get install -y python3-setuptools
sudo apt-get install -y python3.9-venv
sudo apt-get install -y python3.9-dev

sudo python3.9 -m ensurepip
sudo python3.9 -m pip install virtualenv