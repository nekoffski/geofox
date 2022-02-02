#!/bin/bash

if [ -d ./venv ]; then
    sudo rm -rf ./venv
fi

echo "$ generating venv"
sudo python3.8 -m venv ./venv
sudo ./venv/bin/python3.8 -m pip install --upgrade pip

source ./venv/bin/activate

echo "$ installing deps"
sudo ./venv/bin/python3.8 -m pip install -r ./misc/requirements.txt
