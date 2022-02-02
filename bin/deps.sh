#!/bin/bash

sudo apt-get install -y build-essential
sudo apt-get install -y python3.8
sudo apt-get install -y python3-setuptools
sudo apt-get install -y python3.8-venv
sudo apt-get install -y python3.8-dev
sudo apt-get install -y libffi-dev

sudo python3.8 -m ensurepip
sudo python3.8 -m pip install virtualenv