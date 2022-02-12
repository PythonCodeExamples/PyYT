#!/usr/bin/bash
sudo apt install mpv
pip3 install -r requirements.txt
sudo pip3 install -t /usr/bin/ --upgrade youtube-dl
chmod +x app/main.py
