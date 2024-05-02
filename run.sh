#!/bin/bash

# Update package lists
apt update
apt install -y python3-pip

pip3 install dash
pip3 install dash_bootstrap_components
pip3 install plotly
pip3 install pandas
pip3 install jupyter