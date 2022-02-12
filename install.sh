#!/usr/bin/bash

sudo apt install mpv, curl, rlwrap
pip3 install -r requirements.txt

sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp

echo "#!/usr/bin/bash
cd $PWD/app
./main.py" > start_app.sh

chmod +x app/main.py 
chmod +x start_app.sh

sudo ln -f -s /usr/local/bin/yt-dlp /usr/bin/youtube-dl
sudo ln -f -s $PWD/start_app.sh /usr/bin/pyyt
