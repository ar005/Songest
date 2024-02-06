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

docker build -t Songest .
docker run -d -v library:library Songest
```
