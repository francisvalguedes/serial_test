#!/bin/bash
sudo apt install -y python3-venv
python3 -m venv env
# pip install virtualenv
# sudo apt install python3 virtualenv

# virtualenv env
source env/bin/activate
# pip install -r requirements.txt