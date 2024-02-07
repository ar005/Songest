# Songest

A tool designed to automate the process of downloading songs using SpotDL and then adding them to a Jellyfin media server. It simplifies the process of acquiring music and integrating it seamlessly into your Jellyfin library.


# Install Docker


```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh 
```

# Modifying for your deployment


Update your Jellyfin address and API key in update_jellyfin.py.

Update your bot token in main.py.

# Run with docker

```

docker build -t songest .
docker run -d -v library:library songest
```
# Ussage

Just send the link of playlist or album link to the bot and it will download it fir your jellyfin

# This tool is derived from spotify-downloader by spoDl

check out https://github.com/spotDL/spotify-downloader

# Fair use
The purpose of this tool is not to encourage piracy, I fully support the creator of music getting full credit and monetry fee for their honest work. This tool doesn`t support piracy.
