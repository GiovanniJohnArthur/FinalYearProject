#!/usr/bin/bash

sudo mkdir /opt/gvn/
sudo cp -r . /opt/gvn/
sudo chmod +x /opt/gvn/gvn--main/gvn
sudo ln -sf /opt/gvn/gvn--main/gvn /usr/local/bin/gvn
echo "To call the framework type gvn"
