#!/usr/bin/bash
sudo apt install mpv
sudo apt install curl
pip3 install -r requirements.txt
chmod +x app/main.py start_app.sh

sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp

sudo ln -f -s /usr/local/bin/yt-dlp /usr/bin/youtube-dl
sudo ln -f -s $PWD/start_app.sh /usr/bin/pyyt
